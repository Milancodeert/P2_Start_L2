# Maak een programma dat:
# - De naam van de gebruiker vraagt.
# - De naam van de gebruiker doorstuurt naar de API.
# - Een tekstje print met de naam en de voorspelde leeftijd.
import requests
naam_aanvraag = input("Wat is je naam? ")
response = requests.get(
    url = "https://api.agify.io/",
    params={"name": naam_aanvraag}
)
if response.status_code == 200:
    data = response.json()
    print(data["age"])
else:
    print("Oei! Er ging iets mis!")
