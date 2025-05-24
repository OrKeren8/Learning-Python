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
        """Initialize the NearestNeighbor classifier with training data
        Args:
            x_train (DataFrame): training features
            y_train (pd.Series): training labels
        """
        self.x_train = x_train.to_numpy()
        self.y_train = y_train.to_numpy()
        self.x_vld = x_vld.to_numpy()
        self.y_vld = y_vld.to_numpy()
        self.fit_distances = self.pre_calc_distances()

    def pre_calc_distances(self):
        distances = []
        for row in self.x_vld:
            distances.append(self._calc_distances(row))
        return np.array(distances)
    
    def _calc_distances(self, origin: np.ndarray):
        return np.linalg.norm(self.x_train - origin, axis=1)
    
    def _get_nearest_neighbors_class(self, origin: np.ndarray, radius: float, pre_dist_idx: int = -1):
        distances = self.fit_distances[pre_dist_idx] if pre_dist_idx > 0 else self._calc_distances(origin)
        within_radius = distances <= radius
        labels_within = self.y_train[within_radius]
        values, counts = np.unique(labels_within, return_counts=True)
        return values[np.argmax(counts)] if counts.size > 0 else self.y_train[0]
        
    def check_best_radius(self, start: float, end: float, jump) -> float:
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
        """Predict the class of each instance in the data using the nearest neighbor algorithm
        Args:
            data (DataFrame): input data for which to predict the class
            radius (float): radius within which to consider neighbors
        Returns:
            List: list of predicted classes for each instance in the data
        """
        predictions = []
        for i in range(len(np_data)):
            predictions.append(self._get_nearest_neighbors_class(np_data[i], radius, i if from_fit else -1))
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
