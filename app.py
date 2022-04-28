from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/succes")
def succes():
    return render_template("succes.html")

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        mail = request.form["email"]
        f = open("list.txt", "r")
        for x in f:
            if x.lower() == mail.lower():
                return render_template("error.html")
            print(x)
        f = open("list.txt", "a")
        f.write("\n")
        f.write(mail)
        f.close()
        return redirect(url_for("succes"))

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)