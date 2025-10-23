# Import our libaries
#from ipywidgets import widgets
#from IPython.display import display, clear_output
import pandas as pd
from functools import partial
print = partial(print, flush=True)

# Welcome message
def welcome_message():
    print("Welcome to the WHOligans life expectancy predictor\n")
    return None


# Model Decider
def model_decider():
    print("Do you consent to using advanced population" \
    " data, \nwhich may include protected information, for better" \
    " accuracy? (Y/N): ")
    response = input()
    while True:
        try:
            if response.lower() == "y":
                break
            elif response.lower() == "n":
                break
            else:
                raise Exception
        except:
            print("Please enter either Y or N")
            response = input("Please enter either Y or N: ")
    print(f"Thank you, your response was: {response} \n")
    return response.lower()


#def model_picker(): # An experiment with ipywidgets
#    # Create a dropdown widget
#    radio_button = widgets.RadioButtons(
#        options = ['Y', 'N'],
#        description = "Do you consent to using advanced population" \
#    " data, which may include protected information, for better" \
#    " accuracy?",
#    layout = {'width': 'max-content'}
#    )    
#
#    radio_button.style.background = 'lightblue'
#
#    # Create a button
#    button = widgets.Button(description="Confirm")
#
#    # Create an output area
#    out = widgets.Output()
#
#    # Define what happens on button click
#    def on_button_click(b):
#        with out:
#            clear_output()
#            print(f"You chose: {radio_button.value}")
#    
#    button.on_click(on_button_click)
#
#    display(radio_button, button, out)
#
#    return radio_button.value


# Collect user values
def collect_values(df, response, sensitive_features, non_sensitive_features):
    if response == 'n':
        required_features = sensitive_features
    else:
        required_features = non_sensitive_features
    user_values = {}
    for feature in required_features:
        print(f"Please enter the value for {feature}. {expected_input(df,feature)}")
        while True:
            try:
                user_values[feature] = input(f"Enter value for {feature}: ")
                if not valid_feature_input(df, feature, user_values[feature], user_values):
                    print("Raising exception")
                    raise Exception
                else:
                    break
            except:
                print("\nPlease insure your input is an accepted value")
    
    return user_values

# Explain excepted inputs
def expected_input(df, feature):
    if feature == 'Region':
        return f"Pick from the following list {list(df.Region.unique())}"
    elif feature == 'Economy_status_Developed':
        return "Enter 1 for yes, and 0 for no"
    else:
        return "Please enter a number"

# Check if user input is valid
def valid_feature_input(df, feature, value, user_values):
    if feature == 'Region':
        return valid_region(df, value)
    elif feature == 'Economy_status_Developed':
        user_values[feature] = int(value)
        return valid_economy_status(user_values[feature])
    else:
        user_values[feature] = float(value)
        return valid_num(df, feature, user_values[feature])


# Check if region is valid
def valid_region(df, value):
    if value in list(df.Region.unique()):
        return True
    else:
        print("Your input is not one of the accepted regions, please re-enter your region")

# Check if bool input is valid
def valid_economy_status(value):
    return value in [0,1]

#Check if numerical input is in accepted range
def valid_num(df, feature, value):
    if value > float(df[feature].min()) and value < float(df[feature].max()):
        return True
    else:
        print("Your value is out of the expected range. Please enter Y to confirm or Q to re-enter your value")
        confirmation = input("Y to confirm, q to re-enter")
        if confirmation.lower() == 'y':
            return True
        else:
            return False