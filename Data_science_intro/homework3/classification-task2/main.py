import time
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from typing import List

class NearestNeighbor:

    def __init__(self, x_train: DataFrame, y_train: pd.Series, x_vld: DataFrame, y_vld: pd.Series):
        """Initialize the Nearest Neighbor classifier with training and validation data
        Args:
            x_train (DataFrame): training features
            y_train (Series): training labels
            x_vld (DataFrame): validation features
            y_vld (Series): validation labels
        """
        self.x_train = x_train.to_numpy()
        self.y_train = y_train.to_numpy()
        self.x_vld = x_vld.to_numpy()
        self.y_vld = y_vld.to_numpy()
        self.fit_distances = self.pre_calc_distances()

    def pre_calc_distances(self):
        """Pre-calculate distances from training data to validation data
        Returns:
            np.ndarray: array of distances from each validation instance to all training instances
        """
        distances = []
        for row in self.x_vld:
            distances.append(self._calc_distances(row))
        return np.array(distances)
    
    def _calc_distances(self, origin: np.ndarray):
        """Calculate the Euclidean distance from a given origin to all training instances
        Args:
            origin (np.ndarray): the point from which distances are calculated
        Returns:
            np.ndarray: array of distances from the origin to each training instance
        """
        return np.linalg.norm(self.x_train - origin, axis=1)
    
    def _get_nearest_neighbors_class(self, origin: np.ndarray, radius: float, pre_dist_idx: int = -1):
        """Get the class of the nearest neighbor within a specified radius
        Args:
            origin (np.ndarray): the point from which to find the nearest neighbor
            radius (float): the radius within which to consider neighbors
            pre_dist_idx (int): index of pre-calculated distances, -1 if not using pre-calculated distances
        Returns:
            int: the class of the nearest neighbor within the radius, or the first class if no neighbors found"""
        distances = self.fit_distances[pre_dist_idx] if pre_dist_idx > 0 else self._calc_distances(origin)
        within_radius = distances <= radius
        labels_within = self.y_train[within_radius]
        values, counts = np.unique(labels_within, return_counts=True)
        return values[np.argmax(counts)] if counts.size > 0 else self.y_train[0]
        
    def check_best_radius(self, start: float, end: float, jump) -> float:
        """Check the best radius for classification by evaluating accuracy on validation data
        Args:
            start (float): starting radius value
            end (float): ending radius value
            jump (float): step size for radius increment
        Returns:
            float: the radius that gives the best accuracy on validation data
        """
        best_acc, best_rad = 0, 0
        for radius in np.arange(start, end, jump):
            predictions = self.predict(self.x_vld, radius, from_fit=True)
            accuracy = accuracy_score(self.y_vld, predictions)
            if accuracy > best_acc:
                best_acc = accuracy
                best_rad = radius
            print(f'Radius: {radius}, Accuracy: {accuracy}, Best so far: {best_rad}')
        return best_rad

    def predict(self, np_data: np.ndarray, radius: float = 1, from_fit: bool = False) -> List:
        """Predict the class labels for the given data using the nearest neighbor algorithm
        Args:
            np_data (np.ndarray): data for which to predict class labels
            radius (float): radius within which to consider neighbors
            from_fit (bool): whether to use pre-calculated distances from fit
        Returns:
            List: predicted class labels for the input data
        """
        predictions = []
        for i in range(len(np_data)):
            predictions.append(self._get_nearest_neighbors_class(np_data[i], radius, i if from_fit else -1))
        return predictions

def scale_features(df: DataFrame) -> DataFrame:
    """Scale features of the DataFrame using StandardScaler
    Args:
        df (DataFrame): DataFrame containing features to be scaled
    Returns:
        DataFrame: scaled features
    """
    scalar = StandardScaler()
    data_scaled = pd.DataFrame(scalar.fit_transform(df))
    return data_scaled

def upload_data(data_file: str) -> DataFrame:
    """Upload data from a CSV file
    Args:
        data_file (str): path to the CSV file
    Returns:
        DataFrame: DataFrame containing the data from the CSV file
    """
    df = pd.read_csv(data_file)
    return df

def classify_with_NNR(data_trn: str, data_vld: str, df_tst: DataFrame) -> List:
    """Classify test data using Nearest Neighbor Radius algorithm
    Args:
        data_trn (str): path to the training data file
        data_vld (str): path to the validation data file
        df_tst (DataFrame): DataFrame containing test data
    Returns:
        List: predicted class labels for the test data
    """
    print(f'starting classification with {data_trn}, {data_vld}, predicting on {len(df_tst)} instances')
    df_tst = scale_features(df_tst)
    df_trn = upload_data(data_trn)
    x_train, y_train = scale_features(df_trn.drop(['class'], axis=1)), df_trn['class']
    df_vld = upload_data(data_vld)
    x_val,  y_val = scale_features(df_vld.drop(['class'], axis=1)), df_vld['class']

    nn = NearestNeighbor(x_train, y_train, x_val, y_val)
    radius = nn.check_best_radius(start=1, end=4, jump=0.1)
    print(f'Best radius found: {radius}')
    predictions = nn.predict(df_tst.to_numpy(), radius)

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
