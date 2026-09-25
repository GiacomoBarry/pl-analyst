import httpx

URL = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = httpx.get(URL, timeout=10)

response.raise_for_status()
data = response.json()
players = data["elements"]

top_scorers = sorted(players, key=lambda p: p["goals_scored"], reverse=True)

for player in top_scorers[:20]:
    print(player["web_name"], player["goals_scored"])
