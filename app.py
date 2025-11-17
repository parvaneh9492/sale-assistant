from flask import Flask, request, jsonify
from flask_cors import CORS
import re, json

app = Flask(__name__)
CORS(app)

try:
    with open("intents.json", "r", encoding="utf-8") as f:
        FAQ = json.load(f)
except:
    FAQ = {}

def get_response(user_text):
    text = user_text.lower()

    # price or cost
    if any(k in text for k in ["price", "cost", "how much", "phone price"]):
        return FAQ.get("price", "Phone prices depend on the model and storage. Please tell me the exact model 😊")

    # availability
    if any(k in text for k in ["available", "availability", "in stock", "stock"]):
        return FAQ.get("availability", "To check availability, please tell me the phone model 📱")

    # warranty
    if any(k in text for k in ["warranty", "guarantee"]):
        return FAQ.get("warranty", "All phones come with the Apple official warranty ✅")

    # delivery
    if any(k in text for k in ["delivery", "shipping", "delivery time"]):
        return FAQ.get("delivery", "Delivery usually takes 1–2 days in the UAE 🚚")

    # payment
    if any(k in text for k in ["payment", "pay", "payment method"]):
        return FAQ.get("payment", "You can pay by card, PayPal, or cash on delivery 💳")

    # phone models
    m = re.search(r"(iphone|samsung|xiaomi|huawei|oppo|galaxy|pixel)", text)
    if m:
        return f"For {m.group(1).capitalize()}, please tell me the storage size and color so I can give you the exact price 📞"

    # fallback
    return FAQ.get(
        "default",
        "Hello 👋 I'm the EmiratePhones assistant. I can help you with phone prices, availability, and delivery."
    )

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    reply = get_response(user_msg)

    return app.response_class(
        response=json.dumps({"reply": reply}, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )


@app.route("/health")
def health():
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
