import pandas as pd
import matplotlib.pyplot as plt

def plot(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    # Load and Clean
    df = pd.read_csv("data/movie_profit.csv")
    df = df.drop(columns=("Unnamed: 0")).dropna()

    # Group By
    print(df.groupby("mpaa_rating")["domestic_gross"].mean())
    print(df.groupby("distributor")["worldwide_gross"].sum().sort_values(ascending=False))
    print(df.groupby("genre")["production_budget"].mean())
    print(df.groupby("mpaa_rating")["domestic_gross"].median())
    print(df.groupby(df["release_date"].str.slice(6, 8))["movie"].count().sort_values(ascending=False).head())
    print(df.groupby("genre")["domestic_gross"].max())
    print(df.groupby("mpaa_rating")["production_budget"].min())
    print(df.groupby("distributor")["worldwide_gross"].mean())
    print(df.groupby("mpaa_rating")["worldwide_gross"].std())

    # Histogram
    plt.hist(df["worldwide_gross"])
    plot(title="Distribution of Worldwide Gross", xlabel="Worldside Gross", ylabel="Frequency")

    # Bar Chart
    plt.bar(df["release_date"].head(), df["domestic_gross"].head()) # 5 "random" movies
    plot(title="Release Date Domestic Gross", xlabel="", ylabel="Domestic Gross")

    df.groupby("genre")["production_budget"].sum().sort_values(ascending=False).plot(kind="bar")
    plot(title="Total Production Budget by Genre", xlabel="Genre", ylabel="Total Production Budget")

    df.groupby("distributor")["domestic_gross"].mean().head().plot(kind="barh") # 5 "random" distributor
    plot(title="Average Domestic Gross by Distributor", xlabel="Average Domestic Gross", ylabel="Distributor")

    # Line Chart
    df.groupby(df["release_date"].str.slice(-4, None))["worldwide_gross"].mean().plot(kind="line")
    plot(title="Mean Worldwide Gross Over Years", xlabel="Release Year", ylabel="Mean Worldwide Gross")

    # Pie Chart
    df.groupby("mpaa_rating")["domestic_gross"].sum().plot(kind="pie")
    plot(title="Total Domestic Gross by Rating", xlabel="", ylabel="")

    # Scatter Plot
    df.plot(kind="scatter", x="production_budget", y="worldwide_gross")
    plot(title="Production Budget vs. Worldwide Gross", xlabel="Prodcution Budget", ylabel="Worldwide Gross")