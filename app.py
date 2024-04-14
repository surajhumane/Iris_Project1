from flask import Flask, request,render_template
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iris.html')

@app.route('/get_data', methods = ['POST'])
def model_prediction():
    data = request.form 
    print(data)

    model = pickle.load(open(r'C:\Users\DELL\OneDrive\Desktop\Model\model.pkl','rb'))
    print(model)

    user_data = [[float(data['x1_sepal_length']),
                  float(data['x2_sepal_width']),
                  float(data['x3_petal_length']),
                  float(data['x4_petal_width'])
                  ]]
    
    print(user_data)


    result = model.predict(user_data)

    print(result)

    target = ['setosa', 'versicolor', 'virginica']

    print(f"prediction = {target[result[0]]}")


    return target[result[0]]


if __name__ == "__main__":
    app.run(debug=True)