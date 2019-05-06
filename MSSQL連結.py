import pyodbc

server='SSPC135V2\SQLEXPRESS01'
database='BESDB'
username='sa'
password='12664093'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT emp_na from bes_emp ")
row = cursor.fetchone()
while row :
    print(row)
    row = cursor.fetchone()
    
