from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
app.config['DEBUG'] = False

# array of dummy products 
# products 0-99 are 'valid products' - this is just a quick way to get dummy data
products = [ str(i) for i in range(100) ]


# put actual file/database IO here
def save_and_update():
    print("Saving data to the excel sheet or database")

# This function makes flask serve up html at http://0.0.0.0:5000/
# the base URL doesn't actually do anything, but when data is encoded in it (like this: http://0.0.0.0:5000/?pn=70&io=out)
# then the html is rendered, using the values that were passed.  In the example given, '70' represents the product ID
# and 'out' is supposed to indicate that the product is being REMOVED from stock.  
@app.route('/', methods=['POST', 'GET'])
def index():
    print('test it out! http://0.0.0.0:5000/?pn=70&io=out')

    if request.method == 'GET':

        # requests.args['pn'] should get the value 70 in the example
        if request.args['pn'] in  products:
            if request.args['io'] == 'in' or request.args['io'] == 'out':
                save_and_update()
                return render_template('io.html', io=request.args['io'], pn=request.args['pn'])
        else:
            # this will happen for any product number outside of 1-99
            return "<h1>Product {} not found in the database...</h1>".format(request.args['pn'])
    return "<h1>Error!</h1>"


@app.route('/qty')
def test():
    print(request.args)
    if request.args['qty']:
        return render_template('qty.html', qty=request.args['qty'], io=request.args['io'], pn=request.args['pn'])
