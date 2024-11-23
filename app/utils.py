import requests

def fetch_anime_details(anime_name):
    url = "https://api.jikan.moe/v4/anime"
    params = {"q": anime_name}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            anime = data["data"][0]
            return {
                "image": anime["images"]["jpg"]["image_url"],
                "title": anime["title"],
                "score": anime["score"],
                "rank": anime["rank"],
                "genres": [genre["name"] for genre in anime["genres"]]
            }
    return None  # Return None if no anime is found or error occurs

