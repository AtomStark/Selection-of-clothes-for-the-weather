import postgresql
from User import User

try:
    db = postgresql.open('pq://postgres:postgres@localhost:5432/selectedDB')
except postgresql.exceptions.ClientCannotConnectError:
    print("ERROR : No connect to BD")
    exit()

def user_get(user_name):
    try:
        data = db.query("SELECT id, name, user_id, city_id, yesterdays_color FROM selected.users WHERE name = " + user_name)
    except postgresql.exceptions.UndefinedTableError:
        print("ERROR : Table not exists")
        exit()
    id = data[0][0]
    user_name = data[0][1]
    user_id = data[0][2]
    city_id = data[0][3]
    yesterdays_color = data[0][4]
    user = User(id, user_name, user_id, city_id, yesterdays_color)
    return user


def get_Сlothes(table, yesterdays_color):
    data = db.query("SELECT id, name, color FROM selected." + table + " WHERE use = 'NO'")
    if not data:
        db.query("UPDATE selected." + table +" SET use = 'NO' WHERE use = 'YES'")
        data = db.query("SELECT id, name, color FROM selected." + table + " WHERE use = 'NO'")
    x = 0
    while x <= len(data) - 1:
        if data[x][1] != yesterdays_color:
            choice = data[x][1]
            id = str((data[x][0]))
            db.query("UPDATE selected." + table + " SET use = 'YES' WHERE id = '" + id + "'")
            break
        x += 1
    else:
        choice = data[0][1]
    return choice

def create_users_table(name_BD):
    db.execute("CREATE TABLE " + name_BD + " (id SERIAL PRIMARY KEY, name VARCHAR (64), user_id VARCHAR (64), city_id VARCHAR (64))")
    print("BD created")

def create_user(name, user_id, city_id):
    ins = db.prepare("INSERT INTO selected.users (name, user_id, city_id) VALUES ($1, $2, $3)")
    ins(name, user_id, city_id)
    print("User created")

def create_tshirts_table():
    db.execute("CREATE TABLE selected.tshirts (id SERIAL PRIMARY KEY, name VARCHAR (64), color VARCHAR (64), use VARCHAR (64))")

def create_outerwear_table():
    db.execute("CREATE TABLE selected.outerwear (id SERIAL PRIMARY KEY, name VARCHAR (64), temp_min INT, temp_max INT )")

def create_tshirts(name, color, use="NO"):
    ins = db.prepare("INSERT INTO selected.tshirts (name, color, use) VALUES ($1, $2, $3)")
    ins(name, color, use)
    print("T-Shirts " + name + " created")
