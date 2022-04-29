from flask import Flask, flash, redirect, url_for, render_template, request


app = Flask(__name__)
app.secret_key = "1234"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/output", methods=["POST", "GET"])
def output():
    if request.method == "POST":
        mail = request.form["email"]
        f = open("list.txt", "r")
        for x in f:
            if x.lower() == mail.lower():
                flash("Błąd! Ten email już jest na liście!")
                return render_template("index.html")
            if x != "\n":
                f = open("list.txt", "a")
                f.write("\n")
            print(x)
        f = open("list.txt", "a")
        f.write(mail)
        f.close()
        flash("Sukces! Email został dodany do listy!")
        return render_template("index.html")

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)