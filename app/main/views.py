from locale import currency
from flask import render_template, request
from . import main
from .forms import Currency
from ..models import User
from flask_login import login_required,current_user
from .. import db
from ..requests import convert_currency

@main.route('/', methods=['GET', 'POST'])
def index():
    """
    Index view function that returns the index html page. Which is the homepage.
    """
    title = 'hello welcome to THE CURRENCY '


    
    form = Currency()

    if form.validate_on_submit():
        amount = form.amount.data
        amount = float(amount)
        from_c = form.from_c.data
        to_c = form.to_c.data
        response = convert_currency(from_c,to_c)
        rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
        rate = float(rate)
        result = rate * amount
        from_c_code = response['Realtime Currency Exchange Rate']['1. From_Currency Code']
        from_c_name = response['Realtime Currency Exchange Rate']['2. From_Currency Name']
        to_c_code = response['Realtime Currency Exchange Rate']['3. To_Currency Code']
        to_c_name = response['Realtime Currency Exchange Rate']['4. To_Currency Name']
        time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
    return render_template('home.html', result=round(result, 2), amount=amount,
								from_c_code=from_c_code, from_c_name=from_c_name,
								to_c_code=to_c_code, to_c_name=to_c_name, time=time)

   
