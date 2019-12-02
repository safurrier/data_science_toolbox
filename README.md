# data_science_toolbox

Various code to aid in data science projects for tasks involving data cleaning,
ETL, EDA, NLP, viz, feature engineering, feature selection, model training and validation etc.

## Installation

### Using pip

You can install from PyPI using the pip package manager by running

    pip install data-science-toolbox

You can install the latest version by cloning this repo and installing from src

    git clone https://github.com/safurrier/data_science_toolbox

    cd data_science_toolbox    

    pip install .    

## Project Organization

---------------------
    ├── README.md              
    ├── data_science_toolbox   <- Project source code
    │   │
    │   ├── gists              <- Code gists with commonly used code (change to root
    │   │                         directory, connect to database, profile data, etc)
    │   ├── data_checks        <- Code for data checks and assertions
    │   ├── io                 <- Code for input/output utilities
    │   ├── etl                <- For building reproducible ETL pipelines, including data
    │   │                         checks and transformers
    │   ├── ml                 <- Machine Learning utility code (feature engineering, etc) 
    │   ├── pandas             <- Pandas related utility code
    │   │   ├── analysis                  
    │   │   ├── cleaning
    │   │   ├── engineering
    │   │   ├── text    
    │   │   ├── datetime     
    │   │   ├── optimization       
    │   │   └── profiling   
    │   ├── project_utils.py   <- For project specific utilities
    │   │
    │   ├── text               <- Code for dealing with text. Includes distributed loading of text corpus, 
    │   │                         entity statement extraction, sentiment analysis, pii removal etc.
    │   └── __init__.py        <- Makes data_science_toolbox a Python module               
    ├── tests                  <- Pytest unit tests 
    ├── dist                   <- tars and whls of version builds
    ├── LICENSE
    ├── poetry.lock
    └── pyproject.toml 