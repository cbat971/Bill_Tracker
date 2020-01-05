import pandas as pd
import budget_calculator

datelist = pd.date_range(pd.datetime.today(), periods=30).day.tolist()
	# periods=int(input("How many days till Payday? "))).day.tolist()
c=datelist[0]
#print((datelist))


days = (pd.to_datetime('today').date() - pd.to_datetime('11-8-2019').date())
if (days.days%14) == 0:
	bi_weekly = "true"
	daycare_date = pd.to_datetime('today').day
else:
	bi_weekly = "false"
	daycare_date = 1
#print(bi_weekly)




#####Prints what day of the week it is.
# datelist = pd.date_range(pd.datetime.today(), periods=20, freq='D').to_series()
# c=datelist[0]
# print((c.dayofweek))
# print((datelist.dt.dayofweek))