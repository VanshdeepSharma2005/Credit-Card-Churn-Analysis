import pandas as pd
df=pd.read_csv("BankChurners.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df=df.drop(columns=[
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2" ])
print(df.columns)

df = df.rename(columns={
    "CLIENTNUM": "Customer_ID",
    "Attrition_Flag": "Customer_Status",
    "Customer_Age": "Age",
    "Dependent_count": "Dependents",
    "Months_on_book": "Relationship_Months",
    "Total_Relationship_Count": "Products_Held",
    "Months_Inactive_12_mon": "Inactive_Months",
    "Contacts_Count_12_mon": "Contact_Count",
    "Credit_Limit": "Credit_Limit",
    "Total_Revolving_Bal": "Revolving_Balance",
    "Avg_Open_To_Buy": "Available_Credit",
    "Total_Amt_Chng_Q4_Q1": "Amount_Change_Ratio",
    "Total_Trans_Amt": "Total_Transaction_Amount",
    "Total_Trans_Ct": "Total_Transaction_Count",
    "Total_Ct_Chng_Q4_Q1": "Transaction_Count_Change",
    "Avg_Utilization_Ratio": "Credit_Utilization"
})
print(df.columns)

df = df[[
    "Customer_ID",
    "Customer_Status",
    "Age",
    "Gender",
    "Dependents",
    "Income_Category",
    "Card_Category",
    "Relationship_Months",
    "Inactive_Months",
    "Contact_Count",
    "Credit_Limit",
    "Revolving_Balance",
    "Available_Credit",
    "Total_Transaction_Amount",
    "Total_Transaction_Count",
    "Credit_Utilization"
]]

df.to_csv("Cleaned_Bank_Churners.csv", index=False)