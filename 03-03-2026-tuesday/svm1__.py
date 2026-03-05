import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (classification_report,confusion_matrix, accuracy_score)
from sklearn.svm import SVC

class SVMClassifier:
    def __init__(self, file_path, target_column):
        self.file_path = file_path
        self.target_column = target_column
        self.df = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.best_model = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Data Loaded Successfully!")
        print("Shape:", self.df.shape)
        print(self.df.head())

    def perform_eda(self):
        print("-" * 70)
        print("\nMissing Values:\n", self.df.isnull().sum())

        # Target distribution
        plt.figure(figsize=(6,4))
        sns.countplot(x=self.target_column, data=self.df)
        plt.title("Target Class Distribution")
        plt.show()

        # Correlation heatmap
        plt.figure(figsize=(10,8))
        sns.heatmap(self.df.corr(), cmap='coolwarm')
        plt.title("Correlation Matrix")
        plt.show()

    def remove_outliers(self):
        X = self.df.drop(self.target_column, axis=1)
        y = self.df[self.target_column]

        Q1 = X.quantile(0.25)
        Q3 = X.quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        X_clean = X[~((X < lower_bound) | (X > upper_bound)).any(axis=1)]
        y_clean = y[X_clean.index]

        self.X = X_clean
        self.y = y_clean

        print("\nOutliers Removed!")
        print("New Shape:", self.X.shape)

    def split_data(self, test_size=0.2):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=test_size,random_state=42,stratify=self.y)
        print("Data Split Completed!")

    def grid_search_svm(self):

        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('svm', SVC(probability=True))
        ])

        param_grid = {'svm__C': [0.1, 1, 10],'svm__kernel': ['linear', 'rbf'],}

        grid = GridSearchCV(pipeline,param_grid,cv=5,scoring='accuracy',n_jobs=-1)

        grid.fit(self.X_train, self.y_train)

        self.best_model = grid.best_estimator_

        print("Best Parameters (SVM):", grid.best_params_)
        print("Best CV Score:", grid.best_score_)

    def evaluate_model(self):

        y_pred = self.best_model.predict(self.X_test)

        print("\nTest Accuracy:", accuracy_score(self.y_test, y_pred))
        print("\nClassification Report:\n")
        print(classification_report(self.y_test, y_pred))

        cm = confusion_matrix(self.y_test, y_pred)
        plt.figure(figsize=(5,4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")
        plt.show()

if __name__ == "__main__":
    svm = SVMClassifier(file_path="pulsar_stars.csv",target_column="target_class")
    svm.load_data()
    svm.perform_eda()
    svm.remove_outliers()
    svm.split_data()
    svm.grid_search_svm()
    svm.evaluate_model()