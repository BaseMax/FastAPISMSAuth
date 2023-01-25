# Fast API Authentication

This is a simple example of how to use FastAPI to create a simple authentication system based on phone number with SMS verification. (Login, Register, Auth, Panel, Whoiam, Hi)

## Routes

- `/register`: Register a new user (name, phone number, city)
- `/login`: Login with phone number
- `/auth`: Authenticate with verification code
- `/panel`: Get user info
- `/whoiam`: Get user role
- `/hi`: Hi

## How to run

```bash
$ uvicorn main:app --reload
```

## How to test

```bash
$ python test.py
```

## How to debug

```bash
$ python print-db.py
```

Copyright (c) 2022, Max Base
