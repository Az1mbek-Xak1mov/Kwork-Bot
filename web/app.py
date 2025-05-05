from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin,ModelView

from db.engine import engine
from db.model import User, Meal, Order, Fast_Food,Salat

app=Starlette()
admin=Admin(engine=engine,
            title="restaran",
            base_url="/"
)
admin.add_view(ModelView(User))
admin.add_view(ModelView(Meal))
admin.add_view(ModelView(Fast_Food))
admin.add_view(ModelView(Order))
admin.add_view(ModelView(Salat))

admin.mount_to(app)