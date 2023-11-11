import matplotlib.pyplot as plt

from util import *
import pandas as pd
import torch
import os
from scipy import optimize

np.set_printoptions(threshold=np.inf)


def euclidean_distance(v_i, v_j):
    return np.sqrt(np.sum(np.square(v_i - v_j)))


def generate_dist_graph(x):

    num_node = x.shape[0]
    # print("x.shape" + x.shape)
    dist_graph = np.zeros((num_node, num_node))
    # print("dist_graph.shape" + dist_graph.shape)

    sigma_D = 100
    varepsilon = 0.1

    for i in range(num_node):
        for j in range(num_node):
            dist_graph[i][j] = np.exp( -((euclidean_distance(x[i], x[j])** 2) / (sigma_D ** 2)))
            if dist_graph[i][j] < varepsilon:
                dist_graph[i][j] = 0
    # print("dist_graph\n" + dist_graph.round(4))
    np.save(save_dir + "dist_graph", dist_graph)


def generate_tempp_graph(features):
    features = np.squeeze(features)
    features = np.array((features.T))
    # print(features)
    # data = features
    corr_matrix = np.corrcoef(features)
    #print(corr_matrix.shape)


    similarity_matrix = np.zeros(corr_matrix.shape)
    for i in range(corr_matrix.shape[0]):
        for j in range(i, corr_matrix.shape[0]):
            if i == j:
                similarity_matrix[i][j] = 1.000
            else:
                similarity_matrix[i][j] = corr_matrix[i][j]
                similarity_matrix[j][i] = corr_matrix[i][j]


    # print(similarity_matrix)
    np.save(save_dir+"similarity_matrix", similarity_matrix)


save_dir = r'./data/graph/four graph/'

pm25_data_dir = pd.read_hdf("data/original_data/metr-la.h5")
df=np.array(pm25_data_dir.T)

generate_dist_graph(df)
generate_tempp_graph(df)