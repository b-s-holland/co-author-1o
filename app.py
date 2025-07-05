from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = "your_api_key_here"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a darkly satirical writing assistant who helps develop cult-themed content with psychologically sharp insights."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
