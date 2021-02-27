import pandas as pd
import re

file = "/home/trace/classes/dasc1222/midterm/data/nppes.csv"
df = pd.read_csv(file)

dfOut = df[df.address_purpose == 'LOCATION']

phone = dfOut["telephone_number"].replace("-", "", regex=True)
print(phone)


# dfOut.to_csv('nppes_filtered.csv', index=None, header=True)