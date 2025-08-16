import requests
from datetime import datetime

today=datetime.today().strftime("%Y%m%d")
grade=input("학년 입력:")
class_nm=input("반 입력:")

api_key="a2a331d46daa4a43bad3c6d5394d536b"
link="https://open.neis.go.kr/hub/hisTimetable"
edu_code="J10"         
school_code="7531290"  

#파라미터
parameter={
    "KEY": api_key,                  
    "Type": "json",                 
    "ATPT_OFCDC_SC_CODE": edu_code, 
    "SD_SCHUL_CODE": school_code,   
    "GRADE": grade,                                                                                         
    "CLASS_NM": class_nm,       
    "ALL_TI_YMD": today             
}

response_api=requests.get(link, params=parameter)
if response_api.status_code==200:
    print("status_code==200")
    data=response_api.json()

    if "hisTimetable" in data:
        rows=data["hisTimetable"][1]["row"]
        print(f"\n{grade}학년 {class_nm}반 {today} 시간표: ")
        for row in rows:
            print(f"{row['PERIO']}교시-{row['ITRT_CNTNT']}")

    else:
        print("시간표가 없다.")

else:
    print("시간표 불러오기 실패.")