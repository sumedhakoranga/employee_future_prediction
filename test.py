import pickle
import pandas as pd

from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)

    df = pd.read_csv('Employee.csv')

    X = df.drop(['LeaveOrNot'], axis=1)
    y = df['LeaveOrNot']

    X_full_train, X_test, y_full_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    score = model.score(X_test, y_test)

    print('Test set accuracy =', score)
