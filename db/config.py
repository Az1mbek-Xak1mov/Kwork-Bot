from db import model
from db.manager import *
from db.model import *

def saving_developer(developer_info:dict):
    dev = model.Developer(
        name=developer_info.get("name"),
        contact=developer_info.get("contact"),
        occupation=developer_info.get("occupation"),
        chat_id=developer_info.get("chat_id")
    )
    dev.save()
def saving_customer(customer_info:dict):
    cus = model.Customer(
        name=customer_info.get("name"),
        contact=customer_info.get("contact"),
        chat_id=customer_info.get("chat_id")
    )
    cus.save()
def saving_project(project_info):
    proj= model.Project(
        name=project_info.get("name"),
        description=project_info.get("description"),
        price=project_info.get("price"),
        deadline=project_info.get("deadline"),
        occupation=project_info.get("occupation"),
        tz=project_info.get("tz"),
    )
    proj.save()