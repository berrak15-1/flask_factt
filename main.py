from flask import Flask
import random
app = Flask(__name__)
@app.route("/")

def hello_world():
    return ''' 
    <h1>Hello World</h1>
    <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle</a>
    
    <a href="/yazı_tura">Yazı tura</a>
    '''
@app.route("/rastgele_gercek") 


def random_fact():

    facts=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, şebeke kapsama alanı dışında yoğun stres yaşar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduklarını düşünüyor.",
"2019'da yapılan bir araştırmaya göre, insanların %60'ı işten sonra 15 dakika içinde iş mesajlarına yanıt veriyor.",
]

    seçilen=random.choice(facts)
    return f'<h1> RASTGELE GERÇEK </h1> {seçilen} <a href="/">Anasayfa </a>'
#########

    

@app.route("/yazı_tura") 


def yazı_tura():
    yazıtura = ["yazı", "tura"]
    secim = random.choice(yazıtura)
    return f'<h1> YAZI MI TURA MI </h1> {secim} <a href="/">Anasayfa </a>'



if __name__ == "__main__":

    app.run(debug=True)
