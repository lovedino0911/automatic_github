import requests
from datetime import datetime

edu_code="D10" 
school_code="B000024656"
today=datetime.today().strftime("%YM%m%d")
link="https://open.neis.go.kr/hub/mealServiceDietInfo"

#parameter
parameter={
    "KEY": "a2a331d46daa4a43bad3c6d5394d536b",
    "TYPE":"json",
    "ATPT_OFCDC_SC_CODE": edu_code,
    "SD_SCHUL_CODE": school_code,
    "MLSV_YMD":today
}

response_api=requests.get(link, params=parameter)
if response_api.status_code==200:
    print("status_code==200")
    data=response_api.json()
    if "mealServiceDietInfo" in data:
        rows=data["mealServiceDietInfo"][1]["row"]
        print(f"\n{today} 급식:")
        for row in rows:
            print(f"\n{row['DDISH_NM']}")
            print("\n요리명에 표시된 숫자는 아래 알레르기 유발 식품을 의미한다.")
            print("""1.난류, 2.우유, 3.메밀, 4.땅콩, 5.대두, 6.밀, 7.고등어, 8.게, 9.새우, 10.돼지고기, 11.복숭아, 12.토마토, 13.아황산류, 14.호두,
15.닭고기, 16.쇠고기, 17.오징어, 18.조개류(굴, 전복, 홍합 포함), 19.잣""")
            print(f"\n칼로리:{row['CAL_INFO']}kcal")
        
    else:
        print("급식 정보가 없다.")
else:
    print("급식 정보 불러오기 실패.")