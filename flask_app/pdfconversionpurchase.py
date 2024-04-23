#pip3 install fitz
import fitz
import pandas as pd
import csv

purchase_details_txt = fitz.open('purchase_details.pdf')

db = pd.DataFrame()

for i in range(len(purchase_details_txt)):
        page_words = purchase_details_txt[i].find_tables()
        df = page_words[0].to_pandas()
        df.columns.name = None
        db = pd.concat([db,df])
        print(i)

def amnt_to_int(a):
    a = a.split(',')
    a = int(''.join(a))
    return a
denom_list = list(db['Denominations'])
for i in range(len(denom_list)):
      denom_list[i] = amnt_to_int(denom_list[i])
for i in range(len(denom_list)):
    db['Denominations'].iloc[i] = denom_list[i]
print(db)
        
db.to_csv(f"purchase_details.csv", index=False)
