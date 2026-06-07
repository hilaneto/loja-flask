
from flask import Blueprint, render_template, session, redirect, url_for
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates' / 'home'

home_bp = Blueprint('home', __name__, template_folder=str(TEMPLATE_DIR))

@home_bp.route('/')
def root():
    print(session)
    if 'usuario' not in session:
        return redirect(url_for('login.root'))

    return render_template('pg0_home.html')
