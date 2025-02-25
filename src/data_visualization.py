import matplotlib.pyplot as plt


def plot_age_distribution(df):
    """Plot a bar chart for the age distribution of the DataFrame."""
    plt.figure(figsize=(10, 6))
    df["Age"].value_counts().sort_index().plot(kind="bar")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.grid()
    plt.show()
