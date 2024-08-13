import pandas as pd
import os

# Make one dataframe from all the data
data = pd.DataFrame()

for root, dirs, files in os.walk("bse_stock_data"):
    for file in files:
        if file.endswith(".csv"):
            temp_data = pd.read_csv(os.path.join(root, file), index_col=0)
            # Rename the column to the file name
            temp_data = temp_data[['Open Price']]
            temp_data.columns = [file.split('.')[0]]
            data = pd.concat([data, temp_data], axis=1)

data.to_excel('omf_all_data.xlsx')