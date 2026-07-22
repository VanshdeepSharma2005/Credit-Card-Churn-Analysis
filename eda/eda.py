import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Final_Bank_Churners.csv")

print(df.columns)

print(df.describe())
print(df.describe(include='object'))

# UNIVARIATE ANALYSIS
print(df["Customer_Status"].value_counts())                  
print(df["Gender"].value_counts())
print(df["Income_Category"].value_counts())

# BIVARIATE ANALYSIS
print(pd.crosstab(df["Income_Category"], df["Customer_Status"]))            

print(df["Card_Category"].value_counts())
# CHURN RATE
print(df["Customer_Status"].value_counts(normalize=True) * 100)           


sns.countplot(x="Customer_Status", data=df)
plt.title("Customer Status Distribution")
plt.show()
# Insight: 
# Around 84% of customers are existing customers,
# while about 16% have churned.

print(df["Age"].value_counts())
sns.histplot(df["Age"], bins=20)
plt.title("Customer Age Distribution")
plt.show()
# Insight:
# Most customers belong to the middle-age group,
# indicating the bank mainly serves working professionals.

print(df["Credit_Limit"].value_counts())
sns.boxplot(x=df["Credit_Limit"])
plt.title("Credit Limit Boxplot")
plt.show()
# Insight:
# Some customers have exceptionally high credit limits,
# indicating premium customer segments.

sns.countplot(x="Gender",
              hue="Customer_Status",
              data=df)
plt.title("Gender vs Customer Status")
plt.show()
# Insight:
# Compare the proportion of churned customers between males and females
# to identify whether one group experiences higher churn.

contact_churn = pd.crosstab(
    df["Contact_Count"],
    df["Customer_Status"],
    normalize="index"
) * 100

sns.barplot(
    x=contact_churn.index,
    y=contact_churn["Attrited Customer"]
)

plt.title("Churn Rate by Contact Count")
plt.xlabel("Number of Contacts ")
plt.ylabel("Churn Rate (%)")
plt.show()

income_churn = pd.crosstab(
    df["Income_Category"],
    df["Customer_Status"],
    normalize="index"
) * 100

sns.barplot(
    x=income_churn.index,
    y=income_churn["Attrited Customer"]
)

plt.title("Churn Rate by Income Category")
plt.xlabel("Income Category")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=45)
plt.show()

card_churn = pd.crosstab(
    df["Card_Category"],
    df["Customer_Status"],
    normalize="index"
) * 100

sns.barplot(
    x=card_churn.index,
    y=card_churn["Attrited Customer"]
)

plt.title("Churn Rate by Card Category")
plt.ylabel("Churn Rate (%)")
plt.show()

contact_churn = pd.crosstab(
    df["Contacts_Count_12_mon"],
    df["Customer_Status"],
    normalize="index"
) * 100

sns.barplot(
    x=contact_churn.index,
    y=contact_churn["Attrited Customer"]
)

plt.title("Churn Rate by Contact Count")
plt.ylabel("Churn Rate (%)")
plt.show()
