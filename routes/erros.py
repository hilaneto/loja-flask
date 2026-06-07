
from flask import Blueprint, render_template, session, redirect, url_for
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'erros'

erros_bp = Blueprint('erros', __name__, template_folder=str(TEMPLATE_DIR))    
@erros_bp.route('/')
def root():
    if 'erros' not in session:
        return redirect(url_for('erros.root'))
    return render_template('pg1_erros.html')
    