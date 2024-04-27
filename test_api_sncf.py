import requests

def fetch_all_stop_areas(api_key):
    all_stop_areas = []
    url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
    headers = {"Authorization": api_key}
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            all_stop_areas.extend(data.get('stop_areas', []))
            # Passer à la page suivante
            links = data.get('links', [])
            url = next((link['href'] for link in links if 'rel' in link and link['rel'] == 'next'), None)
        else:
            print("Erreur lors de la requête :", response.status_code)
            break
    return all_stop_areas

# Remplacez par votre clé d'API
api_key = "877d0066-7f11-4b6a-89c6-6fd4c635c1f6"
stop_areas = fetch_all_stop_areas(api_key)
print(stop_areas)
