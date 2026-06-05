import os
import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# 1. Donne directement la clé entre guillemets (sans os.environ)
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
# On utilise la route 2.5/forecast qui fonctionne parfaitement avec ta clé
URL_API = "https://api.openweathermap.org/data/2.5/forecast"

parametres_meteo = {
    "lat": 55.25,
    "lon": 134.26,
    "appid": os.environ.get("OWM_API_KEY"),
    "units": "metric",  # Pour avoir les degrés Celsius
    "cnt": 4
}

reponse = requests.get(url=URL_API, params=parametres_meteo)
reponse.raise_for_status()

will_rain = False
list_codes = []
data = reponse.json()
print(data)
for forecast in range(0,4):
    if data["list"][forecast]["weather"][0]["id"] < 700:
        will_rain = True
# if will_rain:
if True:
    print("Bring an umbrella!")
    # 2. Transmets-les à Twilio
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain!",
        from_="+19349423039",
        to="+15813096020",
    )

# Dans l'API 2.5/forecast, la liste des prévisions (toutes les 3 heures)
# se trouve dans la clé "list".
# liste_previsions = data["list"]
#
# # Angela veut vérifier les 12 prochaines heures.
# # Comme chaque élément vaut 3 heures, on prend les 4 premiers éléments (4 x 3h = 12h)
# tranche_12h = liste_previsions[:4]
#
# print("--- ANALYSE DES PROCHAINES 12 HEURES ---")
# for prevision in tranche_12h:
#     # On extrait le code météo (ex: 500 pour petite pluie, 800 pour ciel dégagé)
#     id_meteo = prevision["weather"][0]["id"]
#     heure_texte = prevision["dt_txt"]
#
#     print(f"Heure : {heure_texte} | Code Météo : {id_meteo}")
#
#     # La logique d'Angela : Si le code est inférieur à 700, c'est de la pluie/neige/tempête
#     if id_meteo < 700:
#         print("⚠️ Alerte ! Apporte un parapluie, il va pleuvoir !")
