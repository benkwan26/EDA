import matplotlib.pyplot as plt
import seaborn as sns

def plot(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    # Load
    df = sns.load_dataset("flights")

    # Group By
    print(df["month"].value_counts())
    print(df.groupby("year")["passengers"].sum())
    print(df.groupby("month")["passengers"].mean())
    print(df["year"].value_counts())

    # Box Plot
    sns.boxplot(data=df, x="year", y="passengers")
    plot(title="Passenger Distribution Per Year", xlabel="Year", ylabel="Passenger Count")

    # Heat Map
    sns.heatmap(df.pivot_table(values="passengers", index="month", columns="year"))
    plot(title="Passenger Count Per Month Per Year", xlabel="Year", ylabel="Month")

    # Line Plot
    sns.lineplot(data=df.groupby("year")[["passengers"]].sum(), x="year", y="passengers")
    plot(title="Passenger Count Per Year", xlabel="Year", ylabel="Passenger Count")

    sns.lineplot(data=df, x="month", y="passengers")
    plot(title="Passenger Count Per Month", xlabel="Month", ylabel="Passenger Count")

    sns.lineplot(data=df.groupby(["year", "month"]).mean(), x="month", y="passengers", hue="year")
    plot(title="Passenger Count Per Month Per Year", xlabel="Month", ylabel="Passenger Count")

    sns.lineplot(data=df, x=df.index, y="passengers")
    plot(title="Passenger Count Over Time", xlabel="Month", ylabel="Passenger Count")

    # Violin Plot
    sns.violinplot(data=df, x="month", y="passengers")
    plot(title="Passenger Count Per Month", xlabel="Month", ylabel="Passenger Count")

    # Histogram
    sns.histplot(data=df, x="passengers", bins=10)
    plot(title="Passenger Count Distribution", xlabel="Passenger Count", ylabel="Flight Count")