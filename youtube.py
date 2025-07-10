import pandas as pd
pd.set_option("display.float_format", "{:.2f}".format)
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    # Load and Clean
    df = pd.read_csv("data/Global YouTube Statistics.csv", encoding="latin1")

    # Bar Chart
    df.groupby("category")["subscribers"].mean().sort_values(ascending=False).plot(kind="bar")
    plt.xticks(rotation=90)
    plot(title="Mean Subscribers by Category", xlabel="Category", ylabel="Mean Subscribers")

    df.groupby("Country")["subscribers"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
    plt.xticks(rotation=90)
    plot(title="Total Subscribers by Country", xlabel="Country", ylabel="Total Subscribers")

    df.groupby(["category", "Country"])["subscribers"].sum().unstack().plot(kind="bar", stacked=True)
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.xticks(rotation=90)
    plot(title="Subscribers Breakdown by Category and Country", xlabel="Category", ylabel="Total Subscribers")

    df.groupby("channel_type")["Unemployment rate"].mean().sort_values(ascending=False).plot(kind="bar")
    plt.xticks(rotation=90)
    plot(title="Average Unemployment Rate by Channel Type", xlabel="Channel Type", ylabel="Average Unemployment Rate")

    df.groupby(["created_year", "channel_type"])["subscribers"].mean().unstack().tail().plot(kind="bar", width=1)
    plt.xticks(rotation=45)
    plt.legend(title="Channel Type", bbox_to_anchor=(1.05, 1), loc="upper left")
    plot(title="Average Subscribers by Created Year and Channel Type", xlabel="Created Year", ylabel="Average Subscribers")

    # Pie Chart
    df["channel_type"].value_counts().head().plot(kind="pie", autopct="%1.1f%%")
    plot(title="Top 5 Channel Type Distribution", xlabel="", ylabel="")

    # Scatter Plot
    plt.scatter(df["subscribers"], df["video views"])
    plot(title="Subscribers vs. Views", xlabel="Subscribers", ylabel="Video Views")

    plt.scatter(df["Gross tertiary education enrollment (%)"], df["subscribers"], alpha=0.5)
    plot(title="Subscribers vs. Gross Tertiary Education Enrollment", xlabel="Gross Tertiary Education Enrollment", ylabel="Subscribers")

    # Group By
    print(df.groupby("created_year")["subscribers"].mean().sort_values(ascending=True))
    print(df.groupby("channel_type")["video_views_rank"].median().sort_values(ascending=False))
    print(df.groupby("Country")["subscribers_for_last_30_days"].mean().sort_values(ascending=False))
    print(df.groupby("created_month")["subscribers"].sum())
    print(df.groupby("category")["video views"].std())
    print(df.groupby("Country")["Unemployment rate"].min().sort_values(ascending=True))
    print(df.groupby("channel_type")["uploads"].sum())
    print(df.groupby(["Latitude", "Longitude"]).size())

    # Box Plot
    sns.boxplot(x="channel_type", y="highest_monthly_earnings", data=df)
    plt.title("")
    plt.xticks(rotation=90)
    plot(title="Distribution of Highest Monthly Earnings by Channel Type", xlabel="", ylabel="")

    # Line Chart
    df.groupby(["created_year", "created_month"])["subscribers"].sum().unstack().head().plot(kind="line", stacked=True)
    plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.xticks(rotation=45)
    plot(title="Subscribers Growth Over Time", xlabel="Year", ylabel="Total Subscribers")

    df.groupby(["created_year", "Country"])["highest_yearly_earnings"].mean().unstack().head().plot(kind="line", marker="o")
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.xticks(rotation=45)
    plot(title="Trend of Highest Yearly Earnings by Created Year and Country", xlabel="Created Year", ylabel="Average Highest Yearly Earnings")

    df.groupby("created_month")["subscribers_for_last_30_days"].mean().plot(kind="line", marker="o")
    plt.xticks(rotation=45)
    plot(title="Average Subscribers for Last 30 Days by Month", xlabel="Month", ylabel="Average Subscribers for Last 30 Days")

    # Pie Chart
    df.groupby("category")["highest_monthly_earnings"].sum().sort_values(ascending=False).head().plot(kind="pie", autopct="%1.1f%%")
    plot(title="Percentage of Highest Monthly Earnings by Category", xlabel="", ylabel="")

    # Heat Map
    sns.heatmap(df.groupby(["channel_type", "created_year"])["subscribers_for_last_30_days"].mean().unstack(), cmap="YlGnBu")
    plot(title="Mean Subscribesr For Last 30 Days by Channel Type and Created Year", xlabel="Created Year", ylabel="Channel Type")