import requests

# Vaihdetaan kohde sellaiseen, joka ei estä botteja
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_hae_yksi_kayttaja():
    # Haetaan käyttäjä ID:llä 1
    response = requests.get(f"{BASE_URL}/users/1")
    
    # Tarkistetaan että haku onnistui
    assert response.status_code == 200
    
    # Tarkistetaan data
    data = response.json()
    # Tässä APIssa käyttäjän 1 nimi on aina "Leanne Graham"
    assert data['name'] == "Leanne Graham"

def test_luo_uusi_kayttaja():
    # Luodaan uusi
    uusi = {
        "name": "Testaaja",
        "username": "Koodari",
        "email": "testi@esimerkki.com"
    }
    
    response = requests.post(f"{BASE_URL}/users", json=uusi)
    
    # JSONPlaceholder palauttaa 201 (Created)
    assert response.status_code == 201
    
    # Tulostetaan ID varmistukseksi
    print("\nLuotu ID:", response.json()['id'])