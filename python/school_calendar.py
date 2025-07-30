import datetime

#timetable
timetable = {
    "월": ["1교시", "2교시", "3교시", "4교시", "5교시", "6교시", "7교시"],
    "화": ["1교시", "2교시", "3교시", "4교시", "5교시", "6교시"],
    "수": ["1교시", "2교시", "3교시", "4교시", "5교시", "6교시", "7교시"],
    "목": ["1교시", "2교시", "3교시", "4교시", "5교시", "6교시"],
    "금": ["1교시", "2교시", "3교시", "4교시", "5교시", "6교시", "7교시"]
}

#day
day = {0: "월", 1: "화", 2: "수", 3: "목", 4: "금", 5: "토", 6: "일"}

#day checking
today_1 = datetime.datetime.today().weekday()
today_2 = day[today_1]

print(f"\n오늘은 {today_2}요일이다.")

if today_2 in timetable:
    print("시간표:")
    for i, subj in enumerate(timetable[today_2]):
        print(f"{i}교시: {subj}")
else:
    print("오늘은 주말인데 왜 물어봄?ㅋ")