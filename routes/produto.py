
from flask import Blueprint, render_template, session, redirect, url_for
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'produto'
produto_bp = Blueprint('produto', __name__, template_folder=str(TEMPLATE_DIR))    

@produto_bp.route('/')
def root():
    if 'usuario' not in session:
        return redirect(url_for('login.root'))
    return render_template('pg1_produto.html')
