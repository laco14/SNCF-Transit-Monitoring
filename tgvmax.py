import requests

def fetch_tgvmax_data(api_key):
    url = "https://ressources.data.sncf.com/api/records/1.0/search/"
    params = {
        'dataset': 'tgvmax',
        'rows': 20,  # Limite les résultats à 20 trajets
        'start': 0,  # Commence à 0 pour les 20 premiers enregistrements
        'apikey': api_key
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Vérifie que la requête ne retourne pas d'erreur
        data = response.json()
        records = data.get('records', [])
        for record in records:
            fields = record.get('fields', {})
            print({
                'DATE': fields.get('date'),
                'TRAIN_NO': fields.get('numero_de_train'),
                'ENTITY': fields.get('entite'),
                'Axe': fields.get('axe'),
                'Origine IATA': fields.get('origine_iata'),
                'Destination IATA': fields.get('destination_iata'),
                'Origine': fields.get('origine'),
                'Destination': fields.get('destination'),
                'Heure_depart': fields.get('heure_depart'),
                'Heure_arrivee': fields.get('heure_arrivee'),
                'Disponibilité MAX JEUNE': fields.get('disponibilite_max_jeune'),
                'Disponibilité MAX SENIOR': fields.get('disponibilite_max_senior')
            })
    except requests.RequestException as e:
        print(f"Une erreur s'est produite: {e}")

# Utilisation de la clé API (assurez-vous de la remplacer par votre clé réelle et de la gérer de manière sécurisée)
api_key = '877d0066-7f11-4b6a-89c6-6fd4c635c1f6'
fetch_tgvmax_data(api_key)
