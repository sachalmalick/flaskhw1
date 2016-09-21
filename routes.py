from flask import Flask
routes=Flask(__name__)

@routes.route("/")
def hello_world():
        return """<a href = "http://localhost:5000/cake"> cake </a>"""


@routes.route("/cake")
def cake():
	return """<a href = "http://localhost:5000/pie"> pie </a>"""
@routes.route("/pie")
def pie():
        return "pie"

if __name__ == "__main__":
	routes.run()

