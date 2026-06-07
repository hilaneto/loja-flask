
from flask import Blueprint, render_template, session, redirect, url_for
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'venda'
venda_bp = Blueprint('venda', __name__, template_folder=str(TEMPLATE_DIR))    

@venda_bp.route('/')
def root():
    if 'usuario' not in session:
        return redirect(url_for('login.root'))
    return render_template('pg1_venda.html')

@venda_bp.route('/devolucao')
def devolucao():
    return render_template('pg2_devolucao.html')
