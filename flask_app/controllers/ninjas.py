from flask_app import app

from flask import render_template, request, redirect

from flask_app.models.ninja_model import Ninja

from flask_app.models.dojo_model import Dojo


# ------  CREATE - RENDERS THE FORM  ------
@app.route("/ninja")
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos=dojos)

# ----  CREATE - POST ROUTE - SENDS IN DATA  ----
@app.route("/ninja/create", methods = ["POST"])
def create_ninja():
    new_data = {**request.form}
    print("ninja_post_data", new_data)
    dojo_id = Ninja.create(new_data)
    return redirect("/dojo/"+f"{request.form['dojo_id']}")







