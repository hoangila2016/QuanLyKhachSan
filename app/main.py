from app import app, request, render_template,dao


@app.route("/")
def xin():
    a = dao.get_category()
    b = dao.get_product()
    return render_template("index.html", Category = a, Products = b)


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]
        if account == "admin" and password == "123":
            return render_template("login.html", account = account, password= password)
        else:
            return "false"
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
