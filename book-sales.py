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
    df = pd.read_csv("data/Books_Data_Clean.csv")
    df = df[df["Publishing Year"] > 1900]
    df.dropna(subset = "Book Name", inplace = True)

    # Histrogram
    plt.hist(df["Publishing Year"])
    plot(title="Distribution of Publishing Year", xlabel="Publishing Year", ylabel="Frequency")

    # Bar Chart
    df['genre'].value_counts().plot(kind='bar')
    plot(title="Number of Books Per Genre", xlabel="Genre", ylabel="Number of Books")

    df.groupby("Author")["gross sales"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
    plot(title="Total Gross Sales Per Author", xlabel="Author", ylabel="Total Gross Sales")

    # Box Plot
    sns.boxplot(data=df, x="genre", y="Book_ratings_count")
    plot(title="Book Ratings Count Per Genre", xlabel="Genre", ylabel="Book Ratings Count")

    sns.boxplot(data=df, x="Author_Rating", y="units sold")
    plot(title="Units Sold Per Author Rating", xlabel="Author Rating", ylabel="Units Sold")

    # Scatter Plot
    plt.scatter(df["sale price"], df["units sold"])
    plot(title="Sale Price vs. Units Sold", xlabel="Sale Price", ylabel="Units Sold")

    plt.scatter(df["Book_average_rating"], df["Book_ratings_count"])
    plot(title="Book Average Rating vs. Book Ratings Count", xlabel="Book Average Rating", ylabel="Book Ratings Count")

    # Group By
    print(df.groupby("Publisher ")["publisher revenue"].sum().sort_values(ascending=False))
    print(df.groupby("Author_Rating")["Book_ratings_count"].mean().sort_values(ascending=False).head())
    print(df.groupby("language_code").size().sort_values(ascending=False))

    # Line Chart
    df.groupby("Publishing Year")["units sold"].sum().plot(kind="line", marker="o")
    plot(title="Total Units Sold Over Time", xlabel="Publishing Year", ylabel="Total Units Sold")