import mysql.connector
import geocoder
from flask import Flask, render_template, request
app = Flask(__name__)
# home function to call homepage for user
@app.route("/")
def home():
    return render_template('index.html')


# guide function to call guidelines page for user
@app.route("/guide", methods=['GET', 'POST'])
def guide():
    calamity = request.form['disaster']
    fw = request.form['FW']
    med = request.form['Med']
    note = request.form['note']
    guide.CALAMITY = calamity
    guide.FW = fw
    guide.MED = med
    guide.NOTE = note

    g = geocoder.ip("me")
    my_add = g.address
    guide.Add = my_add

    return render_template('guide.html', Calamity=calamity, FW=fw, Med=med, Note=note)


# display function to call the display page for the responsible authorities
@app.route("/display", methods=['GET', 'POST'])
def display():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="provider1")
    my_cursor = db.cursor()

    my_cursor.execute("SELECT quantity FROM INVENTORY where item='Food & Water'")
    f_qty = 0
    for i in my_cursor:
        f_qty = i[0]

    my_cursor.execute("SELECT quantity FROM INVENTORY where item='Medicines'")
    m_qty = 0
    for i in my_cursor:
        m_qty = i[0]

    return render_template('display.html', Add=guide.Add, Calamity=guide.CALAMITY,
                           FW=guide.FW, Med=guide.MED, Note=guide.NOTE, F=f_qty, M=m_qty)


app.run(debug=True)