from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = "dog" #testing
    return jsonify({"i have predicted : ": prediction})

if __name__ == "__main__":
    app.run(debug=True)