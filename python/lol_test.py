import requests

api_key = "RGAPI-a1f91248-53e2-487a-ae5f-eff6d3026b48"
summoner_name = "Hide on bush"  # Faker 소환사 이름
summoner_name_encoded = requests.utils.quote(summoner_name)

url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}"
headers = {"X-Riot-Token": api_key}

response = requests.get(url, headers=headers)
print(response.status_code, response.text)

print("API KEY:", repr(api_key))

import requests

api_key = "RGAPI-a1f91248-53e2-487a-ae5f-eff6d3026b48"
headers = {"X-Riot-Token": api_key}

url = "https://kr.api.riotgames.com/lol/status/v4/platform-data"
r = requests.get(url, headers=headers)

print("status:", r.status_code)
print("response:", r.text)


