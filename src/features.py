import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
import statsmodels.api as sm

# Function to split the data
def splitting_data(df, target):
    X = df.drop(columns = [target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=1)
    return X_train, X_test, y_train, y_test

# log transformer
def log_transform(df, name):
    df[name+'_log'] = np.log1p(df[name])
    df.drop(columns = name, inplace=True)

# exp transformer    
def exp_transform(df, name):
    df[name+'_exp'] = np.exp(df[name])
    df.drop(columns = name, inplace=True)


# Function to feature engineer
def feature_engineering(df):

    # Make a copy of the DF
    df_local = df.copy()
    
    # If thinness data exists in the dataframe,
    # Generate an arbitrary metric combining 'thinness' values, placing 2x more emphasis on 10-19 yr olds than 5-9 yr olds
    # in expectation that there are approx. 2x more people in the former category
    if 'Thinness_five_nine_years' in df_local.columns:
        df_local['Thinness_metric'] = (df_local['Thinness_five_nine_years'] + 2 * df_local['Thinness_ten_nineteen_years'])/3
        # Remove the former thinness columns
        df_local.drop(columns=['Thinness_five_nine_years','Thinness_ten_nineteen_years'], inplace=True)
    
    # One-hot encode 'Regions'
    df_local = pd.get_dummies(df_local, columns=['Region'], drop_first=True, prefix='', prefix_sep='', dtype='int')
    df_local = pd.DataFrame(df_local)

    # Convert zero values of 'Alcohol_consumption' to 0.001 to allow logarithmic transformation
    # df_local.loc[df_local['Alcohol_consumption'] < 0.002, 'Alcohol_consumption'] = 0.001

    # Some features have a strong positive skew.
    # Calculate the log of these (if they exist in the dataframe) to better predict countries with very low values.
    # Then drop the original column.
    for feature in ['Under_five_deaths',
                    'Incidents_HIV',
                    'GDP_per_capita',
                    'Population_mln',
                    'Thinness_metric']:
        if feature in df_local.columns:
            log_transform(df_local, feature)

 #   if 'Under_five_deaths' in df_local.columns:
  #      df_local['Under_five_deaths_log'] = np.log1p(df_local['Under_five_deaths'])
   #     df_local.drop(columns='Under_five_deaths', inplace=True)
#    if 'Incidents_HIV' in df_local.columns:
#        df_local['Incidents_HIV_log'] = np.log1p(df_local['Incidents_HIV'])
#        df_local.drop(columns='Incidents_HIV', inplace=True)
#    if 'GDP_per_capita' in df_local.columns:
#        df_local['GDP_per_capita_log'] = np.log1p(df_local['GDP_per_capita'])
#        df_local.drop(columns='GDP_per_capita', inplace=True)
#    if 'Population_mln' in df_local.columns:
#        df_local['Population_mln_log'] = np.log1p(df_local['Population_mln'])
#        df_local.drop(columns='Population_mln', inplace=True)
#    if 'Thinness_metric' in df_local.columns:
#        df_local['Thinness_metric_log'] = np.log1p(df_local['Thinness_metric'])  # Using a slightly different transformation to reduce the impact of outliers
#        df_local.drop(columns='Thinness_metric', inplace=True)
    
    # All four immunisation rate features have a strong negative skew.
    # If they exist in the dataframe, calculate the exponent of these to better predict countries with very high rates of immunisation.

    for feature in ['Hepatitis_B',
                    'Measles',
                    'Polio',
                    'Diphtheria']:
        if feature in df_local.columns:
            exp_transform(df_local, feature)
#    if 'Hepatitis_B' in df_local.columns:
#        df_local['Hepatitis_B_exp'] = np.exp(df_local['Hepatitis_B']/100)
#        df_local.drop(columns='Hepatitis_B', inplace=True)
#    if 'Measles' in df_local.columns:
#        df_local['Measles_exp'] = np.exp(df_local['Measles']/100)
#        df_local.drop(columns='Measles', inplace=True)
#    if 'Polio' in df_local.columns:
#        df_local['Polio_exp'] = np.exp(df_local['Polio']/100)
#        df_local.drop(columns='Polio', inplace=True)
#    if 'Diphtheria' in df_local.columns:
#        df_local['Diphtheria_exp'] = np.exp(df_local['Diphtheria']/100)
#        df_local.drop(columns='Diphtheria', inplace=True)
    
    return df_local

# A scaling function
def scaling(df, scaler = None):

    # Make a copy of the DF
    df_local = df.copy()
    
    # If no scaler provided, create and fit a new one
    if scaler is None:
        scaler = RobustScaler()
        scaler.fit(df_local)

    # Normalise the data; store as a DataFrame
    df_scaled = pd.DataFrame(scaler.transform(df_local), columns = df_local.columns, index=df_local.index)
    
    return df_scaled, scaler # returns scaled data and scaler (so that the same scaling can be used on new data)

def add_constant_column(df):
    return sm.add_constant(df)