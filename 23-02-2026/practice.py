import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, confusion_matrix

df = pd.read_csv("bank_loan.csv")
print("dataset loaded")
print("shape",df.shape)


print("\nfirst 5 row")
print(df.head())

print("\nInfo")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# performing EDA
sns.countplot(x ='Loan_Status', data=df)
plt.title('Loan Distribution')
plt.show()


# numerical distribution
df.hist(figsize=(12,10))
plt.show()


# sns.scatterplot(
#     x="ApplicantIncome",
#     y="LoanAmount",
#     data=df
# )
# plt.show()


# correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True))
plt.title("Correlation Heatmap")
plt.show()


# Data preprocessing
df.drop("Loan_ID",axis=1,inplace=True)

# Handle Missing Values
categorical_cols = df.select_dtypes(include="object").columns
print(categorical_cols)
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0],inplace=True)

# cat_cols=["Gender","Married","Dependents","Self_Employed","Property_Area"]
# for col in cat_cols:
#     df[col].fillna(df[col].mode()[0],inplace=True)
#
# num_cols=["LoanAmount","Loan_Amount_Term","Credit_History"]
# for col in num_cols:
#     df[col].fillna(df[col].median(),inplace=True)


numerical_cols= df.select_dtypes(include=np.number).columns
print(numerical_cols)
for col in numerical_cols:
    df[col].fillna(df[col].median(),inplace=True)
print(df.isnull().sum())


le = LabelEncoder()
for col in categorical_cols:
    df[col]=le.fit_transform(df[col])


num_cols= df.select_dtypes('int64','float64').columns
for col in num_cols:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title("box plot")
    plt.show()


X=df.drop("Loan_Status",axis=1)
y=df["Loan_Status"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)
print("R2 score:",r2_score(y_test,y_pred))
print("MSE:",mean_squared_error(y_test,y_pred))


log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train,y_train)
y_pred = log_reg.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred))


# Confusion Matrix
cm= confusion_matrix(y_test,y_pred)
print("Confusion Matrix:")
print(cm)


sns.heatmap(cm,annot=True,fmt="g")
plt.title('Confusion Matrix')
plt.show()


