from flask import Flask, flash, redirect, url_for, render_template, request, jsonify


email_list = [

]

check_list = [

]

app = Flask(__name__)
app.secret_key = "1234"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/output", methods=['POST', 'GET'])
def output():
    if request.method == "POST":
        mail = request.form["email"]
        for x in check_list:
            if x.lower() == mail.lower():
                print("Podany mail: ", mail)
                print("Lista maili: ", check_list)
                flash("Błąd! Ten email już jest na liście!")
                return render_template("index.html")
        
        check_list.append(mail)
        mail = {
            'email': mail
        }
        email_list.append(mail)
        print(email_list)
        flash("Sukces! Email został dodany do listy!")
        return render_template("index.html")

    else:
        return render_template("index.html")

@app.route("/zaq1@WSXcde3$RFV", methods=['GET'])
def emails():
    return jsonify(email_list)

@app.route("/admin", methods=['POST', 'GET'])
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)