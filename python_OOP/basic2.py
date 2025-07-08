# 모듈
import basic as bs
# 모듈을 가져올 때는 basic 이름을 가져오기 때문에
# __main__ 아니라 __name__이 basic으로 설정됨
# 따라서, basic 모듈을 import할 때는
# if __name__ == "__main__": 부분이 실행되지 않음

# 패키지를 구성할 때 __init__.py 파일이 필요함
# 이 파일이 있으면 해당 디렉토리가 패키지로 인식됨

bs.a.add()  # 30

# relative 패키지
# from . import basic as bs2
# relative import는 현재 모듈의 위치를 기준으로 상대 경로로 모듈을 가져옴

## 예외처리
try:
    result = bs.a.div()  # 10 / 20
    print(result)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다:", e)
except Exception as e:
    print("알 수 없는 오류:", e)    
else:
    print("예외가 발생하지 않았습니다:", result)
finally:
    print("예외 처리 완료")
    
## 내장함수
# 파이썬은 다양한 내장 함수를 제공함
# 내장&외장함수는 외우지말고, # 필요할 때마다 찾아서 사용하면 됨

# dir() 함수는 객체의 속성과 메서드를 나열함
# 자체적으로 가지고 있는 변수나 함수를 보여줌
print("dir(a):", dir(bs.a))

# eval() 함수는 문자열로 표현된 파이썬 코드를 실행함
result = eval("10 + 20")
print("eval 결과:", result)

# map() 함수는 리스트의 각 요소에 함수를 적용함
# 람다함수를 많이 씀
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("제곱된 숫자들:", squared_numbers)

## 외장함수
# 외장함수는 파이썬 표준 라이브러리에서 제공하는
# 다양한 기능을 가진 함수들임
# 예를 들어, os 모듈은 운영체제와 상호작용하는
# 함수들을 제공함
import os
# os 모듈을 사용하여 현재 작업 디렉토리를 가져옴
current_directory = os.getcwd()
print("현재 작업 디렉토리:", current_directory)

# time 모듈은 시간 관련 함수들을 제공함
import time
# 현재 시간을 가져옴
current_time = time.localtime()
# 시간 정보를 문자열로 변환함
current_time_string = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print("현재 시간:", current_time_string)

# webbrowser 모듈은 웹 브라우저를 제어하는
# 함수들을 제공함
import webbrowser
# 기본 웹 브라우저를 열어 구글 홈페이지를 엶
# webbrowser.open("https://www.google.com")

# sys 모듈은 파이썬 인터프리터와 상호작용하는
# 함수들을 제공함
import sys
# 현재 파이썬 버전을 출력함
print("현재 파이썬 버전:", sys.version)

# pickle 모듈은 파이썬 객체를 직렬화하고
# 역직렬화하는 함수들을 제공함
import pickle
# 예시로, 리스트를 직렬화하고 파일에 저장함
# data = [1, 2, 3, 4, 5]
# with open("data.pkl", "wb") as f:
#     pickle.dump(data, f)    

# JSON 모듈은 JSON 데이터를 처리하는
# 함수들을 제공함
