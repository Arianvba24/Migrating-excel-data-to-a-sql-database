#Creating the sql file and the table
import sqlite3

conexion = sqlite3.connect('stocks_database.db')
cursor = conexion.cursor()
cursor.execute("CREATE TABLE stocks3(ID VARCHAR(13) PRIMARY KEY,Type VARCHAR(20),Date reception DATE NOT NULL,Units per stock INT)")
conexion.commit()
conexion.close()

for file in os.listdir(r"C:\Users\Cash\Documents\pruebas_python\proyectos\excel"):
    

    wb = openpyxl.load_workbook(fr"C:\Users\Cash\Documents\pruebas_python\proyectos\excel/{file}")

    ws = wb.active

    data = []

    for i in range(2,1001):
        if f"{ws[f'A{i}'].value}" == "None":
            break
        else:
            data.append([f"{ws[f'A{i}'].value}",f"{ws[f'B{i}'].value}",f"{ws[f'C{i}'].value}",f"{ws[f'D{i}'].value}"])


    conexion = sqlite3.connect("stocks_database.db")
    cursor = conexion.cursor()


    cursor.executemany("INSERT INTO stocks3 VALUES (?,?,?,?)", data)
    conexion.commit()
    conexion.close()
print("Data tranfered succesfully!")