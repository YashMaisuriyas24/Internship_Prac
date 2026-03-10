import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler


class  UnsupervisedMl:
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
        self.models = {}
        self.scaled_data = None
        self.k_means = None


    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Data Loaded Successfully!")
        print("Shape:", self.df.shape)
        print(self.df.head())

    def preprocess(self):
        print("\nMissing Values:\n", self.df.isnull().sum())
        print("\nPreprocessing data:-")
        if "customerID" in self.df.columns:
            self.df.drop("customerID", axis=1, inplace=True)

        le=LabelEncoder()
        self.df["Gender"] = le.fit_transform(self.df["Gender"])
        print("\nPreprocess complete")
        print(self.df.head())

    def perform_eda(self):
        print("-" * 80)
        print("\nPerforming EDA")
        print("-" * 80)
        plt.figure(figsize=(8,6))
        sns.heatmap(self.df.corr(),annot=True,cmap="coolwarm")
        plt.title("correlation heatmap")
        plt.show()


        # plt.figure(figsize=(10, 6))
        # cols_to_plot = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
        # sns.boxplot(data=self.df[cols_to_plot])
        # plt.title("BoxPlots of Age, Income, and Spending Score")
        # plt.show()


        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.df["Age"], y=self.df["Spending Score (1-100)"])
        plt.title("Age Vs Spending Score")
        plt.show()

    def scale_feature(self):
        print("-" * 80)
        print("\nScaling features")
        print("-" * 80)
        scaler = StandardScaler()
        self.scaled_data = scaler.fit_transform(self.df)
        print("-" * 80)
        print("\nScaling complete")
        print("-" * 80)

    def elbow_method(self):
        print("Finding Optimal Clusters...")
        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, random_state=42)
            kmeans.fit(self.scaled_data)
            wcss.append(kmeans.inertia_)
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, 11), wcss, marker='o')
        plt.title("Elbow Method")
        plt.xlabel("Number of clusters")
        plt.ylabel("WCSS")
        plt.show()


if __name__ == "__main__":
       model = UnsupervisedMl("Mall_Customers.csv",target_column="CustomerID")
       model.load_data()
       model.preprocess()
       model.perform_eda()
       model.scale_feature()
       model.elbow_method()
