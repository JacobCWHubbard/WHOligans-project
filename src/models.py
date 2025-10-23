import statsmodels.api as sm
import statsmodels.tools

# Train model
def train_model(y, X):
    lin_reg = sm.OLS(y, X)
    results = lin_reg.fit()
    return results