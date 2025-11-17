📦 Sale Assistant

A lightweight and fast Flask-based chatbot API designed to help online stores automatically answer customer questions such as product pricing, availability, delivery time, warranty, and payment details.

This chatbot works perfectly as a floating chat widget inside WordPress or any other website and can be deployed 100% free using Render.

🚀 Features

✓ Fast REST API built with Flask

✓ Supports CORS for WordPress integration

✓ Simple rule-based natural language responses

✓ Reads replies from intents.json

✓ Detects phone models using regex

✓ 24/7 uptime with Render Free Tier

✓ Works with any custom HTML/JS chat widget

✓ Very easy to customize and extend


📁 Project Structure

sale-assistant/

│── app.py                # Main Flask app
│── intents.json          # Predefined bot responses
│── requirements.txt      # Dependencies
│── Procfile              # Render/Gunicorn entry point
│── README.md             # Documentation
│── LICENSE               # MIT License


🧠 How It Works

POST /api/chat

Send a user message → get a bot reply.

Request:

{
  "message": "iphone price"
}

Response:

{
  "reply": "Phone prices depend on the model and storage. Please tell me the exact model 😊"
}

GET /health

Returns:

ok 

Used by Render for health checks and uptime monitoring.

🔧 Tech Requirements

flask

flask-cors

gunicorn

Procfile file:

web: gunicorn app:app
