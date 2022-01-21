import pandas as pd
from sodapy import Socrata

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