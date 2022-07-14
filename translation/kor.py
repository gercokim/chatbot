import tensorflow as tf
import numpy as np
import pandas as pd

# Loading the data
dataset = pd.read_csv("datasets/conversations.csv", sep=",")
dataset = dataset.drop(dataset.columns[[0, 1, 4]], axis=1)
train_dataset = np.array(dataset)
print(train_dataset)