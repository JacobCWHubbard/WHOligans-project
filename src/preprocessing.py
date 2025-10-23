# Import libaries
import pandas as pd

# Load the data
def load_data():
    df = pd.read_csv('../data/life_expectancy.csv')
    return df
