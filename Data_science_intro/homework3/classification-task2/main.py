import time
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from typing import List


def euclidean_distance(x: np.ndarray, y: np.ndarray) -> float:
    """calculate the euclidian distnace between two n-dimensional vectors
    Args:
        x (np.ndarray): first vector
        y (np.ndarray): second vector
    Returns:
        float: euclidean distance between x and y
    """
    return np.sqrt(np.sum((x - y) ** 2))

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

def classify_with_NNR(data_trn: str, data_vld: str, df_tst: DataFrame) -> List:
    #  the data_tst dataframe should only(!) be used for the final predictions your return
    print(f'starting classification with {data_trn}, {data_vld}, predicting on {len(df_tst)} instances')

    predictions = list()  # todo: return a list of your predictions for test instances
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
