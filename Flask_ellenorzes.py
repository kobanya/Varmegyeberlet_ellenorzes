from flask import Flask, request, jsonify

app = Flask(__name__)

# Példányosítjuk az eladott berletek listát
eladott_berletek = ["000001"]



@app.route('/ellenorzes', methods=['POST'])
def ellenorzes():
    try:
        # Megkapjuk a JSON adatot a kérésből
        data = request.get_json()

        # Ellenőrizzük, hogy az azonosító szerepel-e az eladott_berletek listában
        if data['azonosito'] in eladott_berletek:
            eredmeny = {"status": "ÉRVÉNYES"}
        else:
            eredmeny = {"status": "ÉRVÉNYTELEN"}

        return jsonify(eredmeny)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
