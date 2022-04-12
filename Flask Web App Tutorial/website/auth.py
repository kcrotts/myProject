from flask import Blueprint, render_template

auth = Blueprint('auth', __name__) #blueprint for flask app, defines blue print

@auth.route('/about_us')
def about_us():
    return render_template("about_us.html")


# If we need more templates, use this format:  
@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

