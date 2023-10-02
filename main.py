import cv2
from pyzbar.pyzbar import decode
import json

# Kamera inicializálása
cap = cv2.VideoCapture(0)

# Változó az adat tárolásához
QR_beolvasott = None

while QR_beolvasott is None:
    # Kamera képkockájának olvasása
    ret, frame = cap.read()

    # QR-kódok felismerése
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        # QR-kód adatainak kinyerése és elmentése a változóba
        QR_beolvasott = obj.data.decode('utf-8')
        break  # Azonnal kilépünk, ha találtunk egy QR-kódot

    # Képernyőn megjelenítés
    cv2.imshow('QR Code Scanner', frame)

    # Kilépés a q gomb lenyomásával
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kapcsolat megszakítása és ablak bezárása
cap.release()
cv2.destroyAllWindows()

# Ha van beolvasott QR-kód
if QR_beolvasott is not None:
    print(f'A beolvasott jegy: {QR_beolvasott}')

    # JSON fájlba mentés
    data = {
        "nev": "Kiss Elemer",
        "megye": "Pest varmegye",
        "ervenyesseg": "2023.10.31",
        "azonosito": "00001"
    }

    with open('buszberlet.json', 'w') as json_file:
        json.dump(data, json_file)
        print("Az adatok JSON fájlba mentve.")
else:
    print('Nem találtam azonosítót')
