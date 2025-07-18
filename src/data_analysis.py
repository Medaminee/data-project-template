import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV data from a file into a pandas DataFrame.
    :param file_path: csv file path to load.
    :type file_path: str
    :return: pandas dataframe of the file.
    :rtype: pd.DataFrame
    """
    return pd.read_csv(file_path)


def get_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get summary statistics of the DataFrame.
    :param df: pandas dataframe to compute statistics.
    :type df: pd.DataFrame
    :return: summary statistics of the DataFrame.
    :rtype: pd.DataFrame
    """
    return df.describe()


def filter_by_age(df: pd.DataFrame, age: int) -> pd.DataFrame:
    """
    Filter the DataFrame to include only people older than a certain age.
    :param df: pandas dataframe to filter.
    :type df: pd.DataFrame
    :param age: age value to filter on.
    :type age: int
    :return: Filtered DataFrame.
    :rtype: pd.DataFrame
    """
    return df[df["Age"] > age]
