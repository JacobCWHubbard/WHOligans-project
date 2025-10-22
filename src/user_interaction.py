# Import our libaries
from ipywidgets import widgets
from IPython.display import display, clear_output
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


def model_picker(): # An experiment with ipywidgets
    # Create a dropdown widget
    radio_button = widgets.RadioButtons(
        options = ['Y', 'N'],
        description = "Do you consent to using advanced population" \
    " data, which may include protected information, for better" \
    " accuracy?",
    layout = {'width': 'max-content'}
    )    

    radio_button.style.background = 'lightblue'

    # Create a button
    button = widgets.Button(description="Confirm")

    # Create an output area
    out = widgets.Output()

    # Define what happens on button click
    def on_button_click(b):
        with out:
            clear_output()
            print(f"You chose: {radio_button.value}")
    
    button.on_click(on_button_click)

    display(radio_button, button, out)

    return radio_button.value


# Collect user values
def collect_values(df, response, sensitive_features, non_sensitive_features):
    if response == 'n':
        required_features = sensitive_features
    else:
        required_features = non_sensitive_features
    user_values = {}
    for feature in required_features:
        print(f"Please enter the value for {feature} from the following list {list(df[feature].unique())}: ")
        while True:
            try:
                user_values[feature] = input(f"Enter value for {feature}: ")
                if not valid_feature_input(feature, user_values[feature]):
                    raise Exception
                break
            except:
                print("Sorry, your input is not valid")
    
    print(user_values)

# Check if user input is valid
def valid_feature_input(df, feature, value):
    if feature == 'Region':
        if value in list(df.Region.unique()):
            return True
        else:
            print("Your ")