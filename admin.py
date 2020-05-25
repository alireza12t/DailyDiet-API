from flask_admin import Admin
from extentions import db
from users.models import User, UserModelView
from foods.models import Food, FoodModelView

admin = Admin(name='Dailydiet', template_mode='bootstrap3', url='/admin')
# adding models to admin
admin.add_view(UserModelView(User, db.session, endpoint='user_admin'))
admin.add_view(FoodModelView(Food, db.session, endpoint='food_admin'))
