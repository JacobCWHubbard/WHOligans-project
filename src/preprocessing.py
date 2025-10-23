# Import libaries
import pandas as pd

# Load the data
def load_data():
    df = pd.read_csv('../data/life_expectancy.csv')
    return df

# Select features
def select_features(response):
    if response == 'y':
        None