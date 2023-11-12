# MSTGCN-AL
Graph Neural Network

## Introduction
This paper investigates attention-based multi-map traffic prediction. Our model, named MSTGCN+AL, utilizes multi-graph representation to capture node information and innovatively combines adaptive adjacency graph and cycle graph to depict node relationships. This solves the problems of insufficient summation of node neighborhood information and insufficient extraction of initial adjacency matrix information. In addition, we introduce a multi-graph fusion module based on attention mechanism to summarize the information of multiple graphs and improve the ability of the model to represent the spatio-temporal features of the traffic network. Extensive experiments are conducted on the Los Angeles Metro dataset to demonstrate that the proposed MSTGCN+AL model outperforms the baseline approach in terms of predictive performance.

## Datasets
The METR-LA dataset obtained from the Los Angeles Metropolitan Transportation Authority contains average traffic speed values measured by 207 loop detectors on the highways of Los Angeles County ranging from March 2012 to June 2012.

## Requirements

Our code is based on Python3 (>= 3.6). The major libraries are listed as follows:
- torch >= 1.8.1
- numpy >= 1.15
- scipy >= 1.1.0
- torch-cluster >= 1.5.9
- torch-geometric >= 1.7.2
- torch-scatter >= 2.0.6
- torch-sparse >= 0.6.9
- torch-spline-conv >= 1.2.1
- pytorch-lightning >= 1.2.8
- wandb >= 0.11.1
