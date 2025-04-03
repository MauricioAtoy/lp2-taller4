
from reactpy import component, web, html
from reactpy.backend.flask import configure
from flask import Flask
from datos import productos

mui = web.module_from_template("react", "@mui/material",  fallback=" ⏳")
Container = web.export(mui, "Container")

@component
def App():
    return Container(
        {"maxWidth": "md"},
        html.h1 ("Hola, mundo")
    )

app = Flask(__name__)
configure(app, App)
app.run(host='0.0.0.0', debug=True)
