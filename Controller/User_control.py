from fastapi import HTTPException, status
from Model import Database_Model, Pydantic_Model
from sqlalchemy.future import select

# User Account details

async def get_user_details(email,db):
    get_user = await db.execute(select(Database_Model.User).where(Database_Model.User.Email == email))
    return get_user.scalars().first()


async def change_account(email,request,db):

    query = await db.execute(select(Database_Model.User).where(Database_Model.User.Email == email))

    result = query.scalars().first()

    update_data = request.model_dump(exclude_unset = True)
    
    for field, values in update_data.items():
        setattr(result,field,values)

    await db.commit()
    await db.refresh(result)
    return result


async def delete_user(email,db):
    query = await db.execute(select(Database_Model.User).where(Database_Model.User.Email == email))
    result = query.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Account has been deleted"