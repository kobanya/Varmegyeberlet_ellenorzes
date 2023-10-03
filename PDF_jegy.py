import cv2
from barcode import decode

# Kamera inicializálása
cap = cv2.VideoCapture(0)

# Változó az adat tárolásához
PDF417_beolvasott = None

while PDF417_beolvasott is None:
    # Kamera képkockájának olvasása
    ret, frame = cap.read()

    # PDF417 kódok felismerése
    barcodes = decode(frame)

    for barcode in barcodes:
        # PDF417 kód adatainak kinyerése és elmentése a változóba
        PDF417_beolvasott = barcode.data
        break  # Azonnal kilépünk, ha találtunk egy PDF417 kódot

    # Képernyőn megjelenítés
    cv2.imshow('PDF417 Code Scanner', frame)

    # Kilépés a q gomb lenyomásával
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kapcsolat megszakítása és ablak bezárása
cap.release()
cv2.destroyAllWindows()

# Ha van beolvasott PDF417 kód
if PDF417_beolvasott is not None:
    print(f'A beolvasott PDF417 kód: {PDF417_beolvasott}')
else:
    print('Nem találtam azonosítót')
