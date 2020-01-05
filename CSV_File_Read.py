import pandas as pd
import datetime
import os
directory = (__file__)
path = directory.replace(os.path.basename(__file__), r'Bills_CSVs\\')
mydate = datetime.datetime.now()
month = str(mydate.strftime("%B"))
df = pd.read_csv(path + month + ".testing.csv", index_col=[0])
saved_column = df #you can also use df['column_name']



# df.to_csv("test.csv", index=False)
