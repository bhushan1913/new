#pip install flask in the terminal
from flask import Flask, request, jsonify, redirect, url_for
app = Flask(__name__) 
import calculations
import config

################################ HOME API ########################################
@app.route('/')
def welcome():
    return 'Welcome to the flask session.'

################################ API WITH NAME ###################################
@app.route('/happy')
def happy():
    return 'We are happy to be a Data Scientist'

@app.route('/MachineLearning')
def MachineLearning():
    return 'We are learning Machine Learning.'

############################## API WITH VARIABLE #################################
@app.route('/person/<name>')
def person(name):
    return 'Name of the person is ' +name

@app.route('/success/<int:score>')
def success(score):
    return 'Person has passed and marks are ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'Person has failed and marks are ' + str(score)

################################## API WITH REQUESTING VALUES FROM USER ##########################

@app.route('/addition')
def addition():
    input_data = request.form
    print('Input Data :', input_data)
    
    a = int(input_data['a'])
    b = eval(input_data['b'])
    result = calculations.add1(a,b)
    return jsonify({'Result': f'Addition of {a} and {b} is {result}.'})


################################# API FOR REDIRECTING ONE URL TO ANOTHER #################################

@app.route('/result/<int:marks>')
def result(marks):
    res=''
    if marks < 40:
        res ='fail'
    else:
        res ='success'
    return redirect(url_for(res, score=marks)) # res is a variable here, where we are storing the result.


if __name__ == "__main__":
    app.run(debug=True, port=config.PORT_NUMBER)