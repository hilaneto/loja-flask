
from flask import Blueprint, render_template, session, redirect, url_for
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'cliente'

cliente_bp = Blueprint('cliente', __name__, template_folder=str(TEMPLATE_DIR))    

@cliente_bp.route('/')
def root():
    if 'usuario' not in session:
        return redirect(url_for('login.root'))
    return render_template('pg1_cliente.html')

@cliente_bp.route('/cadastro')
def cadastro():
    if 'usuario' not in session:
        return redirect(url_for('login.root'))
    return render_template('pg2_cadastro.html')

@cliente_bp.route('/extrato')
def extrato():
    if 'usuario' not in session:
        return redirect(url_for('login.login'))
    return render_template('pg3_extrato.html')
