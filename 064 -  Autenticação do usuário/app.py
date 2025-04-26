from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'chave-secreta-da-geovanna'  # Pode ser qualquer string segura

# Simulando banco de dados
USERS = {
    'admin': '1234',
    'geovanna': 'nunes2025',
    'ricardo' : '123456'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in USERS and USERS[username] == password:
            session['username'] = username
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Você precisa estar logado para acessar.', 'warning')
        return redirect(url_for('login'))

    return render_template('dashboard.html', username=session['username'])


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
