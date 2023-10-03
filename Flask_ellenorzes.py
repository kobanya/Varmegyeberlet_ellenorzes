from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Példányosítjuk az eladott berletek listát
eladott_berletek = ["000001-20231031-PM" , "000002-20230912-PM", "000002-20231112-PM", "000002-20231112-OB"]

@app.route('/ellenorzes', methods=['POST'])
def ellenorzes():
    try:
        # Megkapjuk a JSON adatot a kérésből
        data = request.get_json()

        # Kinyerjük az azonosítót
        azonosito = data.get('azonosito', '')

        # Ellenőrizzük, hogy az azonosító és a dátum érvényesek-e
        if ervenyes_azonosito(azonosito):
            eredmeny = {"status": "ÉRVÉNYES"}
        else:
            eredmeny = {"status": "ÉRVÉNYTELEN"}

        return jsonify(eredmeny)

    except Exception as e:
        return jsonify({"error": str(e)})

def ervenyes_azonosito(azonosito):
    try:
        # Ellenőrizzük, hogy az azonosító szerepel-e az eladott_berletek listában
        if azonosito not in eladott_berletek:
            return False

        # Kinyerjük a dátumot az azonosítóból (az első 8 karakter)
        datum_str = azonosito.split('-')[1]
        ev_str = datum_str[:4]
        honap_str = datum_str[4:6]
        nap_str = datum_str[6:8]

        # Konvertáljuk a dátum részeket számokká
        ev = int(ev_str)
        honap = int(honap_str)
        nap = int(nap_str)

        # Az aktuális dátum
        mai_datum = datetime.now().date()

        # Ellenőrizzük, hogy a dátum érvényes-e
        if mai_datum.year < ev or (mai_datum.year == ev and mai_datum.month < honap) or (mai_datum.year == ev and mai_datum.month == honap and mai_datum.day <= nap):
            return True

        return False

    except Exception as e:
        return False

if __name__ == '__main__':
    app.run(debug=True)
