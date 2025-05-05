from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session, sessionmaker

from db.engine import engine
# from db.model import User,Meal,Salat,Fast_Food,Order

session = sessionmaker(engine)()


async def save(model, values):
    query_insert = insert(model).values(**values)
    session.execute(query_insert)
    session.commit()



async def select_one(model, filter_value):
    query_select = select(model).filter(model.chat_id == filter_value)
    result = session.execute(query_select)
    return result.scalars().first()


async def delete_record(model, filter_value):
    with Session(engine) as session:
        query_delete = delete(model).filter(model.id == filter_value)
        session.execute(query_delete)
        session.commit()

# async def update_record(model, id, new_value):
#     with Session(engine) as session:
#         query_update = (
#             update(model)
#             .where(model.id == id)
#             .values(phone_number=new_value)
#         )
#         session.execute(query_update)
#         session.commit()

