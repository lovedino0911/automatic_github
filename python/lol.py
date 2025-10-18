import requests

api_key = "RGAPI-a9b1efe7-c359-48ab-a9f8-53e54ad9e574"
if not api_key:
    raise SystemExit("error")

summoner_name = input("소환사 이름 입력: ")
summoner_name_encoded = requests.utils.quote(summoner_name)

url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name_encoded}"
headers = {"X-Riot-Token": api_key}

response = requests.get(url, headers=headers)
print(response.text)

if response.status_code == 200:
    summoner_data = response.json()
    puuid = summoner_data["puuid"]
    print(f"puuid : {puuid}")

    # 최근 20게임 매치 리스트 가져오기
    match_url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    params = {"start": 0, "count": 20}
    match_headers = {"X-Riot-Token": api_key}
    match_response = requests.get(match_url, headers=match_headers, params=params)
    if match_response.status_code == 200:
        match_ids = match_response.json()
        print("최근 매치 ID 리스트:", match_ids)

        # 매치 상세 정보 가져오기
        match_results = []
        for match_id in match_ids:
            match_detail_url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
            detail_response = requests.get(match_detail_url, headers=match_headers)
            if detail_response.status_code == 200:
                match_data = detail_response.json()
                match_results.append(match_data)
            else:
                print(f"{match_id} 매치 정보 불러오기 실패")

        print(f"가져온 매치 개수 : {len(match_results)}")

        # 승률, 챔피언 전적
        win_count = 0
        champ_stats = {}

        for match in match_results:
            info = match.get("info", {})
            participants = info.get("participants", [])
            my_data = None
            for p in participants:
                if p.get("puuid") == puuid:
                    my_data = p
                    break

            if not my_data:
                continue

            # 승패 집계
            if my_data.get("win"):
                win_count += 1

            # 챔피언별 집계
            champ = my_data.get("championName")
            if champ not in champ_stats:
                champ_stats[champ] = {"games": 0, "wins": 0}
            champ_stats[champ]["games"] += 1
            if my_data.get("win"):
                champ_stats[champ]["wins"] += 1

        total_games = len(match_results)
        win_rate = win_count / total_games * 100 if total_games > 0 else 0
        print(f"\n최근 {total_games}게임 승률 : {win_rate:.1f}%")

        # 가장 많이 플레이한 챔피언
        if champ_stats:
            best_champ = max(champ_stats, key=lambda c: champ_stats[c]["games"])
            champ_games = champ_stats[best_champ]["games"]
            champ_wins = champ_stats[best_champ]["wins"]
            champ_win_rate = champ_wins / champ_games * 100 if champ_games > 0 else 0
            print(f"가장 많이 플레이 한 챔피언 : {best_champ} ({champ_games} 게임, 승률 {champ_win_rate:.1f}%)")
        else:
            print("챔피언 정보 없음")
    else:
        print("매치 리스트를 가져올 수 없습니다.")
else:
    print("소환사 정보를 가져올 수 없습니다.")

print("status code :", response.status_code)
print("response text :", response.text)