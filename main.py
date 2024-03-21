#COMP661 at SDCCE Hackathon Project
#Author: Belinda Zhu
#Neural Network Predicting Breast Cancer from mRNA Expression

import sys

sys.path.append("the path")
import matplotlib.pyplot as plt

#Data Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

#preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

#Classification
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
