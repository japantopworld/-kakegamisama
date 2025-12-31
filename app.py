from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "kagamisama_secret_key"

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "KING1219" and password == "11922960":
            session["user"] = username
            session["is_admin"] = True
            return redirect(url_for("mypage"))

        if username and password:
            session["user"] = username
            session["is_admin"] = False
            return redirect(url_for("mypage"))

    return render_template("login.html")

@app.route("/mypage")
def mypage():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/lottery/results")
def lottery_results_home():
    if "user" not in session:
        return redirect(url_for("login"))
    if not session.get("is_admin"):
        return redirect(url_for("mypage"))
    return render_template("lottery_results_home.html")

def admin_only():
    if "user" not in session:
        return False
    return session.get("is_admin", False)

@app.route("/lottery/results/loto7")
def loto7():
    if not admin_only():
        return redirect(url_for("mypage"))
    return render_template("loto7_result_home.html")

@app.route("/lottery/results/loto6")
def loto6():
    if not admin_only():
        return redirect(url_for("mypage"))
    return render_template("loto6_result_home.html")

@app.route("/lottery/results/miniloto")
def miniloto():
    if not admin_only():
        return redirect(url_for("mypage"))
    return render_template("miniloto_result_home.html")

@app.route("/lottery/results/numbers3")
def numbers3():
    if not admin_only():
        return redirect(url_for("mypage"))
    return render_template("numbers3_result_home.html")

@app.route("/lottery/results/numbers4")
def numbers4():
    if not admin_only():
        return redirect(url_for("mypage"))
    return render_template("numbers4_result_home.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("top"))

# ★変更ここから★
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
# ★変更ここまで★
