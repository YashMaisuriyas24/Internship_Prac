import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score


df = pd.read_csv("insurance.csv")
df.head()

print("shape of dataset",df.shape)
print("columns",df.columns)
df.info()

print(df.info())

print(df.head(5))

df= pd.get_dummies(df,drop_first=True)
df.head()

X = df.drop("charges", axis=1)
y = df["charges"]
print("x shape",X.shape)
print("y shape",y.shape)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTraining size",x_train.shape)
print("\nTesting size",x_test.shape)

model = LinearRegression()
model.fit(x_train, y_train)
print("Model Trained successfully")


y_pred = model.predict(x_test)
print(y_pred[:5])


r2= r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)



print("Model performance")
print("R2 score (Accuracy)",r2)
print("Mean Absolute Error",mae)
print("Mean Squared Error",mse)
print("Root Mean Squared Error",rmse)


comparison = pd.DataFrame({
    "actual": y_test,
    "predicted": y_pred
})
comparison.head(10)


plt.figure(figsize=(8,6))
plt.scatter(y_test,y_pred)
plt.xlabel("actual charges")
plt.ylabel("predicted charges")
plt.title("Actual vs predicted charges")
plt.show()

error = y_test - y_pred
plt.figure(figsize=(8,6))
plt.hist(error, bins=20)
plt.title("error distribution")
plt.xlabel("prediction error")
plt.ylabel("frequency")
plt.show()