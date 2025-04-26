
from reactpy import component, web, html
from reactpy.backend.flask import configure
from flask import Flask
from datos import productos

mui = web.module_from_template("react", "@mui/material",  fallback=" ⏳")
Container = web.export(mui, "Container")
Grid = web.export(mui, "Grid")

@component
def App():
    return Container(
        {"maxWidth": "md"},
        Grid (
            {"container": True, "spacing": "8"},
            Grid(
                {"item": True, "sm": 6, "md": 4, "lg": 3},
                html.h1("producto 1")
            ),
            Grid(
                {"item": True, "sm": 6, "md": 4, "lg": 3},
                html.h1("producto 1")
            ),
            Grid(
                {"item": True, "sm": 6, "md": 4, "lg": 3},
                html.h1("producto 1")
            ),
            Grid(
                {"item": True, "sm": 6, "md": 4, "lg": 3},
                html.h1("producto 1")
            ),
        )
    )

app = Flask(__name__)
configure(app, App)
app.run(host='0.0.0.0', debug=True)
