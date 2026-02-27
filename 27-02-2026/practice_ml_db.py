import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


class RandomForestRegression:
    def __init__(self, server, database, driver="ODBC+Driver+17+for+SQL+Server"):
        """Initialize database connection and placeholders"""
        connection_string = f"mssql+pyodbc://{server}/{database}?driver={driver}"
        try:
            self.engine = create_engine(connection_string)
            print("Engine created successfully!")
        except Exception as e:
            print(f"Connection Error: {e}")

        self.df = None
        self.model = None
        self.X_train = self.X_test = self.y_train = self.y_test = None

    def load_table(self, table_name):
        """Load full table from SQL Server and store it in self.df"""
        query = f"SELECT * FROM {table_name}"
        self.df = pd.read_sql(query, self.engine)
        print("Dataset loaded from SQL Server.")
        print("-" * 70)
        print(f"Shape of Dataset: {self.df.shape}")
        print("-" * 70)
        print(self.df.head())
        print("-" * 70)
        return self.df

    def load_query(self, query):
        """
        Load custom SQL query
        """
        df = pd.read_sql(text(query), self.engine)
        return df


    def preprocess(self):
        """Clean data and encode categorical variables"""
        print("\nMissing Values:")
        print(self.df.isnull().sum())

        self.df = self.df.dropna()

        # print("\nMissing Values:")
        # print(self.df.isnull().sum())

        label_encoder = LabelEncoder()
        categorical_columns = self.df.select_dtypes(include=['object']).columns

        for col in categorical_columns:
            self.df[col] = label_encoder.fit_transform(self.df[col].astype(str))
        print("\nPreprocessing Completed.")

    def perform_eda(self):
        """Visualize target distribution and correlations"""
        if 'PriceEuro' not in self.df.columns:
            print("Error: 'PriceEuro' column not found for EDA.")
            return

        # Boxplot
        plt.figure()
        plt.boxplot(self.df['PriceEuro'])
        plt.title("Box Plot of PriceEuro")
        plt.xlabel("PriceEuro")
        plt.ylabel("Frequency")
        plt.show()

        # Heatmap
        plt.figure(figsize=(10, 8))
        corr= self.df.corr(numeric_only=True)
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1, center=0)
        plt.title("Correlation Heatmap")
        plt.show()


    def split_data(self):
        """Prepare features and target for training"""
        X = self.df.drop('PriceEuro', axis=1)
        y = self.df['PriceEuro']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        print(f"Data split: Training {self.X_train.shape}, Testing {self.X_test.shape}")

    def train_model(self):
        """Initialize and fit the Random Forest"""
        self.model = RandomForestRegressor(n_estimators=50, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        print("Model Training Completed.")

    def evaluate_model(self):
        """Calculate and print regression metrics"""
        y_pred = self.model.predict(self.X_test)
        r2 = r2_score(self.y_test, y_pred)
        mae = mean_absolute_error(self.y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))

        print("\nModel Evaluation Completed:")
        print(f"Accuracy (R2 Score): {r2:.4f}")
        print(f"Mean Absolute Error: {mae:.4f}")
        print(f"Root Mean Squared Error: {rmse:.4f}")


def main():
    server = "localhost"
    database = "interns"
    #Initialize instance
    loader = RandomForestRegression(server, database)
    #Load data from table (this populates loader.df)
    loader.load_table("ElectricCarDataset")
    #Execute Pipeline using the correct instance name 'loader'
    loader.preprocess()
    loader.perform_eda()
    loader.split_data()
    loader.train_model()
    loader.evaluate_model()


if __name__ == "__main__":
    main()
