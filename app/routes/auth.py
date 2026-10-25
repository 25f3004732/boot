from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        email = request.form.get('email', "").strip().lower()   
        password = request.form.get('password', "").strip()

        if not email or not password:
            flash("Please fill in all fields", "danger")
            return render_template('/auth/login.html', message="Please provide both email and password.")

        if user and user.check_password(password):
            return render_template('/auth/login.html', message="Login Successful")

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return render_template()
    return render_template('/auth/login.html', message="Login Successful")

@auth.route('/register/customer')
def register_customer():
    if request.method == 'POST':
        name = request.form.get('name', "").strip()
        email = request.form.get('email', "").strip().lower()
        password = request.form.get('password', "").strip()

        if not name or not email or not password:
            flash("Please fill in all fields", "danger")
            return render_template('/auth/register_customer.html', message="Please provide all required fields.")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered", "danger")
            return render_template('/auth/register_customer.html', message="Email already registered.")

        new_user = User(name=name, email=email, role='customer')
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('auth.login'))
    return render_template('/auth/register_customer.html')

@auth.route('/register/professional')
def register_professional():
    return render_template('/auth/register_professional.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('views.home'))