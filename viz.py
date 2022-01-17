import pandas as pd
import matplotlib.pyplot as plt


def get_missing_time_periods(dates, frequency):
    """
    Function to find the missing dates from a series (find's missing dates, not na's)
    
    :param dates (pd.Series): time series of interest
    :param frequency (str): frequency of the data (must be pandas format)
    
    :ret all_dates, out (pd.Series): full date range, missing dates
    """

    # TODO: should frequency be changed to kwargs so any additional arguments can be passed to date_range ...
    
    all_dates = pd.date_range(start=dates.min(), end=dates.max(), freq=frequency)
    
    return all_dates, all_dates.difference(dates)

def show_gaps(dates):
    """
    Function to show the gaps in the time series
    
    :param dates (pd.Series): data of interest dates
    
    :ret None
    """
    print((dates-dates.shift(1)).value_counts())

def show_missing_dates(dates, frequency, ax=None, lw=10, **kwargs):
    """
    Function to show the missing dates in a date range
    
    :param dates (pd.Series): data of pandas datetime
    :param frequency (str): frequency of the data
    :params kwargs (dict): 
    
    :ret ax (matplotlib axes): missing plot
    """
    # TODO: add the percent of continuously missing data ...
    
    full_range, missing_dates = get_missing_time_periods(dates, frequency)
    
    if not ax:
        fig, ax = plt.subplots()
    
    ax.scatter(
        full_range, 
        [1] * len(full_range),
        marker='_',
        lw=lw,
        label='Observed'
    )
    
    ax.scatter(
        missing_dates, 
        [1] * len(missing_dates),
        marker='_',
        lw=lw,
        label='Missing'
    )
    # rotate since the lavels are dates, show the legend ...
    plt.xticks(rotation=90)
    ax.legend()
    
    ax.set(
        yticks=[1],
        yticklabels=['Date'],
        **kwargs
    )
    
    return ax