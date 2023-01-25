import sqlite3

# connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

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
