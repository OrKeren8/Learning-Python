import time
import json
import numpy as np
from numpy.linalg import norm
import pickle

from utils import evaluate_clustering_result


def cosine(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))

def load_from_pickle(file):
    with open(file, 'rb') as fin:
        dataset = pickle.load(fin)
    print(type(dataset), len(dataset))
    return dataset


def calc_cluster_centroid(cluster, features):
    if not cluster:
        return None
    centroid = np.zeros_like(features[next(iter(cluster))])
    for img_key in cluster:
        centroid += features[img_key]
    return centroid / len(cluster)


def cluster_data(features_file, min_cluster_size, iterations=10):
    min_similarity = 0.6
    print(f'starting clustering images in file {features_file}')
    cluster2filenames = dict()
    centroids = dict()
    img_features = load_from_pickle(features_file)
    images = dict()
    
    for i in range(iterations):
        for img_key, img in img_features.items():
            max_similarity = 0
            closest_centroid_cluster = None
            for centroid_key, centroid in centroids.items():
                similarity = cosine(img, centroid)
                if similarity > max_similarity and similarity > min_similarity:
                    max_similarity  = similarity
                    closest_centroid_cluster = centroid_key
            if closest_centroid_cluster is not None:
                before_cluster = images.get(img_key, None)
                if before_cluster != closest_centroid_cluster:
                    if before_cluster is not None:
                        cluster2filenames[before_cluster].remove(img_key)
                        centroids[before_cluster] = calc_cluster_centroid(cluster2filenames[before_cluster], img_features)
                        if len(cluster2filenames[before_cluster]) == 0:
                            del cluster2filenames[before_cluster]
                            del centroids[before_cluster]
                    cluster2filenames[closest_centroid_cluster].append(img_key)
                    images[img_key] = closest_centroid_cluster
                    centroids[closest_centroid_cluster] = calc_cluster_centroid(cluster2filenames[closest_centroid_cluster], img_features)
            else:
                max_key = max(centroids.keys(), default=0)
                cluster2filenames[max_key + 1] = [img_key]
                centroids[max_key + 1] = img
                images[img_key] = max_key + 1
    cluster2remove = set()
    for cluster in cluster2filenames:
        if len(cluster2filenames[cluster]) < min_cluster_size:
            cluster2remove.add(cluster)
    for cluster in cluster2remove:
        del cluster2filenames[cluster]
        del centroids[cluster]
    return cluster2filenames


if __name__ == '__main__':
    start = time.time()

    with open('config.json', 'r', encoding='utf8') as json_file:
        config = json.load(json_file)

    result = cluster_data(config['features_file'],
                          config['min_cluster_size'],
                          config['max_iterations'])

    evaluation_scores = evaluate_clustering_result(config['labels_file'], result)  # implemented
    
    print(f'total time: {round(time.time()-start, 0)} sec')
