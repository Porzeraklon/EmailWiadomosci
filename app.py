from flask import Flask, flash, redirect, session, url_for, render_template, request, jsonify


app = Flask(__name__)
app.secret_key = "1234"

check_list = [

]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/output", methods=['POST', 'GET'])
def output():
    if request.method == "POST":
        
        f = open("check_list.txt", "r")
        for x in f:
            if x != "\n":
                check_list.append(x)
        f.close

        mail = request.form["email"]
        for x in check_list:
            if x != '\n':
                print(x)
                print(x.lower())
                if mail.lower() == x.lower().strip():
                    flash("Błąd! Ten email już jest na liście!")
                    print("nie ma")
                    return render_template("index.html")
                
        f = open("check_list.txt", "a")
        f.write(mail)
        f.write('\n')
        f.close()

        f = open("id_list.txt", "r")
        _id = f.read()
        f.close()

        f = open("id_list.txt", "w")
        _id = int(_id) + 1
        f.write(str(_id))
        f.close()

        mail = "{'mail_id':'" + str(_id) + "','email':'" + mail + "'}"
        print(mail)
        f = open("list.txt", "a")
        f.write(mail + ",")
        f.close

        flash("Sukces! Email został dodany do listy!")

        return render_template("index.html")

    else:
        return render_template("index.html")

    

@app.route("/zaq1@WSXcde3$RFV", methods=['GET'])
def emails():
    email = []
    f = open("list.txt", "r")
    for x in f:
        email.append(x)
    f.close()
    return jsonify(email)

#@app.route("/admin", methods=['POST', 'GET'])
#def admin():
   

if __name__ == "__main__":
    app.run(debug=True)