from flask import render_template, request, flash, redirect, url_for

from .. import db, app
from ..model import Member, Paid


@app.route("/register", methods=['POST', 'GET'])
def register_page():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        member_name = request.form['member_name']
        student_id = request.form['student_id']
        member_sex = request.form['member_sex']
        member_college = request.form['member_college']
        member_WeChat = request.form['member_WeChat']
        member_QQ = request.form['member_QQ']
        member_telephone = request.form['member_telephone']
        member_political_status = request.form['member_political_status']
        member_email = request.form['member_email']
        member_birthday = request.form['member_birthday']
        new_member = Member.query.filter(Member.student_id == student_id).first()

        if new_member is None:
            paid = Paid.query.filter(Paid.student_id == student_id).first()
            if paid is None:
                flash("尚未缴费，请联系工作人员处理！")
                return redirect(url_for("register_page"))
            member = Member(member_name, str(student_id), member_sex, member_college, member_WeChat,
                            str(member_QQ), str(member_telephone), member_political_status, member_email,
                            member_birthday)
            db.session.add(member)
            db.session.commit()
            flash(member_name + "恭喜，注册成功，欢迎加入军事爱好者协会")
            return redirect(url_for('page_index'))
        else:
            flash("学号已经注册!", )
            return redirect(url_for('register_page'))
