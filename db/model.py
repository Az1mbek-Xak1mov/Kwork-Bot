from db.manager import Manager


class Customer(Manager):
    def __init__(self ,id:int=None,name:str=None,contact:int=None,chat_id:int=None):
        self.id=id
        self.name=name
        self.contact=contact
        self.chat_id=chat_id


class Developer(Manager):
    def __init__(self ,id:int=None,name:str=None,contact:int=None,occupation:str=None,chat_id:int=None):
        self.id=id
        self.name=name
        self.contact=contact
        self.occupation=occupation
        self.chat_id=chat_id

class Project(Manager):
    def __init__(self,id:int=None,name:str=None,description:str=None,price:int=None,deadline:int=None,occupation:str=None,tz:str=None):
        self.id=id
        self.name=name
        self.description=description
        self.price=price
        self.deadline=deadline
        self.occupation=occupation
        self.tz=tz