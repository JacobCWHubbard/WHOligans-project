import sys
from user_interaction import welcome_message, model_decider, collect_values
from preprocessing import load_data 
from models import full_pipeline
from features import feature_engineering, scaling, add_constant_column



def final_function():
    minimal_cols = ['Region',
                'Under_five_deaths',
                'Adult_mortality',
                'GDP_per_capita',
                'Schooling',
                'Economy_status_Developed',
                'Life_expectancy'
                ]

    elaborate_cols = minimal_cols + [
                  'Alcohol_consumption',
                  'Hepatitis_B',
                  'Measles',
                  'BMI',
                  'Polio',
                  'Diphtheria',
                  'Incidents_HIV',
                  'Thinness_ten_nineteen_years',
                  'Thinness_five_nine_years'
                 ]
    welcome_message()
    response = model_decider()
    if response == 'n': # Decide columns in use
        features = minimal_cols
    else:
        features = elaborate_cols
    df = load_data()
    user_values = collect_values(df, response, features) # Get user data

    # Get model and scaler
    pipeline_results = full_pipeline(features) # This is a tuple
    model = pipeline_results[4] # Extract model from results
    scaler = pipeline_results[5] # Extract scaled used on training data
    training_columns = pipeline_results[6]

    # Apply feature engineering on user_values
    user_values_fe = feature_engineering(user_values)

    # Align columns with training data, to ensure we have the same columns (give that we have one hot encoded on less columns)
    user_values_fe = user_values_fe.reindex(
        columns = [col for col in training_columns if col != 'const'],
        fill_value = 0
        )
    
    # Scale and add constant column
    user_values_fe, _ = scaling(user_values_fe, scaler)
    user_values_fe = add_constant_column(user_values_fe)

    user_values_fe = user_values_fe.reindex(columns=training_columns, fill_value =1)

    # Get prediction
    prediction = model.predict(user_values_fe)
    print(f"Predicted life expectancy: {prediction[0]:.1f} years\n")

    return prediction[0]
