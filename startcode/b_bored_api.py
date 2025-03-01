# Gebruik de bored api om een JSON-bestand in te lezen: https://www.boredapi.com/api/activity

# De response als json interpreteren kan zo: data = response.json()
import requests
request = requests.get('https://bored.api.lewagon.com/api/activity/')
if request.status_code == 200:
    data = request.json()

    print(data["type"])
else:
    print("Oei! Er is een fout opgetreden! Probeer opnieuw!")