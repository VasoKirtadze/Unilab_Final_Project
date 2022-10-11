from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView
from flask import redirect, url_for
from flask_login import current_user


class Authmixin(object):

    def is_accessible(self):
        return current_user.has_roles('Admin')

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('public.home_page'))


class CudstomBaseView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_roles('Admin')

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('public.home_page'))


class UserView(ModelView, Authmixin):

    can_edit = True
    can_create = False

    column_searchable_list = ['username']
    column_exclude_list = ['password_hash']


admin = Admin(name="Admin Panel", template_mode="bootstrap4", index_view=CudstomBaseView())
