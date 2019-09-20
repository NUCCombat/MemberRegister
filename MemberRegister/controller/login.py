from flask import render_template, request, redirect, url_for

from .. import app
from ..handler.session import auth_in, auth_out, login_required, is_auth_in
from ..model import Admin


@app.route("/login", methods=['POST', 'GET'])
def login_page():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form['username']
    password = request.form['password']

    admin = Admin.query.filter(Admin.username == username).first()
    if admin is None:
        return render_template("login.html", msg="用户名不存在")

    if password != admin.password:
        return render_template("login.html", msg="密码错误")

    auth_in(admin)
    return redirect("/")


@app.route("/logout")
@login_required
def logout_page():
    auth_out()
    return redirect(url_for("page_index"))
