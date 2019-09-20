from flask import render_template, request, redirect, url_for

from .. import db, app
from ..handler.session import login_required, is_auth_in
from ..model import Paid, Member


@app.route('/addPaid', methods=['POST', 'GET'])
@login_required
def add_paid_page():
    if request.method == "GET":
        return render_template("add_paid.html")

    student_id = request.form['student_id']
    get_student = Paid.query.filter(Paid.student_id == student_id).first()
    if get_student is None:
        paid = Paid(student_id)
        db.session.add(paid)
        db.session.commit()
        return render_template("add_paid.html", msg=student_id+"已经添加成功")

    return render_template("add_paid.html", msg="学号:"+student_id+"已经存在！")


