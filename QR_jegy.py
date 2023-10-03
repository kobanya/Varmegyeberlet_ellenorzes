import cv2
from pyzbar.pyzbar import decode
import requests

# Függvény az API hívásához
def ellenorzes_api(azonosito):
    api_url = "http://localhost:5000/ellenorzes"  # Az API szerver URL-je

    try:
        response = requests.post(api_url, json={"azonosito": azonosito})

        if response.status_code == 200:
            return response.json()
        else:
            return {"status": "HIBA", "message": "Az API hívás sikertelen."}

    except Exception as e:
        return {"status": "HIBA", "message": str(e)}

# Kamera inicializálása
cap = cv2.VideoCapture(0)

# Változó az azonosító szám tárolásához
azonosito = None

# Kérjük meg a járművezetőt, hogy adja meg a vármegyét
varmegye_kod = input("Kérem, adja meg a vármegye kódját (pl. PM): ")

while azonosito is None:
    # Kamera képkockájának olvasása
    ret, frame = cap.read()

    # QR-kódok felismerése
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        # QR-kód adatainak kinyerése és elmentése az azonosito változóba
        azonosito = obj.data.decode('utf-8')
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
if azonosito is not None:
    print(f'A beolvasott azonosító: {azonosito}')

    # Ellenőrizzük, hogy a vármegye kód megegyezik-e az azonosító utolsó két karakterével
    if azonosito[-2:] == varmegye_kod:
        # Elküldjük az azonosítót az API-nak és megkapjuk a választ
        api_response = ellenorzes_api(azonosito)

        if api_response.get("status") == "ÉRVÉNYES":
            print("A bérlet ÉRVÉNYES.")
        else:
            print("Az azonosító érvénytelen.")
    else:
        print("Ebben a vármegyében ÉRVÉNYTELEN.")

else:
    print('Nem találtam azonosítót')
