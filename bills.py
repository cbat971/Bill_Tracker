import pandas as pd


#If bills are paid anytime of the month then Day = "m"
#If bills are paid biweekly then Day = "b"
#If bills are paid weekly then Day = "w"



bills = {"Index" : {"Day": "Day", "Amount": "Amount", "Paid": 'Paid'},
"Rent" : {"Day": 1, "Amount": 775, "Paid": False},
'Haley_car': {"Day": 10, "Amount": 230, "Paid": False},
'Chris_car': {"Day": 17 , "Amount": 330, "Paid": False},
'Phones': {"Day": 'm', "Amount": 350, "Paid": False},
'Daycare': {"Day": 'b', "Amount": 50, "Paid": False},
'Power': {"Day": 13, "Amount": 140, "Paid": False},
'Charter': {"Day": 'm', "Amount": 75, "Paid": False},
'Food': {"Day": 'w', "Amount": 140, "Paid": False},
'Haley_insurance': {"Day":17, "Amount": 208, "Paid": False},
'Chris_insurance': {"Day": 'm', "Amount": 150, "Paid": False},
}
