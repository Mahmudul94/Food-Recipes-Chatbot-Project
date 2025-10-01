import pandas as pd
from datetime import datetime, timedelta


# Load the two Excel sheets
sheet1 = pd.read_excel('C:/Users/alam/OneDrive - New York State Thruway Authority/Documents/Malicious Plate/April Request - 2025/output/T_VIOL_TX_202504241405.xlsx')
sheet2 = pd.read_excel('C:/Users/alam/OneDrive - New York State Thruway Authority/Documents/Malicious Plate/April Request - 2025/output/T_TRAN_DETAIL_202504241614.xlsx')


merged_df = pd.merge(sheet1,sheet2, left_on='LANE_TX_ID',  right_on ='LANE_TX_ID')


# Compare full fare amount from first sheet with expected revenue amount, full fare amount and video fare amount from second sheet
comparison_results = merged_df.apply(lambda row: row['FULL_FARE_AMOUNT'] == row['EXPECTED_REVENUE_AMOUNT'] or row['FULL_FARE_AMOUNT'] == row['FULL_FARE_AMOUNT'] or row['FULL_FARE_AMOUNT'] == row['VIDEO_FARE_AMOUNT'], axis=1)


# Add comparison results to the dataframe
merged_df['comparison_results'] = comparison_results


print(merged_df.head())

################################################################################

import pandas as pd

# Existing Excel file
nyolap = pd.read_excel('example_1')
prdrsce =pd.read_excel ('example_2')

# Merge the two sheets on account_no
merged_df = pd.merge(nyolap, prdrsce, how ='inner', on='ID')


# Compare full_fare_amount with expected_fare_amount
merged_df['comparison_result'] = merged_df.apply(lambda row: row['T'] == row['TM'], axis=1)

#Filter Mismatch
mismatches = merged_df[~merged_df['comparison_result']]

# Split the data into chunks
chunk_size = 1000000 # Adjust the chunk size as needed
chunks = [merged_df[i:i+chunk_size] for i in range(0, merged_df.shape[0], chunk_size)]


# Save each chunk to a separate sheet
with pd.ExcelWriter('example_3', engine='openpyxl') as writer:
     for i, chunk in enumerate(chunks):
          chunk.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)



print("Comparison completed. The result is saved in 'comparison_result.xlsx'.")





