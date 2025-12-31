from flask import Flask, render_template
from ai_logic import predict_miniloto

app = Flask(__name__)

@app.route("/")
def index():
    numbers, score = predict_miniloto("miniloto.csv")
    return render_template(
        "index.html",
        numbers=numbers,
        score=score.head(10)
    )

if __name__ == "__main__":
    app.run(debug=True)
