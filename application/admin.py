from flask_admin.contrib.sqla import ModelView

from flask import redirect, url_for


class UserView(ModelView):

    def is_accessible(self):
        return True



    can_create = False

    column_searchable_list = ['username']