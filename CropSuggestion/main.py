from flask import Flask
from admin import admin
from farmer import farmer
from public import public
from expert import expert

app=Flask(__name__)
app.secret_key="sss"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(farmer,url_prefix='/farmer')
app.register_blueprint(expert,url_prefix='/expert')
app.run(debug=True,port=5011)

