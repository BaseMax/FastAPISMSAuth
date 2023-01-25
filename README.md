# Fast API SMS Authentication

This is a simple example of how to use FastAPI to create a simple authentication system based on phone number with SMS verification. We used SQLite as a database. (Login, Register, Auth, Panel, Whoiam, Hi)

## Routes

- `/register`: Register a new user (name, phone number, city)
- `/login`: Login with phone number
- `/auth`: Authenticate with verification code
- `/panel`: Get user info
- `/whoiam`: Get user role
- `/hi`: Hi

### FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

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
