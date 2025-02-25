import pandas as pd
from src.data_analysis import load_data, get_summary_statistics, filter_by_age

def test_load_data():
    df = load_data('data/sample_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_get_summary_statistics():
    df = load_data('data/sample_data.csv')
    summary = get_summary_statistics(df)
    assert 'count' in summary['Age']
    assert summary['Age']['mean'] > 0

def test_filter_by_age():
    df = load_data('data/sample_data.csv')
    filtered_df = filter_by_age(df, 30)
    assert all(filtered_df['Age'] > 30)
    assert len(filtered_df) == 2