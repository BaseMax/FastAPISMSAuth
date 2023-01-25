from fastapi import Header, FastAPI, HTTPException
from pydantic import BaseModel,validator
import sqlite3
import uuid
import requests

app = FastAPI()

# define the User model for validation
class User(BaseModel):
	name: str
	phone_number: str
	city: str

	# validator the phone_number
	@validator("phone_number")
	def validate_phone_number(cls, v):
		if not v.isnumeric() or len(v) != 11:
			raise ValueError("Phone number must be 11 digits.")
		return v

	# validate the name
	@validator("name")
	def validate_name(cls, v):
		if not v.strip():
			raise ValueError("Name cannot be empty.")
		return v

# define the Auth model for validation
class Auth(BaseModel):
	phone_number: str
	verify_code: str

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

# define the register route
@app.post("/register")
async def register(user: User):
	# check if the phone number already exists in the database
	cursor.execute(f"SELECT * FROM users WHERE phone_number='{user.phone_number}'")
	if cursor.fetchone() is not None:
		raise HTTPException(status_code=400, detail="Phone number already exists.")
	# insert the user into the database
	cursor.execute(f"INSERT INTO users (name, phone_number, city) VALUES ('{user.name}', '{user.phone_number}', '{user.city}')")
	conn.commit()
	return {"message": "User created successfully."}

# define the login route
@app.post("/login")
async def login(auth: Auth):
	# check if the phone number exists in the database
	cursor.execute(f"SELECT * FROM users WHERE phone_number='{auth.phone_number}'")
	if cursor.fetchone() is None:
		raise HTTPException(status_code=400, detail="Phone number not found.")
	# generate a random verify code
	verify_code = randint(1000, 9999)
	# insert the verify code into the auth table
	cursor.execute(f"INSERT INTO auth (phone_number, verify_code) VALUES ('{auth.phone_number}', '{verify_code}')")
	conn.commit()
	# send the verify code via SMS
	response = requests.get(f"https://sms-api.com/send?phone_number={auth.phone_number}&verify_code={verify_code}")
	if response.status_code != 200:
		raise HTTPException(status_code=500, detail="Error sending SMS.")
	return {"message": "Verification code sent successfully."}

# define the auth route
@app.post("/auth")
async def auth(auth: Auth):
	# check if the verify code is valid
	cursor.execute(f"SELECT * FROM auth WHERE phone_number='{auth.phone_number}' AND verify_code='{auth.verify_code}'")
	if cursor.fetchone() is None:
		raise HTTPException(status_code=400, detail="Invalid verification code.")

	# generate a random token
	token = str(uuid.uuid4())
	# update the auth table with the token
	cursor.execute(f"UPDATE auth SET token='{token}' WHERE phone_number='{auth.phone_number}' AND verify_code='{auth.verify_code}'")
	conn.commit()
	return {"message": "Session activated.", "token": token}

# define the panel route
@app.get("/panel")
async def panel(x_token: str = Header(None)):
	# check if the token is valid
	cursor.execute(f"SELECT * FROM auth WHERE token='{x_token}'")
	user = cursor.fetchone()
	if user is None:
		raise HTTPException(status_code=400, detail="Invalid token.")
	# return the name of the user
	return {"name": user[0]}
