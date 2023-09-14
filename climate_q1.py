
import matplotlib.pyplot as plt
#Start
import sqlite3

con = sqlite3.connect('climate.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM ClimateData")# Returns array of tuples

years = []
co2 = []
temp = []

#grabs the relevant index of each tuple to populate lists
for tuple_row in cursor.fetchall():
    years.append(tuple_row[0])
    co2.append(tuple_row[1])
    temp.append(tuple_row[2])
#end of changes

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
