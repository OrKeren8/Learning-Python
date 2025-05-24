import time
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from typing import List

class NearestNeighbor:

    def __init__(self, x_train: DataFrame, y_train: pd.Series):
        """Initialize the NearestNeighbor classifier with training data
        Args:
            x_train (DataFrame): training features
            y_train (pd.Series): training labels
        """
        self.x_train = x_train.to_numpy()
        self.y_train = y_train

    def euclidean_distance(self, x: np.ndarray, y: np.ndarray) -> float:
        """calculate the euclidean distance between two n-dimensional vectors
        Args:
            x (np.ndarray): first vector
            y (np.ndarray): second vector
        Returns:
            float: euclidean distance between x and y
        """
        return np.sqrt(np.sum((x - y) ** 2))

    def _get_nearest_neighbors_class(self, origin: np.ndarray, radius: float):
        """Get the class of the nearest neighbors within a given radius
        Args:
            origin (np.ndarray): the point for which to find the nearest neighbors
            radius (float): radius within which to consider neighbors
        Returns:
            str: class of the nearest neighbor, or None if no neighbors found"""
        distances = np.linalg.norm(self.x_train - origin, axis=1)
        within_radius = distances <= radius
        labels_within = self.y_train[within_radius]
        values, counts = np.unique(labels_within, return_counts=True)
        return values[np.argmax(counts)] if counts.size > 0 else self.y_train[0]
        
    def check_best_radius(self, data_set: DataFrame, predicted: pd.Series, start: int, end: int, jump = 1) -> int:
        """Find the best radius for the nearest neighbor algorithm
        Args:
            data_set (DataFrame): input data to find the best radius
            start (int): starting radius value
            end (int): ending radius value
            jump (int): step size for radius values
        Returns:
            int: best radius found
        """
        best = 0
        for radius in range(start, end, jump):
            predictions = self.predict(data_set, radius)
            accuracy = accuracy_score(predicted, predictions)
            if accuracy > best:
                best = radius
            print(f'Radius: {radius}, Accuracy: {accuracy}')
        return best

    def predict(self, data: DataFrame, radius: float = 1):
        """Predict the class of each instance in the data using the nearest neighbor algorithm
        Args:
            data (DataFrame): input data for which to predict the class
            radius (float): radius within which to consider neighbors
        Returns:
            List: list of predicted classes for each instance in the data
        """
        predictions = []
        np_data = data.to_numpy()
        for row in np_data:
            predictions.append(self._get_nearest_neighbors_class(row, radius))
        return predictions

def scale_features(df: DataFrame) -> DataFrame:
    """Scale the features of the dataframe using StandardScaler
    Args:
        df (DataFrame): input dataframe with features to be scaled
    Returns:
        DataFrame: scaled dataframe
    """
    scalar = StandardScaler()
    data_scaled = pd.DataFrame(scalar.fit_transform(df))
    return data_scaled

def upload_data(data_file: str) -> DataFrame:
    """Load data from a CSV file into a DataFrame
    Args:
        data_file (str): path to the CSV file
    Returns:
        DataFrame: loaded data
    """
    df = pd.read_csv(data_file)
    return df

def classify_with_NNR(data_trn: str, data_vld: str, df_tst: DataFrame) -> List:
    #  the data_tst dataframe should only(!) be used for the final predictions your return
    print(f'starting classification with {data_trn}, {data_vld}, predicting on {len(df_tst)} instances')
    df_trn = upload_data(data_trn)
    x_train, y_train = df_trn.drop(['class'], axis=1), df_trn['class']
    # df_trn_scaled = scale_features(df_trn.drop(['class'], axis=1))
    df_vld = upload_data(data_vld)
    x_val,  y_val = df_vld.drop(['class'], axis=1), df_vld['class']
    # df_vld_scaled = scale_features(df_vld.drop(['class'], axis=1))

    nn = NearestNeighbor(x_train, y_train)
    radius = nn.check_best_radius(x_val, y_val, start=1, end=200, jump=10)

    df_tst_scaled = scale_features(df_tst)
    predictions = nn.predict(df_tst_scaled, radius)

    return predictions


students = {'id1': '315155531', 'id2': '000000000'}

if __name__ == '__main__':
    start = time.time()

    with open('config.json', 'r', encoding='utf8') as json_file:
        config = json.load(json_file)

    df = pd.read_csv(config['data_file_test'])
    predicted = classify_with_NNR(config['data_file_train'],
                                  config['data_file_validation'],
                                  df.drop(['class'], axis=1))

    labels = df['class'].values
    if not predicted:  # empty prediction, should not happen in your implementation
        predicted = list(range(len(labels)))

    assert(len(labels) == len(predicted))  # make sure you predict label for all test instances
    print(f'test set classification accuracy: {accuracy_score(labels, predicted)}')

    print(f'total time: {round(time.time()-start, 0)} sec')
