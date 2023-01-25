import sqlite3

# connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# create the users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
				  (name TEXT, phone_number TEXT, city TEXT)''')

# create the auth table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS auth
				  (phone_number TEXT, verify_code INTEGER, token TEXT)''')
				  
conn.commit()

# Fetch all users
sql = "SELECT * FROM `users`"
cursor.execute(sql)
users = cursor.fetchall()
print("Users:")
for user in users:
    print(user)

# Fetch all auth
sql = "SELECT * FROM `auth`"
cursor.execute(sql)
auths = cursor.fetchall()
print("Auths:")
for auth in auths:
    print(auth)
