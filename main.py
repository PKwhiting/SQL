import sqlite3
from sqlite3 import Error
import pandas as pd

#creating the db connection
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\Users\dsxgyy1\Desktop\Main\Language Practice\SQL\SQL\sqlite\db\pythonsqlite.db")


conn = sqlite3.connect('sqlite/db/pythonsqlite.db')
c = conn.cursor()

#creating the database
c.execute('''CREATE TABLE autos_mpg (mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,car_name)''')

#importing the csv file using pandas
vehicles = pd.read_csv('autos_mpg.csv')
#pushing the imported csv file into the db
vehicles.to_sql('autos_mpg', conn, if_exists='append', index = False)




conn = sqlite3.connect('sqlite/db/pythonsqlite.db')
c = conn.cursor()

#basic function to query the database with user input
def display_by_mpg(year):
    num = int(year)
    mpgs = c.execute('''SELECT avg(mpg) FROM autos_mpg WHERE model_year = ? ''',(num,)).fetchall()
    print(mpgs)
    pass
def display_by_hp(year):
    num = int(year)
    hps = c.execute('''SELECT avg(horsepower) FROM autos_mpg WHERE model_year = ? ''',(num,)).fetchall()
    print(hps)
    pass
def display_max_hp(year):
    num = int(year)
    hp = c.execute('''SELECT car_name, MAX(horsepower) FROM autos_mpg WHERE model_year = ?''',(num,)).fetchall()
    return hp

def add_vehicle(mpg,cylinders,displacement,hp,weight,accl,year,origin,model):
    c.execute('''INSERT INTO autos_mpg (mpg,cylinders,displacement,horsepower,weight,acceleration,model_year,origin,car_name) 
    VALUES(?,?,?,?,?,?,?,?,?)''',
    (mpg,cylinders,displacement,hp,weight,accl,year,origin,model))
    conn.commit()
    pass
def delete_vehicle(weight):
    num = int(weight)
    c.execute('''DELETE FROM autos_mpg WHERE weight = ?''',(num,))
    conn.commit()
    pass
def modify_vehilce(weight, mpg):
    weight = int(weight)
    mpg = int(mpg)
    c.execute('''UPDATE autos_mpg SET mpg=? WHERE weight=?''',(mpg,weight,))
    conn.commit()
    pass
cont = True
inp = ''
inventory = []
#while loop that controls the program
while cont == True:
    print('What would you like to do? Select Action')
    print('Display vehicles by MPG(1)')
    print('Display vehicles by HP(2)')
    print('Display max vehicle HP by year(3)')
    print('Add Vehicle(4)')
    print('Delete Vehicle(5)')
    print('Update Vehilce(6)')
    print('Print Inventory(7)')
    inp = input('Enter Selection: ')
    if inp == '1':
        year = input('Enter Year between 70 and 82: ')
        display_by_mpg(year)

    if inp == '2':
        year = input('Enter Year between 70 and 82: ')
        display_by_hp(year)

    if inp == '3':
        year = input('Enter Year between 70 and 82: ')
        print(display_max_hp(year))
        inp = input("Would you like to store vehicle in your inventory?")
        if inp == 'y' or inp == 'yes':
            inventory.append(display_max_hp(year))
    if inp == '4':
        mpg = input('Enter vehicle MPG: ')
        mpg = int(mpg)
        if mpg >50 or mpg <5:
            print('NA Try again')
            break
        cylinders = input('Enter vehicles number of cylinders: ')
        cylinders = float(cylinders)
        if cylinders > 12 or cylinders < 4:
            print('NA Try again')
            break
        displacement = input('Enter vehicles engine displacement: ')
        hp = input('Enter vehicle horsepower: ')
        hp = float(hp)
        if hp > 1000 or hp < 25:
            print('NA Try again')
        weight = input('Enter vehicle weight: ')
        weight= float(weight)
        if weight > 10000 or weight < 1000:
            print('NA Try again')
            break
        accl = input('Enter vehicle acceleration: ')
        accl = float(accl)
        year = input('Enter vehicles year: ')
        year = int(year)
        if year >2022 or year < 1900:
            print('NA Try again')
            break
        origin = 1
        model = input('Enter vehicle model: ')
        add_vehicle(mpg,cylinders,displacement,hp,weight,accl,year,origin,model)
        print("vehicle succesfully added")

    if inp == '5':
        weight = input('Enter vehicle weight: ')
        delete_vehicle(weight)
        print('Vehicle Deleted Succesfully')

    if inp == '6':
        weight = input('Enter vehicle weight: ')
        mpg = input ('Enter new MPG of vehicle: ')
        weight = int(weight)
        modify_vehilce(weight,mpg)
        print('Vehicle modified succesfully')
    
    if inp == '7':
        print(inventory
        )
    resp = input('continue?: ')
    if resp == 'no' or resp == 'n':
        break
    
print('Thank You')