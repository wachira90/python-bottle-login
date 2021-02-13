from bottle import route, run, template, get, post, request, static_file,Bottle ,redirect
# from bottle import Bottle, request, redirect, run
from bottle_login import LoginPlugin

# app = Bottle()
app = Bottle()

app.config['SECRET_KEY'] = 'secret'

login = app.install(LoginPlugin())

@login.load_user
def load_user_by_id(user_id):
    # print("load user",user_id)
    user_id = "wachira"
    # Load user by id here


# Some application views

@app.route("/",method="GET")
def index():
    print("current_user")
    current_user = login.get_user()
    return current_user.name

@app.route('/signout')
def signout():
    # Implement logout
    login.logout_user()
    return redirect('/')

@app.route('/signin')
def signin():
    # Implement login (you can check passwords here or etc)
    user_id = int(request.GET.get('user_id'))
    login.login_user(user_id)
    return redirect('/')

run(host='127.0.0.1', port=50000, debug=True)
# run(host='0.0.0.0', port=80)