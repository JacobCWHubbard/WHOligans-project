import pandas as pd
import numpy as np



def feature_engineering(df, feature_cols):

    # Make a copy of the DF
    df_local = df.copy()
    
    # An arbitrary metric combining 'thinness' values, placing 2x more emphasis on 10-19 yr olds than 5-9 yr olds
    # in expectation that there are approx. 2x more people in the former category
    df_local['Thinness_metric'] = (df_local['Thinness_five_nine_years'] + 2 * df_local['Thinness_ten_nineteen_years'])/3
    
    # Remove the former thinness columns
    df_local.drop(columns=['Thinness_five_nine_years','Thinness_ten_nineteen_years'], axis=0, inplace=True)
    
    # One-hot encode 'Regions'
    df_local = pd.get_dummies(df_local, columns=['Region'], drop_first=True, prefix='', prefix_sep='', dtype='int')
    
    # Some features have a strong positive skew.
    # Calculate the log of these to better predict countries with very low values.
    df_local['Under_five_deaths_log'] = np.log(df_local['Under_five_deaths'])
    df_local['Incidents_HIV_log'] = np.log(df_local['Incidents_HIV'])
    df_local['GDP_per_capita_log'] = np.log(df_local['GDP_per_capita'])
    df_local['Population_mln_log'] = np.log(df_local['Population_mln'])
    df_local['Thinness_metric_log'] = np.log1p(df_local['Thinness_metric'])  # Using a slightly different transformation to reduce the impact of outliers
    
    # All four immunisation rate features have a strong negative skew.
    # Calculate the exponent of these to better predict countries with very high rates of immunisation. 
    df_local['Hepatitis_B_exp'] = np.exp(df_local['Hepatitis_B']/100)
    df_local['Measles_exp'] = np.exp(df_local['Measles']/100)
    df_local['Polio_exp'] = np.exp(df_local['Polio']/100)
    df_local['Diphtheria_exp'] = np.exp(df_local['Diphtheria']/100)
    
    return df_local