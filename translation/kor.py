import tensorflow as tf
import numpy as np
import pandas as pd
import string
import re

# Loading the data
dataset = pd.read_csv("datasets/conversations.csv", sep=",")
dataset = dataset.drop(dataset.columns[[0, 1, 4]], axis=1)

# Splitting data into training and testing data
train_dataset = dataset.sample(frac=0.8, random_state=25)
test_dataset = dataset.drop(train_dataset.index)

train_dataset, test_dataset = np.array(train_dataset), np.array(test_dataset)
#np.array(dataset)
print(train_dataset.shape[0])
print(test_dataset[0][0])

# Parsing the data
for data in train_dataset:
    data[0] = "[start] " + data[0] + " [end]"

for data in test_dataset:
    data[0] = "[start] " + data[0] + " [end]"

# Vectorizing the data

# Stripping punctuation characters
strip_chars = string.punctuation
strip_chars = strip_chars.replace("[", "")
strip_chars = strip_chars.replace("]", "")

VOCAB_SIZE = 5000
SEQUENCE_LENGTH = 50

# Standardizes all input data strings
def standardization(input_string):
    lowercase = tf.strings.lowercase(input_string)
    return tf.string.regex_replace(lowercase, "[%s]" % re.escape(strip_chars), "")

# Creating vectorization layers for eng and kor data
english_vector = tf.keras.layers.TextVectorization(
    max_tokens=VOCAB_SIZE,
    output_mode="int",
    output_sequence_length=SEQUENCE_LENGTH
)

korean_vector = tf.keras.layers.TextVectorization(
    max_tokens=VOCAB_SIZE,
    output_mode="int",
    output_sequence_length=SEQUENCE_LENGTH+1,
    standardize=standardization
)
eng_vocab = [data[1] for data in train_dataset]
kor_vocab = [data[0] for data in train_dataset]
print(eng_vocab)



train_dataset = tf.data.Dataset.from_tensor_slices(np.array(train_dataset))
test_dataset = tf.data.Dataset.from_tensor_slices(np.array(test_dataset))

# Shuffling and batching the data
BATCH_SIZE = 64
SHUFFLE_BUFFER_SIZE = 100

train_dataset = train_dataset.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
test_dataset = test_dataset.batch(BATCH_SIZE)


# Text tokenization and detokenization
