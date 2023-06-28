from flask_app import app

from flask import render_template, request, redirect

from flask_app.models.dojo_model import Dojo

# HOME PAGE 
@app.route("/")
def index():
    return redirect("/dojos")

# ----  READ ALL / CREATE - RENDERS THE FORM  -----
@app.route("/dojos")
def all_dojos():
    dojos = Dojo.get_all_dojos()
    # print(dojos)
    return render_template("dojos.html", dojos=dojos)

# ----  CREATE - POST ROUTE - SENDS IN DATA  ----
@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    print(request.form)
    Dojo.add_dojo(request.form)
    return redirect("/dojos")

# -----  SHOW ALL NINJAS FOR ONE DOJO  -----
@app.route("/dojo/<int:id>")
def show_dojo_ninjas(id):
    data = {'dojo_id':id}
    one_dojo = Dojo.get_dojo_with_ninjas(data)
    print(one_dojo)
    return render_template("dojo_show.html", one_dojo=one_dojo)
    # (one_dojo variable is passed onto the html)


