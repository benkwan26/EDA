import pandas as pd
import matplotlib.pyplot as plt

def plot(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    # Load and Clean
    df = pd.read_csv("data/shopping_trends.csv")

    # Histogram
    df["Age"].plot(kind="hist")
    plot(title="Age Histogram", xlabel="Age", ylabel="Count")

    df["Purchase Amount (USD)"].plot(kind="hist", bins=10)
    plt.xticks(rotation=90)
    plot(title="Histogram of Purchase Amount Distribution", xlabel="USD", ylabel="Frequency")

    # Bar Chart
    df["Gender"].value_counts().plot(kind="bar")
    plot(title="Gender Distribution", xlabel="Gender", ylabel="Count")

    df["Color"].value_counts().sort_values(ascending=False).head().plot(kind="bar")
    plot(title="Colour Distribution", xlabel="Colour", ylabel="Count")

    df["Season"].value_counts().plot(kind="bar")
    plot(title="Count of Purchases in Each Season", xlabel="Season", ylabel="Count")

    df.groupby("Color")["Review Rating"].mean().head().plot(kind="bar")
    plot(title="Mean Review Rating for Each Color", xlabel="Color", ylabel="Mean Review Rating")

    # Pie Chart
    df["Subscription Status"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plot(title="Subscription Distribution", xlabel="", ylabel="")

    df["Category"].value_counts().plot(kind="pie")
    plot(title="Distirbution of Purchases by Category", xlabel="", ylabel="")

    df.groupby("Payment Method")["Purchase Amount (USD)"].sum().plot(kind="pie")
    plot(title="Sum of Purchase Amount by Payment Method", xlabel="", ylabel="")

    df.groupby("Season")["Purchase Amount (USD)"].sum().plot(kind="pie")
    plot(title="Sum of Purchase Amount by Season", xlabel="Season", ylabel="Sum of Purchase Amount (USD)")

    # Scatter Plot
    df.plot(x="Previous Purchases", y="Review Rating", kind="scatter")
    plot(title="Previous Purchases Review Rating", xlabel="Count", ylabel="Rating")

    # Box Plot
    df.boxplot(column="Purchase Amount (USD)", by="Frequency of Purchases")
    plt.xticks(rotation=90)
    plot(title="Purchase Amount Based on Frequency of Purchase", xlabel="", ylabel="")

    df.boxplot(column="Review Rating", by="Gender")
    plot(title="Review Rating Distribution by Gender", xlabel="Gender", ylabel="Review Rating")
    
    df.boxplot(column="Purchase Amount (USD)", by="Frequency of Purchases")
    plt.xticks(rotation=90)
    plot(title="Purchase Amount Distribution by Frequency of Purchases", xlabel="Frequency of Purchases", ylabel="Purchase Amount (USD)")

    # Group By
    print(df.groupby("Season")["Purchase Amount (USD)"].sum())
    print(df.groupby("Category")["Purchase Amount (USD)"].mean().sort_values(ascending=False))
    print(df.sort_values("Review Rating", ascending=False))
    print(df["Preferred Payment Method"].value_counts())
    print(pd.pivot_table(df, values="Purchase Amount (USD)", index="Location", columns="Item Purchased", aggfunc="mean"))
    print(df.groupby("Size")["Purchase Amount (USD)"].mean())
    print(df.groupby("Payment Method")["Purchase Amount (USD)"].sum())
    print(df.groupby("Discount Applied")["Review Rating"].mean())
    print(df.groupby("Color")["Category"].value_counts())
    print(df.groupby("Frequency of Purchases")["Previous Purchases"].median())
    print(df.groupby("Season")["Review Rating"].mean())