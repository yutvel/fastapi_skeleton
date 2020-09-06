# FastAPI Skeleton
This repository contains a skeleton FastAPI app.

## Requirements

Python 3.6+

## Installation
Install the required packages in your local environment (ideally virtualenv, conda, etc.).
```bash
pip install -r requirements.txt
``` 

## Setup
1. Duplicate the `.env.example` file and rename it to `.env` 


2. In the `.env` file configure the `API_KEY` entry. The key is used for authenticating our API. <br>
   A sample API key can be generated using Python REPL:
```python
import uuid
print(str(uuid.uuid4()))
```

## Run It

1. Start your  app with: 
```bash
uvicorn fastapi_skeleton.main:app --reload
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
