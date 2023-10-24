from flask import Flask,render_template, request
import pymongo
import bcrypt

app=Flask(__name__)

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["Quiz"]
collection=db['Login']


@app.route("/")
def home():
    return render_template("home.html")

# login Page
@app.route("/login", methods=['GET', 'POST'])
def login():

    return render_template("login.html")

@app.route("/forgot_password")
def forgot_password():
    return render_template('forgot-password.html')


@app.route("/admin_dashboard")
def admin_dashborad():
    return render_template("index.html")

# Admin Page
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        password = request.form.get("password")
        print(username, password, role)
        # collection.insert_one( {"username":username, "password":password, "role":role} )
        # obj = (collection.find({"username":"abhi"},{"username":1,"_id":0}))
        # for i in (obj):
        uname=collection.find({"username":username},{"username":1,"_id":0})[0]["username"]
        pword=collection.find({"username":username},{"password":1,"_id":0})[0]["password"]
        role1=collection.find({"username":username},{"role":1,"_id":0})[0]["role"]
        print(uname,pword,role1)
        # if collection.find({"username":"abhi"},{"username":1,"_id":0})[0]["username"] == username:
        #     return render_template("index.html")
        # if collection.find({"username":"abhi"},{"password":1,"_id":0})[0]["password"]== password:
        #     return render_template("index.html")
        if uname==username and pword==password and role1==role:
            return render_template("index.html")
    
    return "Access denied"

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/inbox")
def inbox():
    return "abhijeet"


@app.route("/add_user",methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        username = request.form.get("username")
        email=request.form.get('email')
        role = request.form.get("role")
        password = request.form.get("password")
        print(username, password, role,email)
        collection.insert_one( {"email":email,"username":username, "password":password, "role":role} )
        
    
    return render_template("add-user.html")


app.run(debug=True)