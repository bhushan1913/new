from flask import Flask ,request,jsonify
import calculations
app=Flask(__name__)

@app.route('/keep')
def keep():
    return 'keep trying brooo'
@app.route('/addition',methods=['GET'])
def addition():
    input_data = request.form
    print('Input Data :', input_data)
    
    a = int(input_data['a'])
    b = eval(input_data['b'])
    result = calculations.add1(a,b)
    return jsonify({'Result': f'Addition of {a} and {b} is {result}.'})

if __name__=="__main__":
    app.run(debug=True)