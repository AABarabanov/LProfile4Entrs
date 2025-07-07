from flask import Flask, render_template, request, redirect, url_for


def greetings():
    print("┌─────────────────────────────┐")
    print("│                             │")
    print("│         LehaProfile         │")
    print("│     (for Entrepreneurs)     │")
    print("│           • 1.0 •           │")
    print("|                             |")
    print("└─────────────────────────────┘\n")


app = Flask(__name__)

# Данные профиля
profile = {
    "personal": {
        "name": "",
        "age": 0,
        "phone": "",
        "email": "",
        "postal_code": "",
        "postal_address": "",
        "additional_info": "",
    },
    "business": {
        "ogrnip": "",
        "inn": "",
        "payment_account": "",
        "bank": "",
        "bik": "",
        "correspondent_account": "",
    },
}


def validate_ogrnip(ogrnip):
    return len(ogrnip) == 15 and ogrnip.isdigit()


def validate_payment_account(account):
    return len(account) == 20 and account.isdigit()


@app.route("/")
def main_menu():
    return render_template("main_menu.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_menu():
    if request.method == "POST":
        section = request.form.get("section")
        if section == "personal":
            return redirect(url_for("edit_personal"))
        elif section == "business":
            return redirect(url_for("edit_business"))
    return render_template("edit_menu.html")


@app.route("/edit/personal", methods=["GET", "POST"])
def edit_personal():
    if request.method == "POST":
        profile["personal"] = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "phone": request.form["phone"],
            "email": request.form["email"],
            "postal_code": request.form["postal_code"],
            "postal_address": request.form["postal_address"],
            "additional_info": request.form["additional_info"],
        }
        return redirect(url_for("main_menu"))
    return render_template("edit_personal.html", data=profile["personal"])


@app.route("/edit/business", methods=["GET", "POST"])
def edit_business():
    if request.method == "POST":
        profile["business"] = {
            "ogrnip": request.form["ogrnip"],
            "inn": request.form["inn"],
            "payment_account": request.form["payment_account"],
            "bank": request.form["bank"],
            "bik": request.form["bik"],
            "correspondent_account": request.form["correspondent_account"],
        }
        return redirect(url_for("main_menu"))
    return render_template("edit_business.html", data=profile["business"])


@app.route("/view", methods=["GET", "POST"])
def view_menu():
    if request.method == "POST":
        view_type = request.form.get("view_type")
        if view_type == "personal":
            return render_template("view_personal.html", data=profile["personal"])
        elif view_type == "full":
            return render_template(
                "view_full.html",
                personal=profile["personal"],
                business=profile["business"],
            )
    return render_template("view_menu.html")


if __name__ == "__main__":
    greetings()
    app.run(debug=True)
