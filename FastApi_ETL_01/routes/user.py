from fastapi import APIRouter

user = APIRouter()

@user.get("/")
def helloworld():
    return "hello world"