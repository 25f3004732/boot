from flask import Blueprint, render_template 

views = Blueprint('views', __name__)

@views.route('/')
def home(): 
    user = 'Pavan'
    age = 20
    return render_template('home.html', user=user, age=age)