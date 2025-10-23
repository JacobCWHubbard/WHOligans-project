import statsmodels.api as sm
import statsmodels.tools
from features import *
from preprocessing import load_data

# Train model
def train_model(y, X):
    lin_reg = sm.OLS(y, X)
    results = lin_reg.fit()
    return results

def full_pipeline(features):
    df_local = load_data()[features]
    X_train, X_test, y_train, y_test = splitting_data(df_local, 'Life_expectancy')
    X_train_fe = feature_engineering(X_train)
    X_train_fe = scaling(X_train_fe)
    X_train_fe = add_constant_column(X_train_fe)
    X_test_fe = feature_engineering(X_test)
    X_test_fe = scaling(X_test_fe)
    X_test_fe = add_constant_column(X_test_fe)
    results = train_model(y_train, X_train_fe)
    return X_train_fe, X_test_fe, y_train, y_test, results

# Calculate RMSE
def calculate_rmse(actual, prediction):
    return statsmodels.tools.eval_measures.rmse(actual, prediction)