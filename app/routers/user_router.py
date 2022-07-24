from fastapi import APIRouter

from app.schema.UserModel import UserId, User

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

users = []

@router.get("/")
async def get_users():
    return users


@router.post("/")
async def create_user(user: User):
    user = user.dict()
    users.append(user)
    print("CTREATE")
    return {"response": "Usuario creado satisfactoriamente!"}


# query parameters: http://127.0.0.1:8000/user/1
@router.post('/{user_id}')
async def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return {"message": "Usuario no encontrado"}


@router.post("2/")  # Otra forma
async def get_user2(user_id: UserId):
    for user in users:
        if user["id"] == user_id.id:
            return user

    return {"message": "Usuario no encontrado"}


@router.delete("/{user_id}")
async def delete(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"message": "Usuario eliminado correctamente"}

    return {"message": "Usuario no encontrado"}


@router.put("/")
async def update(user_update: User):
    for index, user in enumerate(users):
        print(user["id"], user_update.id)
        if user["id"] == user_update.id:
            users[index]["name"] = user_update.dict()["name"]
            return {"message": "Usuario actualizado correctametne"}

    return {"message": "Usuario no encontrado"}
