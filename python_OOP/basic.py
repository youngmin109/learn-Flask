# 기본 지식
# 함수와 메서드의 차이
# 함수는 독립적으로 존재할 수 있지만,
# 메서드는 클래스의 일부로 존재함

# self는 인스턴스 자신을 가리키는 참조
# java의 this와 유사
# jvm이 this를 자동으로 추가해주지만,
# 파이썬에서는 명시적으로 self를 사용해야 함

# __언더바 2개 함수는 미리 정의된 특별한 메서드
# __name__은 클래스의 이름을 나타내는 특별한 속성

# 클래스는 대문자로 시작
class Calculator:
    # 클래스 변수 
    # num1 = 1
    # num2 = 2
    # 이런식으로 공통 변수를 정의할 수 있지만,
    # 일반적으로 인스턴스 변수로 정의함
    
    # init 메서드는 클래스가 인스턴스화될 때 호출됨
    # 자바에서 생성자와 유사
    def __init__(self, num1, num2):
        self.num1 = num1 # 인스턴스 변수
        self.num2 = num2
    # 메서드는 클래스의 일부로 정의됨
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    
# 인스턴스 생성
a = Calculator(10, 20)
print(a.add())  # 30

# 상속
# 파이썬은 다중 상속을 지원한다.

class Calculator2(Calculator):
    # init 메서드를 오버라이드
    def __init__(self, num1, num2, num3):
        # 부모 클래스의 init 메서드를 호출
        super().__init__(num1, num2)
        self.num3 = num3
    
    # 제곱
    def pow(self):
        return self.num1 ** self.num3
    
b = Calculator2(10, 20, 2)
if __name__ == "__main__":
    print(b.pow())

