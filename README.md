data-science-toolbox
=====================

Various code to aid in data science projects for tasks involving data cleaning,
ETL, EDA, NLP, viz, feature engineering, feature selection, model training and validation etc.

Project Organization

---------------------
    ├── README.md              
    ├── data_science_toolbox   <- Project source code
    │   │
    │   ├── gists                  <- Code gists with commonly used code (change to root
    │   │                             directory, connect to database, profile data, etc)
    │   ├── io                     <- Code for input/output utilities
    │   ├── etl                    <- For building reproducible ETL pipelines, including data
    │   │                             checks and transformers
    │   ├── ml                     <- Machine Learning utility code (feature engineering, etc) 
    │   ├── pandas                 <- Pandas related utility code
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
    ├── tests
    ├── LICENSE
    ├── poetry.lock
    └── pyproject.toml 