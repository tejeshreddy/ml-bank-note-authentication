# Bank Note Authentication


##  Contents
- Introduction
- Dataset Discription
    - Tabular View of the Data
- Technology Stack
- Intallation


## Introduction
This machine learning algorithm takes into consideration several features of a bank note like variance, skewness,curtosis and entropy to determine if the note is either genuine or forged

The dataset is available on the UCI website and can also be found on [kaggle](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data) 

Dataset can be used for binary classification, where there are two classes 0 and 1

## Dataset Discription
Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

### Tabular View of the Data

variance | skewness | curtosis | entropy | class
-- | -- | -- | -- | -- | --
3.6216 | 8.6661 | -2.8073 | -0.44699 | 0
4.5459 | 8.1674 | -2.4586 | -1.4621 | 0 
3.866 | -2.6383 | 1.9242 | 0.10645 | 0
.. | .. | .. | .. | .. |


## Folder Structure

```text
ml-bank-note-authentication
 ┣ data
 ┃ ┣ bank_note_authentication.csv
 ┃ ┗ test_file.csv
 ┣ .gitignore
 ┣ Dockerfile
 ┣ LICENSE
 ┣ README.md
 ┣ app.py
 ┣ flasgger_app.py
 ┣ joblib_model.sav
 ┣ model_training.ipynb
 ┣ pickle_model.pkl
 ┣ requirements.txt
 ┗ streamit_app.py
```

## Technology Stack
<p>
<a href="https://www.docker.com/">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/>
</a>
<a href="https://flask.palletsprojects.com/en/1.1.x/">
<img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/>
</a>
<img src="https://raw.githubusercontent.com/vscode-icons/vscode-icons/master/icons/file_type_swagger.svg" alt="swagger" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/scikit-learn/scikit-learn.png" alt="sklearn" width="40" height="40">
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/master/icons/streamlit.svg" alt="streamlit" width="40" height="40">
<img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="streamlit" width="40" height="40">
<img src="https://raw.githubusercontent.com/simple-icons/simple-icons/master/icons/fastapi.svg" alt="fastapi" width="40" height="40">
</p>

## Installation
This repository shows 3 different web microframework based technologies to get the app up and running. They are using flask, flasgger and streamlit

We will be looking at how we can run these apps using both local setup (virtual environment) and docker

There are individual scripts for running the app using each of the packages

- [Flask](app.py)
- [Flasgger](flasgger_app.py)
- [Streamlit](streamlit_app.py)


### Flask and Flasgger

Change the name of the app file accordingly during the run

**Local setup**
```bash
python3 -m venv env # To create a virtual environment, env

source env/bin/activate # To activate the environment

pip3 install -r requirements.txt # To install all the required packages

python3 app.py # To get the app up and running
```

**Docker**
Check if the contents of the docker file are as below

```docker
FROM python:3.8-slim-buster
COPY . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
CMD python app.py
```
And, use the below commands to build and run the docker image

```bash
docker build -t money_auth .    # To build the docker

docker run -p 5000:5000 money_auth    # To run the docker file

docker run -it money_auth sh    # To run in interactive shell mode

```
To view the app while running the `app.py`, access http://localhost:5000/


To view the app while running the `flasgger_app.py`, access http://localhost:5000/apidocs/

<!-- ### Streamlit -->

