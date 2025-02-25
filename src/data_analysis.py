import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load CSV data from a file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def get_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Get summary statistics of the DataFrame."""
    return df.describe()


def filter_by_age(df: pd.DataFrame, age: int) -> pd.DataFrame:
    """Filter the DataFrame to include only people older than a certain age."""
    return df[df["Age"] > age]
