import datetime

#timetable
timetable = {
    "월": ["체육", "공통영어2", "정보", "공통국어2", "한국사2", "통합사회2", "과학탐구실험2"],
    "화": ["공통국어2", "통합과학2", "미술", "미술", "한국사2", "공통수학2"],
    "수": ["공통수학2", "공통국어2", "정보", "미술", "공통영어2", "통합과학2", "한국사2"],
    "목": ["정보", "통합사회2", "공통수학2", "통합과학2", "창주", "창주"],
    "금": ["통합과학2", "공통국어2", "체육", "진로", "통합사회2", "공통영어2", "공통수학2"]
}

#day
day = {0: "월", 1: "화", 2: "수", 3: "목", 4: "금", 5: "토", 6: "일"}

#day checking
today_1 = datetime.datetime.today().weekday()
today_2 = day[today_1]

print(f"\n오늘은 {today_2}요일이다.")

if today_2 in timetable:
    print("시간표:")
    for i, subj in enumerate(timetable[today_2], start=1):
        print(f"{i}교시: {subj}")
else:
    print("오늘은 주말인데 왜 물어봄?ㅋ")