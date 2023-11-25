
from flask import Flask
from factory import create_app


app: Flask = create_app()
app.run(debug=True,port=1112)