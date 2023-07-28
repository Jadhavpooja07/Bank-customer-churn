from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import BankChurn
import config
import traceback
app = Flask(__name__)

@app.route('/bank')
def home1():
    
    return render_template('bank.html')

@app.route('/churn', methods = ['GET', 'POST'])
def bank_churn():
    try:
        if request.method == 'GET':
            print("+"*50)
            data = request.args.get
            print("Data :",data)
            credit_score = data('credit_score')
            gender = data('gender')
            age = data('age')
            tenure = data('tenure')
            balance = data('balance')
            products_number = data('products_number')
            credit_card = data('credit_card')
            active_member = data('active_member')
            estimated_salary = data('estimated_salary')
            country = data('country')

            Obj = BankChurn(credit_score,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country)
            churn = Obj.get_churn()
            
            return render_template('bank.html', prediction = churn)




        elif request.method == 'POST':
            print("*"*40)
            data = request.form.get
            print("Data :",data)
            credit_score = data('credit_score')
            gender = data('gender')
            age = data('age')
            tenure = data('tenure')
            balance = data('balance')
            products_number = data('products_number')
            credit_card = data('credit_card')
            active_member = data('active_member')
            estimated_salary = data('estimated_salary')
            country = data('country')
            country = data('country')

            Obj = BankChurn(credit_score,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country)
            churn = Obj.get_churn()
            
            
            return render_template('bank.html', prediction = churn)

    except:
        print(traceback.print_exc())
        return redirect(url_for('bank'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)