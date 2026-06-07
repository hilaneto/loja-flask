
from flask import Blueprint, render_template, session, redirect, url_for
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'usuario'
usuario_bp = Blueprint('usuario', __name__, template_folder=str(TEMPLATE_DIR))    

@usuario_bp.route('/')
def root():
    #print(session)
    if 'usuario' not in session:
        return redirect(url_for('login.root'))
    if session['nivel'] > 2:
        #return redirect(url_for('home.root', erro='Acesso negado!'))
        return render_template('acesso_negado.html')
    return render_template('pg1_usuario.html')
