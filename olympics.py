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
    df = pd.read_csv("data/dataset_olympics.csv")
    df.drop_duplicates(inplace=True)

    # Pie Chart
    df["Sex"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plot(title="Gender Distribution", xlabel="", ylabel="")

    df["Medal"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plot(title="Medal Distribution", xlabel="", ylabel="")

    # Count Plot
    sns.countplot(data=df, x="Year", hue="Medal", hue_order=["Bronze", "Silver", "Gold"])
    plt.xticks(rotation=90)
    plot(title="Medal Distribution Over Time", xlabel="Year", ylabel="Medal Count")

    # Histogram
    sns.histplot(data=df, x="Age", bins=10, kde=True)
    plot(title="Age Distribution", xlabel="Age", ylabel="Count")

    sns.histplot(data=df, x="Height", bins=20, kde=True)
    plot(title="Height Distribution", xlabel="Height (cm)", ylabel="Count")

    sns.histplot(data=df, x="Weight", bins=20, kde=True)
    plot(title="Weight Distribution", xlabel="Weight (kg)", ylabel="Count")

    # Group By and Facts
    print(df.groupby("Year")["Age"].mean())
    print(df.groupby("Sport")["Height"].median())
    print(df.groupby(["NOC", "Sex"])["ID"].count())
    print(df[df["Medal"] == "Gold"].groupby("NOC")["Medal"].count())
    print(df.groupby(["Sport", "Sex"])["Weight"].mean())
    print("Most Medal-Winning Country:", df["NOC"].value_counts().idxmax())
    print("Tallest Athlete:\n\n", df[df["Height"] == df["Height"].max()][["ID", "Name", "Height", "Sport"]])
    print("Heaviest Athlete:", df[df["Weight"] == df["Weight"].max()][["ID", "Name", "Height", "Sport"]])

    # Bar Chart
    df.groupby("Sport")["Event"].nunique().sort_values(ascending=False).plot(kind="bar")
    plt.xticks(rotation=90)
    plot(title="Number of Unique Events Per Sport", xlabel="Sport", ylabel="Count")

    df.groupby("Year")["ID"].nunique().plot(kind="bar")
    plot(title="Number of Participants Over Time", xlabel="Year", ylabel="Number of Participants")

    df.groupby("NOC")["Age"].mean().sort_values(ascending=False).head(10).plot(kind="bar")
    plt.xticks(rotation=45)
    plot(title="Top 10 Countries With Heightest Average Age of Participants", xlabel="Country", ylabel="Average Age")

    # Box Plot
    sns.boxplot(data=df, x="Season", y="Age")
    plot(title="Distribution of Ages by Season", xlabel="Season", ylabel="Age")

    # Violin Plot
    sns.violinplot(data=df, x="Medal", y="Height", order=["Bronze", "Silver", "Gold"], palette="Set2")
    plot(title="Distribution of Height by Medal", xlabel="Medal", ylabel="Height (cm)")

    # Scatter Plot
    sns.scatterplot(data=df, x="Height", y="Weight", hue="Medal", palette="Set1")
    plt.legend(title="Medal")
    plot(title="Athelte Height vs. Weight by Medal Status", xlabel="Height (cm)", ylabel="Weight (kg)")

    # Heat Map
    sns.heatmap(df.pivot_table(index="NOC", columns="Year", values="Medal", aggfunc="count").sample(n=10), linewidths=0.5)
    plt.xticks(rotation=45)
    plot(title="Medal Counts by Country and Year", xlabel="Year", ylabel="Country")