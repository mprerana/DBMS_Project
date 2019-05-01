import pandas as pd
import pyodbc

#xls = pd.ExcelFile("D:/projects/uidai/data/pincodes/Andhra Pradesh.xls")

state = "Tamil Nadu"
xls = pd.ExcelFile("D:/projects/uidai/data/pincodes/"+str(state)+".xls")
data = xls.parse(0)

#df2 = xls.set_index('OFFICE STATUS', drop = False)

con = pyodbc.connect("Driver={SQL Server};Server=localhost\sqlexpress;UID=uidai;PWD=uidai;")
cur = con.cursor()
ls = []
cur.execute('USE tn_uidai;')
cur.commit()

for index, row in data.iterrows():
#	print(row[0])
	if int(row[2]) not in ls:
		ls.append(int(row[2]))
		cur.execute("EXEC add_pincode @pincode = {}, @city = '{}', @district = '{}', @state = 'Tamil Nadu', @country = '{}';".format(int(row[2]), row[4], row[5], "India"))
		cur.commit()
#	ls.append([row[2], row[4], row[5], "Andhra Pradesh", "India"])

# print( data['TALUK'])
#print(df2)