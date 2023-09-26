from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'Andresta Ersandy', 'umur':'17tahun'}

 komentar = [

  {

   'penulis': {'nama': 'Nanang'},

   'ucapan': 'hai andresta, artikel yang bagus'

  },

  {

   'penulis': {'nama': 'ucup'},

   'ucapan': 'artikel ini cukup membantu saya'

  }

 ]

 return render_template('index.html', title='Beranda', orang=orang, komentar=komentar)