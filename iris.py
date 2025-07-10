import matplotlib.pyplot as plt
import seaborn as sns

def plot(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    # Load
    df = sns.load_dataset("iris")
    df.drop_duplicates(inplace=True)

    # Scatter Plot
    sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
    plot(title="Sepal Length vs. Sepal Width", xlabel="Sepal Length", ylabel="Sepal Width")

    # Box Plot
    sns.boxplot(x="sepal_length", y="species", data=df)
    plot(title="Sepal Length vs. Species", xlabel="Sepal Length", ylabel="Species")