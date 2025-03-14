# Bekijk de documentatie voor de free games API: https://www.freetogame.com/api-doc
# Hoe zou je een lijst met games kunnen binnenhalen met de volgende voorwaarden?
# - PC-games
# - Gesorteerd volgens relevantie
import requests
response = requests.get(
    url ="https://www.freetogame.com/api-doc",
params={'platform': 'pc',
        'sort-by': 'relevance'} )

# Bijkomende opdracht:
# Print voor alle pc-games die het woord “world” bevatten, de titel en de game_url.
# Zorg dat het niet gevoelig is aan hoofdletters.