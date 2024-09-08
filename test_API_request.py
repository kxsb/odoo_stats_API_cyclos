import requests

# URL de l'API Cyclos pour obtenir les utilisateurs
cyclos_api_url = "https://mlc.sol-reseau.org/lagonette/api/users"

# Token de session obtenu précédemment
session_token = "inscrire_votre_token_ici"

# En-têtes de la requête
headers = {
    "Content-Type": "application/json"
}

# Ajouter le token dans les cookies
cookies = {
    "Session-Token": session_token
}

# Effectuer la requête GET avec les cookies
response = requests.get(cyclos_api_url, headers=headers, cookies=cookies)

# Vérification de la réponse
if response.status_code == 200:
    users_info = response.json()
    print("Token valide. Voici les informations des utilisateurs :")
    print(users_info)
else:
    print(f"Token invalide ou expiré : {response.status_code} - {response.text}")

print("Headers de réponse:", response.headers)
