import numpy as np
import pandas as pd
from numpy import corrcoef
import seaborn as sns
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

data = pd.read_csv('../data/Data/data.csv')
malidataidps = pd.read_csv('../data/Data/malidataidps.csv')

data20 = data[data.reference_year==2020]
