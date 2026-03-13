import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt


class GroceryAlgorithm:
    def __init__(self):
        self.df = None
        self.df_encoded = None
        self.basket = None
        self.transactions = None
        self.encoder = TransactionEncoder()
        self.algo = None
        self.rules = None

    def load_data(self):
        self.df = pd.read_csv("Groceries_dataset.csv")
        print("Data Loaded Successfully!")
        print("Shape:", self.df.shape)
        print(self.df.head())
        print(self.df.isnull().sum())


    def group_items(self):
        self.load_data()
        self.basket = self.df.groupby(["Member_number", "Date"])["itemDescription"].apply(list).reset_index()
        self.transactions = self.basket["itemDescription"].tolist()


    def feature_encoding(self):
        self.group_items()
        encoder_array = self.encoder.fit_transform(self.transactions)
        self.df_encoded = pd.DataFrame(encoder_array, columns=self.encoder.columns_)
        print("Feature encoding successful")


    def run_algorithm(self):
        self.feature_encoding()
        self.algo = apriori(self.df_encoded,min_support=0.01,use_colnames=True)
        print(f"Total Frequent Item-sets = {self.algo.shape[0]}\n")
        print("Model Training Completed")

    def generate_association_rules(self):
        self.run_algorithm()
        rules_df = association_rules(self.algo, metric="confidence",min_threshold=0.1)
        if rules_df is None or rules_df.empty:
            print("No association rules were generated.")
            return
        self.rules = rules_df[
            rules_df['antecedents'].apply(lambda x: len(x) >= 1) &
            rules_df['consequents'].apply(lambda x: len(x) >= 1)]
        print("Association Rules:", self.rules.shape[0])
        print(self.rules[['antecedents','consequents','support','confidence','lift']].head(5))

    def visualize(self):
        self.generate_association_rules()
        top_items = self.df['itemDescription'].value_counts().head(10)
        top_items.plot(kind='bar', title='Top 10 Most Purchased Items',color="maroon")
        plt.xlabel("Item")
        plt.ylabel("Count")
        plt.show()

def main():
    apriori = GroceryAlgorithm()
    apriori.visualize()


if __name__ == "__main__":
    main()


