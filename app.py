# Punto de entrada principal, instancia de Flask y rutas importadas

from flask import Flask
from db import close_connection
from routes.user_routes import user_bp


app = Flask(__name__)
app.teardown_appcontext(close_connection)

# Registro del blueprint
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)