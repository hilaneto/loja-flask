
from flask import Flask

from routes.home import home_bp
from routes.usuario import usuario_bp
from routes.cliente import cliente_bp
from routes.produto import produto_bp
from routes.venda import venda_bp
from routes.login import login_bp
from routes.erros import erros_bp

app = Flask(__name__)

app.secret_key = '1553'

# Página principal
app.register_blueprint(login_bp)

# Módulos
app.register_blueprint(home_bp,    url_prefix='/home')
app.register_blueprint(usuario_bp, url_prefix='/usuario')
app.register_blueprint(cliente_bp, url_prefix='/cliente')
app.register_blueprint(produto_bp, url_prefix='/produto')
app.register_blueprint(venda_bp,   url_prefix='/venda')
app.register_blueprint(erros_bp,   url_prefix='/erros')

if __name__ == '__main__':
    app.run(debug=True, port=5153)
