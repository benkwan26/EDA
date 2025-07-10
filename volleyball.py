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
    df = pd.read_csv("data/VNL2023.csv")
    df.rename(columns={"Recieve ": "Receive"}, inplace=True)

    # Heat Map
    numeric_cols = df.select_dtypes(include=["int", "float"]).columns
    corr_matrix = df[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=5)
    plot(title="Correlation Matrix Heatmap", xlabel="", ylabel="")

    # Pie Chart
    position_counts = df["Position"].value_counts()
    plt.pie(position_counts, labels=position_counts.index, autopct="%1.1f%%", startangle=90)
    plot(title="Distribution of Positions", xlabel="", ylabel="")

    # Bar Chart
    df.groupby("Country")["Attack"].mean().sort_values(ascending=False).head(5).plot(kind="bar")
    plot(title="Average Attack by Country", xlabel="Country", ylabel="Average Attack")

    df.groupby("Position")["Attack"].mean().sort_values(ascending=False).plot(kind="bar", color="green")
    plot(title="Average Attack by Position", xlabel="Position", ylabel="Average Attack")

    df.groupby("Country")[["Attack", "Block"]].sum().sort_values(ascending=False, by="Attack").plot(kind="bar", stacked="true", colormap="viridis")
    plot(title="Total Attack and Block By Country", xlabel="Country", ylabel="Total Value")

    # Group By
    print(df.groupby("Age")["Serve"].mean().sort_values(ascending=False))
    print(df.groupby(["Country", "Position"])["Attack"].max().reset_index().sort_values(ascending=False, by="Attack").head())
    print(df.groupby("Country")["Dig"].sum())

    # Scatter Plot
    plt.scatter(df["Block"], df["Receive"])
    plot(title="Block vs. Receive", xlabel="Block", ylabel="Receive")

    # Box Plot
    sns.boxplot(x=df["Serve"])
    plot(title="Distribution of Serve Values", xlabel="Serve", ylabel="")

    # Histogram
    plt.hist(df["Age"], bins=20, color="skyblue", edgecolor="black")
    plot(title="Age Distribution", xlabel="Age", ylabel="Count")

    # Line Chart
    df.groupby("Age")["Serve"].mean().plot(kind="line", marker="o", linestyle="-", color="orange")
    plot(title="Serve Trend Over Age Groups", xlabel="Age", ylabel="Average Serve")
