from flask import render_template, redirect, url_for, session

def register_side_routes(app):

    # =========================
    # ロト殿
    # =========================
    @app.route("/loto")
    def loto_home():
        if "user" not in session:
            return redirect(url_for("login"))
        return render_template("loto_home.html")

    # =========================
    # ミニロト殿
    # =========================
    @app.route("/loto/miniloto")
    def miniloto_home():
        if "user" not in session:
            return redirect(url_for("login"))
        return render_template("miniloto_home.html")

    # =========================
    # 結果入力ホーム（管理者）
    # =========================
    @app.route("/results/lottery")
    def lottery_results_home():
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return render_template("lottery_results_home.html")

    # =========================
    # ミニロト結果入力
    # =========================
    @app.route("/results/miniloto")
    def miniloto_result_home():
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return render_template("miniloto_result_home.html")

    # =========================
    # ロト6結果入力
    # =========================
    @app.route("/results/loto6")
    def loto6_result_home():
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return render_template("loto6_result_home.html")

    # =========================
    # ロト7結果入力
    # =========================
    @app.route("/results/loto7")
    def loto7_result_home():
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return render_template("loto7_result_home.html")

    # =========================
    # ナンバーズ3結果入力
    # =========================
    @app.route("/results/numbers3")
    def numbers3_result_home():
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return render_template("numbers3_result_home.html")

    # =========================
    # ナンバーズ4結果入力
    # =========================
    @app.route("/results/numbers4")
    def numbers4_result_home():
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return render_template("numbers4_result_home.html")
