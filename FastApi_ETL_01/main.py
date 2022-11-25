from fastapi import FastAPI
from router.router import user

app = FastAPI() 

app.include_router(user)

    
    

