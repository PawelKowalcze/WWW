from flask import render_template, redirect, url_for, request, flash
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "password":
            flash('Zalogowano pomyślnie!', 'success')
            return redirect(url_for('dashboard.home'))
        else:
            flash('Błędne dane logowania.', 'danger')

    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        flash(f'Rejestracja zakończona sukcesem dla użytkownika {username}', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')