import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

import pickle

import warnings
warnings.filterwarnings("ignore")


def create_new_pipeline(params):
    numerical_transformer = SimpleImputer(strategy='median')

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoding', OneHotEncoder(drop='first'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('numerical', numerical_transformer, numerical),
            ('categorical', categorical_transformer, categorical)
        ])

    model = RandomForestClassifier(
        n_jobs=-1,
        random_state=42,
        **params
    )

    pipeline = Pipeline(
        steps=[
            ('preprocessing', preprocessor),
            ('model', model)
        ]
    )

    return pipeline


if __name__ == '__main__':
    print('Importing data...')
    df = pd.read_csv('Employee.csv')

    X = df.drop(['LeaveOrNot'], axis=1)
    y = df['LeaveOrNot']

    print('Splitting data...')
    X_full_train, X_test, y_full_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    numerical = ['Age']
    categorical = ['Education', 'JoiningYear', 'City', 'PaymentTier',
                   'Gender', 'EverBenched', 'ExperienceInCurrentDomain']

    params = {'max_features': None,
              'min_samples_split': 10,
              'n_estimators': 62}

    print('Creating pipeline...')
    pipeline = create_new_pipeline(params)

    print('Training model...')
    pipeline.fit(X_full_train, y_full_train)

    print('Saving model')
    with open('model.pickle', 'wb') as f:
        pickle.dump((pipeline), f)
