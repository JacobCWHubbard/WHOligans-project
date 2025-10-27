# WHOligans-project
Developing different machine learning models to predict life expectancy using WHO data

## Team Members
* Amanda
* Ben
* Jacob
* Jonty
* Krish

## Project Structure
* `notebooks/` - Exploratory analysis and model development
* `src/` - Reusable Python modules
* `data/` - Data and Metadata files
* `presentation/` - Presentation notebooks, final_presentation being the main notebook
* `visualisations/` - A selection of visualisations used in our presentation

## Setup Instructions
1. **Navigate to desired location**\
In the terminal head to your chosen location to download the project
2. **Clone the repository**
```bash
   git clone https://github.com/JacobCWHubbard/WHOligans-project.git
   cd WHOligans-project
```
3. **Create and activate a virtual environment**
```bash
   python -m venv venv # replace python with python3 if needed
   
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
```
4. **Ensure you have the requirements**
```bash
   pip install -r requirements.txt
```

### Data Setup
The data file is not tracked by Git. If you want to work with this repo you should:
1. Obtain the dataset from Digital Futures
2. Place the `Life Expectancy Data.csv` file in the `data/` folder and rename to `life_expectancy.csv`

## Models
* Minimal model: A data sensitive model
* Elaborate model: A data insensitive model

## Results
* Best Minimal Model accuracy: [1.41]
* Best Elaborate accuracy: [1.39]
