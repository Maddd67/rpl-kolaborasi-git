from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

def salam_waktu(jam):
    """Mengembalikan salam berdasarkan jam (0-23)."""
    if 4 <= jam < 11:
        return "Selamat pagi"
    elif 11 <= jam < 15:
        return "Selamat siang"
    elif 15 <= jam < 18:
        return "Selamat sore"
    else:
        return "Selamat malam"

@app.route("/", methods=["GET", "POST"])
def beranda():
    nama = ""
    if request.method == "POST":
        # Mengambil input nama, memotong spasi, dan membatasi maksimal 50 karakter (Validasi Server-Side - Latihan Mandiri 2)
        nama = request.form.get("nama", "").strip()[:50]
    
    sekarang = datetime.now()
    return render_template(
        "index.html", 
        nama=nama, 
        waktu=sekarang.strftime("%d-%m-%Y %H:%M:%S"), 
        salam=salam_waktu(sekarang.hour)
    )

@app.route("/tentang")
def tentang():
    """Halaman tentang pembuat aplikasi (Latihan Mandiri 1)."""
    return render_template("tentang.html")

if __name__ == "__main__":
    app.run(debug=True)