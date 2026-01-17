from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()
    if "hi" in msg:
        return jsonify({"reply":"Hello!"})
    elif "price" in msg:
        return jsonify({"reply":"Tell me product name"})
    else:
        return jsonify({"reply":"I am learning..."})

app.run()
