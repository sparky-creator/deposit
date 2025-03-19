from datetime import datetime
import pandas as pd

today =datetime.now()
today_tuple =(today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthday_dict ={}

for (index, data_row) in data.iterrows():
    print(index)
    print(data_row)
# data row in pandas

birth_dict = { (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
print(birth_dict)
print(birth_dict['(3, 3)'])