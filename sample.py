from flask import Flask,request,jsonify
import calculations

app=Flask(__name__)


@app.route('/add')
def add():
    input_data=request.form 
    print('the data is -->>',input_data)
    
    a=int(input_data['a'])
    b=eval(input_data['b'])
    result=calculations.add1(a,b)
    return jsonify({'result':f'the addition is {result}'})

if __name__=="__main__":
    app.run(debug=True)
    