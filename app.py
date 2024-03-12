from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurace.db'  # Nastavíme URI pro naši SQLite databázi
db = SQLAlchemy(app)
app.app_context().push()

# Definice modelu pro tabulku Stoly
class Stoly(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primární klíč ID
    pocet_mist = db.Column(db.Integer)
    zamluveno = db.Column(db.Boolean, default=False)
    datum_zacatek = db.Column(db.DateTime)
    datum_konec = db.Column(db.DateTime)

# Definice modelu pro tabulku Zakaznik
class Zakaznik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jmeno = db.Column(db.String(50))
    prijmeni = db.Column(db.String(50))
    tel = db.Column(db.String(20))

# Definice modelu pro tabulku Objednávka
class Objednavka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_zakaznika = db.Column(db.Integer, db.ForeignKey('zakaznik.id'))
    zakaznik = db.relationship('Zakaznik', backref='objednavky')
    datum_cas_objednavky = db.Column(db.DateTime)
    stav_objednavky = db.Column(db.String(50))
    celkova_cena = db.Column(db.Float)

#db.create_all()
    
# Funkční vytvoření databáze pomocí pythonu
    
# Zatím nefunguje zápis do databáze

@app.route('/', methods=['GET', 'POST'])
def index():
    rows = 5  # Number of rows
    cols = 5  # Number of columns
    
    if request.method == 'POST':
        # Get the state of buttons from the form
        button_states = request.form.getlist('button')
        checked_indexes = [int(index) for index, state in enumerate(button_states) if state == 'on']

        return render_template('index.html', rows=rows, cols=cols, checked_indexes=checked_indexes)

    return render_template('index.html', rows=rows, cols=cols)

if __name__ == '__main__':
    app.run(debug=True)



















"""from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    rows = 5  # Number of rows
    cols = 5  # Number of columns
    
    if request.method == 'POST':
        # Get the state of buttons from the form
        button_states = request.form.getlist('button')
        checked_indexes = [int(index) for index, state in enumerate(button_states) if state == 'on']

        return render_template('index.html', rows=rows, cols=cols, checked_indexes=checked_indexes)

    return render_template('index.html', rows=rows, cols=cols)

"""




#def index():
#    if request.method == 'POST':
#        name = request.form['name'] #name v závorce je name z formu v index.html
#        date = request.form['date']
#        number = request.form['pocetLidi']
#        return  f'<h1>Vaše objednávka</h1><br> Jméno: {name}<br>' +  f' Datum {date}<br>'  + f' Počet lidí {number}<br>'
#    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
