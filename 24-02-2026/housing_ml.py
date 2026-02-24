import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix

df = pd.read_csv("Housing.csv")
print("dataset loaded")
print("shape",df.shape)

print("--"*70)
print("\nfirst 5 row")
print(df.head())

print("--"*70)
print("\nInfo")
print(df.info())

print("--"*70)
print("\nMissing Values:-")
print(df.isnull().sum())


# Data_Preprocessing
print("--"*70)
df =pd.get_dummies(df,drop_first=True)
X = df.drop("price",axis=1)
y= df["price"]


# Statistical Summary
print("--"*70)
print("Statistical Summary:-")
print(df.describe())


#Boxplot
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.title("Box Plot of prices")
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)


# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# Distribution of Target Value
plt.figure(figsize=(8,5))
sns.histplot(y,bins=30,kde=True)
plt.title("Distribution of house price")
plt.show()


# DecisionTreeRegressor
dt_model = DecisionTreeRegressor(max_depth=5,random_state=42)
dt_model.fit(X_train,y_train)

y_pred= dt_model.predict(X_test)


#Model Evaluation
# mse = mean_squared_error(y_test,y_pred)
# rmse = np.sqrt(mean_squared_error(y_test,y_pred))
# mae = mean_absolute_error(y_test,y_pred)
# accuracy= r2_score(y_test,y_pred)
# print("Mean Squared Error:",mse)
# print("Root Mean Squared Error:",rmse)
# print("Mean Absolute Error:",mae)
# print("Accuracy:",accuracy)


#Model Evaluation
r2=r2_score(y_test,y_pred)
print("R2 Score:",r2)
accuracy =dt_model.score(X_test,y_test)
print("Accuracy:",accuracy)


# cm = confusion_matrix(y_test,y_pred)
# print("Confusion Matrix:")
# print(cm)


# Visualize Decision Tree
plt.figure(figsize=(16,8))
plot_tree(dt_model,feature_names=X.columns,filled=True,max_depth=2)
plt.show()



