# Varmegyeberlet_ellenorzes

Feladat :   Készits programot amely ellenőrzi kliens által beolvasott a vármegyebérlet QR kódjának érvényességét egy köszponti szerveren.<BR>
             A  vármegyebérlet a rajta feltüntetett vármegyében jogosít utazásra. Annak határain kívül érvénytelen. <BR>
             A vármegyebérlet a feltüntetett időszakra érvényes.<BR>
             A vármegyebérlet azonosítójának szerepelnie kell a szerveren tárolt adatbázisban <BR><BR><BR>
             A területi érvényességet a járműre szerelt fedélzeti eszköz ellenőrzi. <BR>
             Amennyibe a jármű a bérlet érvényességi területén kívül közlekedik, a fedélzeti eszköz a bérletet azonnal elutasítja, nem küldi tovább a központi szerverre ellenőrzésre<BR>
             Amennyiben a bérlet az adott területen érvényes, annak azonosítóját a kliens API-n keresztül elküldi további ellenőrzésre.<BR>
             A szerveren összevtjük az API-n érkezett adatokat a tárolt adatokkal és az aznapi dátummal!  <BR>
             Amennyiben a bérlet érvényességi ideje a mai dátum előtti időpont, úgy a bérlet érvénytelen.
             Amennyiben a dátum és a tárolt adatok megegyeznek  API- n keresztüli válsz: " ÉRVÉNYES"
             A járműfedélzeti egységen megjelenik az "ÉRVÉNYES" felirat
