
from flask import Blueprint, request, render_template, redirect, url_for, session
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'login'
login_bp = Blueprint('login', __name__, template_folder=str(TEMPLATE_DIR))

USUARIOS = {'Roberto': {'cargo': 'Diretor','nivel': 1,'senha': '123'},
            'Jessica': {'cargo': 'Superintendente','nivel': 2,'senha': '456'},
            'Antonio': {'cargo': 'Gerente','nivel': 3,'senha': '678'},
            'Marcia': {'cargo': 'Analista','nivel': 4,'senha': '912'}}

@login_bp.route('/', methods=['GET', 'POST'])
def root():
    if 'usuario' in session:
        return redirect(url_for('home.root'))

    if request.method == 'POST':
        acao = request.form.get('acao')

        if acao == 'entrar':
            usuario = request.form['usuario']
            senha = request.form['senha']

            if usuario in USUARIOS:
                usuario_logado = USUARIOS[usuario]

                if senha == usuario_logado['senha']:
                    session['usuario'] = usuario
                    session['cargo'] = usuario_logado['cargo']
                    session['nivel'] = usuario_logado['nivel']
                    return redirect(url_for('home.root'))

            return render_template( 'pg0_login.html', erro='Usuário ou senha inválidos!' )

        elif acao == 'sair':
            session.clear()
            return redirect(url_for('login.root'))

    return render_template('pg0_login.html')

@login_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.root'))
