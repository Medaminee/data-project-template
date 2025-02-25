from src.data_analysis import load_data, get_summary_statistics, filter_by_age
from src.data_visualization import plot_age_distribution


def main():
    # Load the dataset
    df = load_data("data/sample_data.csv")

    # Print summary statistics
    summary = get_summary_statistics(df)
    print("Summary Statistics:\n", summary)

    # Filter by age
    older_than_30 = filter_by_age(df, 30)
    print("\nPeople older than 30:\n", older_than_30)

    # Plot age distribution
    plot_age_distribution(df)


if __name__ == "__main__":
    main()
