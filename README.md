# Lectoria

_Lectoria es una aplicación que le permite a tu empresa superar los procesos manuales ofreciendo
la extración y el análisis de documentos escaneados de manera automática._

## Comenzando 🚀.

¿Cómo funciona?

Lectoría le permite al usuario ingresar imágenes dentro de la aplicación, dentro de ésta se procesan y se extrae la información requerida por el usuario. 

En este proyecto estamos extrayendo 12 cuentas de los Estados Financieros


| Balance General   | Estado de pérdidas y ganancias | General            |  
|-------------------|--------------------------------|--------------------|
| *Caja y efectivo  | *Ventas                        | *Fecha              |   
| *Total Pasivo     | *Costo de Ventas               | *Unidades de medida |   
| *Total Patrimonio | *Utilidad Bruta                |                    |   
|                   | *Utilidad operacional          |                    |   
|                   | *Utilidad antes de impuestos   |                    |   
|                   | *Utilidad neta                 |                    |  





Después de extraer la información, se genera un archivo .csv y adicional dentro de la misma aplicación puedes acceder a un dashboard dinámico que contiene analíticos generados
con la información de los archivos ingresados por el usuario



![title](src/static/images/diagrama.png)


------------





## Construido con 🛠️

_Las herramientas utilizadas son las siguientes_

* [Amazon Textract](https://aws.amazon.com/es/textract/) 
* [AWS S3](https://aws.amazon.com/es/s3/) 
* [Streamlit](https://www.streamlit.io/) 

## Contribuyendo 🖇️

Este proyecto es parte de la competencia de programación global creada por BBVA 



[![IMAGE ALT TEXT](src/static/images/hackaton.JPG)](https://www.youtube.com/watch?v=G7ykOxP2Glg&feature=emb_title "Hackaton BBVA")



    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
