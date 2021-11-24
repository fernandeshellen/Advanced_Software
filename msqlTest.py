import mysql.connector
import datetime
import time
import forex_python

from forex_python.converter import CurrencyRates

c = CurrencyRates()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Programmer2@",
    port=3306,
    database="currencyConverter",
)

print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE currencyConverter")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#    print(x)

# mycursor.execute("DROP TABLE Currency")

# mycursor.execute(
#     "CREATE TABLE Currency (Month INT, Day INT, Year INT, CurrencyRate FLOAT(10, 6))"
# )

for i in range(1, 31):
    date_obj = datetime.datetime(2020, 1, i, 18, 36, 28, 151012)

    try:
        myRate = c.get_rate("USD", "BRL", date_obj)
        print(myRate)

        sql = (
            "INSERT INTO Currency (Month, Day, Year, CurrencyRate) VALUES ("
            + str(1)
            + ", "
            + str(i)
            + ", 2020, "
            + str(myRate)
            + ")"
        )
        mycursor.execute(sql)

    except forex_python.converter.RatesNotAvailableError:
        print("Oops!  That was no valid number.  Try again...")

# sql = (
#     "INSERT INTO Currency (Month, Day, Year, CurrencyRate) VALUES ("
#     + str(i)
#     + ", 1, 2020, "
#     + str(myRate)
#     + ")"
# )
# val = (1, 20, 2021, 1.05)

# mycursor.execute(sql)

# mycursor.execute("TRUNCATE TABLE Currency")

mydb.commit()

# print(mycursor.rowcount, "record inserted.")