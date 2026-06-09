from flask import Flask, render_template 

app = Flask(_name_)

@app.route('/')
def inicio():
        nome = "Turma de Programação"
        curso = "Python = HTML"

        return render _template(
            'index.html',
            nome = nome,
            curso = curso
        )

@app.route('/sobre')        
def sobre():
    return """
    <h1>Sobre a Turma</h1>
    <p>Esse projeto foi criado usando Python e HTML.</p>
    <a href="/">Voltar para o início</a>
    """

if _name_ =='_main_':
    app.run(host='0.0.0.0', port=3000, debug=True)