import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
labelencoder = preprocessing.LabelEncoder()

def plot(title="", xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":
    # Load
    df = pd.read_csv("data/insurance.csv")
    df.drop_duplicates(inplace=True)

    # Pie Plot
    df["sex"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plot(title="Sex Distribution", xlabel="", ylabel="")

    df["smoker"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plot(title="Smoker Distribution", xlabel="", ylabel="")

    # Count Plot
    sns.countplot(x="region", data=df)
    plot(title="Region Distribution", xlabel="Region", ylabel="Count")

    # Transform
    df["smoker"] = labelencoder.fit_transform(df["smoker"])
    df["sex"] = labelencoder.fit_transform(df["sex"])
    df["region"] = labelencoder.fit_transform(df["region"])

    # Heat Map
    print(df.corr()["charges"].sort_values(ascending=False))
    sns.heatmap(df.corr(), annot=True, cmap="rainbow")

    # Distribution Plot
    for column in df.columns:
        sns.displot(df[column])
        plot(title=column + " Distribution", xlabel=column, ylabel="Count")

    # Scatter Plot
    colours = ["Red", "Green", "Yellow", "Black", "Blue", "Grey"]
    colour_index = 0
    for column in df.columns[:-1]:
        sns.scatterplot(data=df, x=column, y="charges", color=colours[colour_index])
        plot(title=column + " Distribution", xlabel=column, ylabel="Count")
        colour_index += 1