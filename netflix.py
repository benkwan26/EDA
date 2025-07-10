import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    # Load and Clean
    df = pd.read_csv("data/Netflix Userbase.csv")

    # Group By
    print(df.groupby("Subscription Type")["Monthly Revenue"].mean())
    print(df.groupby("Country")["User ID"].count())
    print(df.groupby("Plan Duration")["Age"].median())
    print(df.groupby("Gender")["Monthly Revenue"].sum())
    print(df.groupby("Device")["Age"].mean())

    # Scatter Plot
    sns.scatterplot(data=df, x="Age", y="Monthly Revenue", hue="Gender")
    plot(title="Age vs. Monthly Revenue", xlabel="Age", ylabel="Monthly Revenue")

    # Bar Chart
    sns.barplot(data=df.groupby("Country")["Monthly Revenue"].mean().reset_index(), x="Country", y="Monthly Revenue")
    plt.xticks(rotation=90)
    plot(title="Average Monthly Revenue by Country", xlabel="Country", ylabel="Average Monthly Revenue")

    # Pair Plot
    sns.pairplot(df[["Monthly Revenue", "Age"]], diag_kind="kde")
    plt.suptitle("Monthly Revenue and Age", y=1.02)
    plot()

    # Count Plot
    sns.countplot(data=df, x="Subscription Type")
    plt.xticks(rotation=45)
    plot(title="Subscription Type Distribution", xlabel="Subscription Type", ylabel="Count")

    sns.countplot(data=df, x="Device")
    plt.xticks(rotation=45)
    plot(title="Device Distribution", xlabel="Device", ylabel="Count")

    # Histogram
    sns.histplot(df["Monthly Revenue"], bins=10, kde=True)
    plot(title="Monthly Revenue Distribution", xlabel="Monthly Revenue", ylabel="Count")

    sns.histplot(df["Age"], bins=5, kde=True)
    plot(title="Age Distribution", xlabel="Age", ylabel="Count")