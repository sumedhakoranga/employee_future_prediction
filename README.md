# Employee Future Prediction

## Description

The [dataset](https://www.kaggle.com/tejashvi14/employee-future-prediction) consists of dummy employee details of a company. It includes employees' education details, joining year, city of office, payment tier, age, gender, if the employee is ever kept out of projects for 1 month or more and experience in current field. The task is to predict whether the employee will leave the company in the next 2 years.

For the project, first I have done [EDA](https://github.com/sumedhakoranga/employee_future_prediction/blob/main/eda.ipynb) and [feature selection](https://github.com/sumedhakoranga/employee_future_prediction/blob/main/feature_selection.ipynb). Then, I have trained three models: [LogisticRegression](https://github.com/sumedhakoranga/employee_future_prediction/blob/main/logistic_regression.ipynb), [RandomForestClassifier](https://github.com/sumedhakoranga/employee_future_prediction/blob/main/random_forest.ipynb) and [XGBClassifier](https://github.com/sumedhakoranga/employee_future_prediction/blob/main/xgboost.ipynb).

I have created a [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) for each of these models, such that the data transformation and model training/predictions steps are assembled together.

## Tech Stack and concepts used

- Python
- Scikit-learn
- Machine Learning Pipeline
- Docker
- Streamlit

## Setup

- Clone the project repo and open it.

### Virtual Environment

- Create a virtual environment for the project using

  ```bash
  pipenv shell
  ```

- Install required packages using

  ```bash
  pipenv install
  ```

### Docker Container

- Build the docker image using

  ```bash
  sudo docker build -t employee_future .
  ```

- Run the docker container using

  ```bash
  sudo docker run -p 5000:5000 employee_future
  ```

- Open the URL http://localhost:5000/ to run and test the app.

### Deploying to Cloud

- Open the [Deploy an app](https://share.streamlit.io/deploy) page of Streamlit.
- Enter the GitHub repository details in which the streamlit_app.py file and model binaries are stored.
- Click on Deploy button.
- Open the URL employeefutureprediction.streamlit.app to run and test the app.

## Prediction Results

| Model                  | Validation Set Accuracy | Training+Validation Set Accuracy |
| ---------------------- | ----------------------- | -------------------------------- |
| LogisticRegression     | 81.20 %                 | 80.12 %                          |
| RandomForestClassifier | 85.28 %                 | 89.04 %                          |
| XGBClassifier          | 85.93 %                 | 87.37 %                          |

Selected Model (RandomForestClassifier) Test Set Accuracy = 86.57 %
