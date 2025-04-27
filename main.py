
from reactpy import component, web, html
from reactpy.backend.flask import configure
from flask import Flask
from datos import productos

mui = web.module_from_template("react", "@mui/material",  fallback=" ⏳")
Container = web.export(mui, "Container")
Grid = web.export(mui, "Grid")
Paper = web.export(mui, "Paper")
Box = web.export(mui, "Box")

def tarjetas(productos):
    def tarjeta(producto):
        return Grid(
            {"item": True, "sm": 6, "md": 4, "lg": 3},
            Paper(
                {"elevation": 4},
                html.img({
                    "src": "https://picsum.photos/id{producto['id']}/400/100",
                    "class_name": "img-fluid",
                    "style": { "width": "100%", "height": "5rem"}
                }),
                Box(
                    {"bgcolor":"background.paper"},
                    html.h1(producto['nombre'])
                ),
            )
        )
    
    return Grid (
        {"container": True, "spacing": "8"},
        [ tarjeta(producto) for producto in productos]
    )
        
@component
def App():
    return Container(
        {"maxWidth": "md"},
        tarjetas(productos)
    )

app = Flask(__name__)
configure(app, App)
app.run(host='0.0.0.0', debug=True)
