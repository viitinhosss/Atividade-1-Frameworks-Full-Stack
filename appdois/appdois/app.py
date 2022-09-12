import os
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
app = Flask(__name__)
 

app.config['MYSQL_DATABASE_USER'] = 'root' 
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'inferno'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)
@app.route("/")
def main():
    return render_template('gravacao.html')


@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']

    if nome and cpf and endereço:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            'insert into gravacao (nome, cpf, endereco) VALUES (%s, %s, %s)', (nome, cpf, endereco))
        conn.commit()
    return render_template('gravacao.html')


@app.route('/listar', methods=['POST', 'GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        'select nome, cpf, endereco from gravacao')
    data = fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)
