import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_sql_injection_yritys():
    """
    Tietoturvatesti: Yritetään syöttää SQL-komentoja nimen tilalle.
    Tavoite: Palvelin EI saa kaatua (500 Internal Server Error).
    """
    
    # Tämä on klassinen "Little Bobby Tables" -hyökkäysmerkkijono
    # Jos palvelin on koodattu huonosti, se saattaisi tuhota tietokannan.
    paha_payload = {
        "name": "Robert'); DROP TABLE Students;--",
        "username": "hacker",
        "email": "hacked@example.com"
    }
    
    print(f"\n[SECURITY] Lähetetään hyökkäys: {paha_payload['name']}")
    
    response = requests.post(f"{BASE_URL}/users", json=paha_payload)
    
    # Analyysi
    print(f"Palvelimen vastaus: {response.status_code}")
    
    # 1. Palvelin ei saa kaatua (500 = Critical Failure)
    assert response.status_code != 500, "CRITICAL: Palvelin kaatui SQL-injektiosta!"
    
    # 2. Oikeassa elämässä toivoisimme koodia 400 (Bad Request).
    # Mutta JSONPlaceholder on "tyhmä" testi-API, se luultavasti hyväksyy kaiken (201).
    # Siksi vain varmistamme, että se on edes hengissä.
    assert response.status_code in [201, 400], "Outo vastauskoodi"

def test_laheta_jattilainen_data():
    """
    Fuzzing-testi: Lähetetään valtava määrä roskaa.
    Tavoite: Testata puskurin ylivuotoa (Buffer Overflow) tai palvelun hidastumista.
    """
    roska_data = "A" * 5000  # Viisi tuhatta A-kirjainta
    
    payload = {
        "name": roska_data,
        "email": "test@test.com"
    }
    
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    # Varmistetaan, että vastausaika on järkevä (alle 2 sekuntia)
    # response.elapsed.total_seconds() kertoo kauanko kesti
    aika = response.elapsed.total_seconds()
    print(f"\nVastausaika jättidatalla: {aika} sekuntia")
    
    assert aika < 2.0, "WARNING: Palvelin tukehtui isoon dataan!"
    assert response.status_code != 500