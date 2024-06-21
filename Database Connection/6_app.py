import numpy as np
from flask import Flask, request, render_template,jsonify
import joblib

# Create flask app
flask_app = Flask(__name__)
model = joblib.load(open("trained_model_rf.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index1.html")

@flask_app.route("/predict/api", methods = ["POST"])
def predict_api():
    data1 = request.form['Sepal_Length']
    data2 = request.form['Sepal_Width']
    data3 = request.form['Petal_Length']
    data4 = request.form['Petal_Width']
    arr = np.array([[data1, data2, data3, data4]])

    # float_features = [float(x) for x in request.form.values()]
    # arr = [np.array(float_features)]


    pred = model.predict(arr)

    return jsonify({'prediction': pred.tolist()})
    
    
@flask_app.route("/predict", methods = ["POST"])
def predict():
    pred = predict_api()
    pred = pred.response

    return render_template("index1.html", prediction_text = "The flower species is {}".format(pred[0].decode('utf8')))

if __name__ == "__main__":
    flask_app.run(debug=True)
    
    