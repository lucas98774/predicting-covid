import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# client = Socrata("data.virginia.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.virginia.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# Returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# results = client.get("bre9-aqqr")

# Convert to pandas DataFrame
# results_df = pd.DataFrame.from_records(results)

def download_data() -> pd.DataFrame:
    """
    Function to download public dataset on covid numbers ...

    # NOTE: using numpy docstring format: https://numpydoc.readthedocs.io/en/latest/format.html

    # NOTE: is there any parameters that allow you to modify what is downloaded??? --- dates or anything else?
    Parameters
    ----------
    None


    Returns
    -------
    results_df: pd.DataFrame
        The dataframe containing info on the covid cases and deaths ...
    """

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata("data.virginia.gov", None)

    # Example authenticated client (needed for non-public datasets):
    # client = Socrata(data.virginia.gov,
    #                  MyAppToken,
    #                  userame="user@example.com",
    #                  password="AFakePassword")

    # Returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get("bre9-aqqr")

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return results_df