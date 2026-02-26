import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score


class RandomForestRegression:
    def __init__(self, file_name, test_size=0.333, random_state=42):
        self.file_name = file_name
        self.test_size = test_size
        self.random_state = random_state
        self.data = None
        self.model = None
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None


    # Load The Dateset
    def load_data(self):
        self.df = pd.read_csv(self.file_name)
        print("Dataset loaded:-")
        print("--" * 70)
        print("Shape of Dataset:-")
        print(self.df.shape)
        print("--" * 70)
        print("Top 5 rows:-")
        print("--" * 70)
        print(self.df.head())
        print("--" * 70)
        print(self.df.describe())
        print("--" * 70)

    # Preprocessing
    def preprocess(self):
        print("--" * 70)
        print("\nMissing Values:-")
        print("--" * 70)
        print(self.df.isnull().sum())
        label_encoder = LabelEncoder()
        categorical_columns=self.df.select_dtypes(include=['object']).columns

        for col in categorical_columns:
                self.df[col]=label_encoder.fit_transform(self.df[col])
        print("--" * 70)
        print("Preprocessing Completed:-")
        print("--" * 70)
        print(self.df.head())

    # EDA
    def perform_eda(self):

        plt.figure()
        plt.boxplot(self.df['PriceEuro'])
        plt.title("Box Plot of PriceEuro")
        plt.xlabel("PriceEuro")
        plt.ylabel("Frequency")
        plt.show()

        plt.figure(figsize=(10, 8))
        sns.heatmap(self.df.corr(), annot=True, fmt=".1f", cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()


    def split_data(self):
        X=self.df.drop('PriceEuro',axis=1)
        y=self.df['PriceEuro']
        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(X,y,test_size=0.2,random_state=42)
        print("Data split Completed")
        print("Training Dataset",self.X_train.shape)
        print("Testing Dataset",self.X_test.shape)


    def train_model(self):
        self.model = RandomForestRegressor(n_estimators=50,random_state=42)
        self.model.fit(self.X_train,self.y_train)
        print("Model Training Completed")


    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        r2=r2_score(self.y_test,y_pred)
        mae=mean_squared_error(self.y_test,y_pred)
        rmse=mean_squared_error(self.y_test,y_pred)
        print("\nmodel Evaluation Completed")
        print("Accuracy(R2 Score):",r2)
        print("Mean Absolute Error:",mae)
        print("Root Mean Squared Error:",rmse)


if __name__ == "__main__":
    rfr= RandomForestRegression("ElectricCarDataset.csv")
    rfr.load_data()
    rfr.preprocess()
    rfr.perform_eda()
    rfr.split_data()
    rfr.train_model()
    rfr.evaluate_model()