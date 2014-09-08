rest-tervehdys
==============

Ääriyksinkertainen REST-palvelu Pythonilla

## Ajo-ohjeet

### Käynnistä palvelu

Tiedostossa `palvelu.py` on määritelty yksinkertainen tervehdyspalvelu. Sen saa ajoon suorittamalla:

    python palvelu.py
    
Palvelu sisältää "tervehdys-resursseja", joiden URI on muotoa

    http://localhost:8080/tervehdys/<NIMI>

Voi testata vaikka curl-työkalulla

    curl -i -X GET http://localhost:8080/tervehdys/Ahto
    

### Suorita asiakas

Palvelun ollessa käynnissä

    python asiakas.py
    
tulostaa jotain tällaista:

    Vastaus: Moi Antti!
