#  ------------------------- 1 --------------------
import pandas as pd
from pandas_profiling import ProfileReport

#  ------------------------- 2 --------------------
df = pd.read_csv('analyze.csv')
# print(df)

#  ------------------------- 3 --------------------
dfReport = ProfileReport(df)
dfReport.to_file(output_file="analyzed.html")

"""
    1. GIVE TITLE 
dfReport = ProfileReport(df, title='MY REPORT')

    2. GIVE HIDE SOME DETAILS
dfReport = ProfileReport(samples=None, correlations=None, missing_diagrams=None, duplicates=None, interactions=None)
         OR
dfReport = ProfileReport(df, minimal=True)

"""

