import os.path
import datetime
import text
import pandas as pd
import time
directory = (__file__)
patha = directory.replace(os.path.basename(__file__), r'Bills_CSVs\\')


__name__ == "__main__"


test_txt = directory.replace(os.path.basename(__file__), r'last_message.txt')
mydate = datetime.datetime.now()
month = str(mydate.strftime("%B"))
file = (patha + month + '.testing.csv')



if os.path.isfile(file) == False:
	import create_csv


import CSV_File_Read as cv
df = (cv.df)



import csv
with open(file, 'r') as f:
	reader = csv.reader(f)
	list = list(reader)
	bills = list[0]
	print(bills)


def Bill_Paid(bill):
	print(df[str(bill)]["Paid"])
	df[str(bill)]["Paid"] = "True"
	df.to_csv(file)
	text.text("{} is paid! Thank you!".format(str(bill)))
unpaid_bills = []
for x in range(0, 1):
	for x in df:		
		if df[x]["Paid"] == "False" and pd.to_datetime(df[x]["Day"]) < pd.to_datetime(mydate) + pd.DateOffset(days=7):
			unpaid_bills.append(str(x))
			text.text("We owe {} on {} and it is due on the {} of this month. Pay {}?" \
				.format(str(df[x]["Amount"]), str(x), str(df[x]["Day"]), str(x)))
	f = open(test_txt,'r')
	currentM = f.read()
	f.close()
	print(currentM)
	time.sleep(5)

	for x in range(0, 180):
		time.sleep(5)
		f = open(test_txt,'r')
		oldM = currentM
		currentM = (f.read())
		f.close()

		if currentM != oldM:
			words = currentM.split()

			if "pay" or "Pay" in words:
				for x in words:
					if str(x) in bills:
						Bill_Paid(str(x))
						print("Thank you for paying {}!".format(str(x)))
						unpaid_bills.remove(str(x))
						print(unpaid_bills)
			complete = ['done', 'complete', 'Done', 'Complete', 'Haley', 'Send']
			for x in complete:
				if x in words:
					print(unpaid_bills)
					print('testing complete works.')
					for each in unpaid_bills:
						text.text_wife("We currently still owe {}. Please text Chris if you believe any of these are paid or will be paid by Friday!".format(each))
						time.sleep(2)
			else:
				print("its not in there")
			
		else:
			print(str(currentM) + ' matches')

