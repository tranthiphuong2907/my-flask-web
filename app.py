from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

# Đọc dữ liệu tarot
with open("tarot_cards.json", "r", encoding="utf-8") as f:
    tarot_cards = json.load(f)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    # Chọn 3 lá bài ngẫu nhiên
    selected_cards = random.sample(tarot_cards, 3)
    return render_template("result.html", cards=selected_cards)

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
