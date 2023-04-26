import sqlite3
import pandas


"ühendab pythoni sqliteis oleva databaseiga"
yhendus = sqlite3.connect('epood_kkalamets')
cursor = yhendus.cursor()
"""
paring = yhendus.execute('SELECT * FROM kkalamets limit 10')
for rida in paring:
    print(rida[0])
    print(rida[1])
    print(rida[2])
    print(rida[3])
    print(rida[4])
    print(rida[5])
    print(rida[6],'\n')
    """

"kasutaja saab lisada andmeid"
def func1():
    a = input('Sisesta eesnimi: ')
    b = input('Sisesta perenimi: ')
    c = input('Sisesta email: ')
    d = input('Sisesta auto mark: ')
    f = input('Sisesta auto mudel: ')
    g = int(input('Sisesta auto aasta: '))
    h = int(input('Sisesta auto hind: '))
    andmed = [a,b,c,d,f,g,h]
    def insertVaribleIntoTable(first_name, last_name, email, car_make, car_model, car_year, car_price):
        sqliteinsert = """INSERT INTO kkalamets (first_name, last_name, email, car_make, car_model, car_year, car_price)
        VALUES(?, ?, ?, ?, ?, ?, ?);"""
        sqtuple = (first_name, last_name, email, car_make, car_model, car_year, car_price)
        cursor.execute(sqliteinsert, sqtuple)
        yhendus.commit()
        cursor.close()
    insertVaribleIntoTable(andmed[0],andmed[1],andmed[2],andmed[3],andmed[4],andmed[5],andmed[6])

def func2():
    s = yhendus.execute('SELECT * FROM kkalamets limit 1')
    z = 0
    k = 0
    o = 0
    for rida in s:
        if(rida[7] > z):
            z = rida[7]
        k += rida[6]
        o += 1
        if(rida[6] < 2000):
            print(rida[0])
            print(rida[1])
            print(rida[2])
            print(rida[3])
            print(rida[4])
            print(rida[5])
            print(rida[6])
            print(rida[7],'\n')
    r = k//o
    print('Keskmine autode aasta on:',r,'Kõige kallim auto hind on:',z,)

"Kuvab 5 kõige uuema auto info"
def func3():
    q = yhendus.execute('SELECT * FROM kkalamets ORDER BY car_year DESC limit 5')
    for n in q:
        print(n[0])
        print(n[1])
        print(n[2])
        print(n[3])
        print(n[4])
        print(n[5])
        print(n[6])
        print(n[7],'\n')

"Kustutab ID järgi mille kasutaja sisestab"
def func4():
    p = input('sisesta ID mida kustutada: ')
    print('Kustutatud \n')
    yhendus.execute('DELETE from kkalamets where id ='+p)
    yhendus.commit()

def func5():
    i = input('Mis aastast ning alla kustudada andmeid: ')
    j = input('Mis automarki soovid kustutada: ')
    print('\n')
    m = yhendus.execute('SELECT * from kkalamets where car_year <= '+i+' and car_make = "'+j+'"')
    for p in m:
        print(p[0])
        print(p[1])
        print(p[2])
        print(p[3])
        print(p[4])
        print(p[5])
        print(p[6])
        print(p[7],'\n')
    l = input('Kas soovid need andmed kustutada (y/n): ')
    if l == 'y':
        yhendus.execute('DELETE from kkalamets where car_year <= '+i+' and car_make = '+j)
        yhendus.commit()
    else:
        print('Ei ole kustutatud')
def func6():
    df = pandas.read_sql_query('select * from kkalamets', yhendus)
    df.to_csv(r'epood.csv')

def func7():
    print("funktsioon")
    u = yhendus.execute('SELECT * from kkalamets where car_year <= 2000 limit 20')
    for v in u:
        print(v[0])
        print(v[1])
        print(v[2])
        print(v[3])
        print(v[4])
        print(v[5])
        print(v[6])
        print(v[7],'\n')

print('1. Lisa andmeid')
print('2. Kuvab read kus aasta on 2000 või alla (max 20)')
print('3. keskmine aasta ning kõige kallim hind')
print('4. kuvab 5 kõige uuema andmed')
print('5. kuvab 5 kõige kallimat automarki sinu valikul')
print('6. kustuta ID järgi')
print('7. Kustuda massiliselt')
print('8. ekspordi csv faili')
t = input('Mida soovid teha: ')
if t == 2:
    func7()