from flask import Flask, request,jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return "Flask api is running Sucessfully !"

@app.route('/predict',methods = ['POST'])
def predict():
    data = request.get_json()
    age = data.get('age',0)
    income = data.get('income',0)
    result = "Approved" if income > 30000 else "Denied"
    return jsonify({"result":result})





