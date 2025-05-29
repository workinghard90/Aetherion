from flask_admin import AdminIndexView, expose
from flask import redirect, url_for
from flask_login import current_user

class SecureAdmin(AdminIndexView):
    @expose("/")
    def index(self):
        if not self.is_accessible():
            return self.inaccessible_callback("admin.index")
        return super().index()

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))
