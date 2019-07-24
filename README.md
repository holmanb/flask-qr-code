# TOY APP
This is a bare bones toy web server that I made when playing through an imaginary scenario.


## The Scenario
You have an inventory to manage, and want to scan QR codes to manage inventory. You want to encode the product number in the QR code, so that you scan, optionally type a quantity (default to 1), and get prompted by a page indicating success.


## What this code does:
This code doesn't do anything to a database or file (this can easily be added).  All it does is present two different html pages.  One is used to submit the product quantity, and another is used to present a confirmation page.  This makes use of HTTP calls to send data (qty, product number, checkin vs checkout) from the web page to the server.  Before serving up the html page to the browser, flask uses Jinja2 templating to insert values into the html before displaying it back to the user see the files under the `/templates` directory.


## Tech
Python 3.7
Flask 1.0.3
(see requirements.txt for more details)

## QR 
QR Codes can be used to encode many different types of data.  The example here is that a QR code is encoded with a product id and a "direction", either in or out.  When the code is scanned (using a modern smartphone), a browser is opened to the URL encoded in the QR code.  The browser in our example points to http://0.0.0.0:5000/?pn=70&io=out, which tells the server that `pn` (product number) 70 is getting taken `out`.


## Testing & Requirements
This was tested localy and worked both in the browser on my local linux machine (Fedora 30), and using a QR App on my smartphone while connected to the same wifi network and with the correct firewall permissions applied on my desktop.  Obviously the bash `start.sh` (which is just the flask start command) script requires bash, but every other tool used in this project should be cross platform __to the best of my knowledge__.  Install python3.7 and use pip to install Flask and you should be good to go.


## Disclaimer:
This is NOT an example of quality or organizaed code by any means.  This is a __hack job__, __proof of concept__, __toy__ that __might__ possible have some value to some individual (most likely my future self).
