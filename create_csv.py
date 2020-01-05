import pandas as pd
import bills
import datetime
import os

mydate = datetime.datetime.now()
month = str(mydate.strftime("%B"))

df = pd.DataFrame.from_dict(bills.bills)
directory = (__file__)
path = directory.replace(os.path.basename(__file__), 'Bills_CSVs\\')


for x in df: #Change due dates in df to due dates in pandas.datetime.date format
	if type(df[str(x)]["Day"]) == int:
		df[str(x)]["Day"] = ("{}-{}-{}".format(mydate.year, mydate.month, df[str(x)]["Day"]))
	elif (df[str(x)]["Day"]) == "w":
		pay_counter = 0
		saturday = pd.to_datetime("2019-11-30")
		for y in range(0, 60):
			saturday = saturday + pd.DateOffset(days=7)
			if saturday.month == mydate.month  and saturday.year == mydate.year:
				pay_counter = pay_counter + 1
				df[(str(x)+str(pay_counter))] = df[str(x)].copy()
				df[(str(x)+str(pay_counter))]["Day"] = saturday.date()
		df = df.drop([str(x)], axis=1)
	elif (df[str(x)]["Day"]) == "m":
		saturday = pd.to_datetime("2019-11-30")
		pay_counter = 0
		for y in range(0, 60):
			saturday = saturday + pd.DateOffset(days=7)
			if saturday.month == mydate.month  and saturday.year == mydate.year:
				pay_counter = pay_counter + 1
				if pay_counter == 4:
					(df[str(x)]["Day"]) = saturday.date()
	elif (df[str(x)]["Day"]) == "b":
		pay_counter = 0
		saturday = pd.to_datetime("2019-11-30") #this needs to be a saturday that the biweekly bill is paid
		for y in range(0, 60):
			saturday = saturday + pd.DateOffset(days=14)
			if saturday.month == mydate.month  and saturday.year == mydate.year:
				pay_counter = pay_counter + 1
				df[(str(x)+str(pay_counter))] = df[str(x)].copy()
				df[(str(x)+str(pay_counter))]["Day"] = saturday.date()
		df = df.drop([str(x)], axis=1)

df.to_csv(path + month + '.testing.csv')