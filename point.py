class Point:
    instance_count = 0  # 클래스 멤버
    # 클래스 멤버: 클래스 이름 공간 내에 생성, 모든 인스턴스 객체가 공유
    # 인스턴스 멤버 : 인스턴스 공간 내에 생성, 개별 인스턴스 객체 내부에서만 활용
    

    def __init__(self,x=0, y=0):    # 생성자 : 매개변수 x , y
        self.x, self.y = x, y
        Point.instance_count += 1

    def __del__(self):
        Point.instance_count -= 1

    def __str__(self):
        # 객체를 문자열로 변환
        return f"Point x = {self.x}, y = {self.y}"

    def __repr__(self):
        # 객체를 문자열로 변환
        # 원래 목적: 객체 재현
        return f"Point({self.x}, {self.y})"

    def setX(self, x):  # 인스턴스 메서드의 첫 번째 인자는 self
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    # 연산자 오버로딩 +
    # 산술연산자 + 오버로딩
    # Point + Point
    # Point + int
    def __add__(self, other):   # Point + {other}
        if isinstance(other, int):  # x, y값에 int 값을 합산
            self.x += other
            self.y += other
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        return self

    def __radd__(self, other):  # {other} + Point
        if isinstance(other, int):
            self.x += other
            self.y += other
        return self

    def __eq__(self, other):    # Point == {other}
        if (isinstance(other, Point)):
            return self.x == other.x and self.y == other.y
        return False

    # 연습
    # 산술연산자, 역이항연산자, 비교연산자 중에서
    # 몇 개는 오버라이딩 해 보기 


# 정적 메서드와 클래스메서드
#   - 클래스 메서드: 모든 인스턴스들이 공유하는 메서드
#   - 정적 메서드: 현재 클래스의 네임스페이스만 공유
# @staticmethod, @classmethod 라는 데코레이터로 선언 가능

# Singlton Pattern 예제
class Singleton:
    # 인스턴스를 저장할 객체
    __instance = None

    def __init__(self):
        # 유일 객체만 유지해야 함
        if Singleton.__instance != None:
            raise Exception("이 객체는 싱글턴입니다. getInstance()를 사용하세요.")
        else:
            Singleton.__instance =self

    # 클래스 메서드
    @classmethod
    def getClassinstance(cls):
        print(cls.__instance)
        if cls.__instance == None:
            Singleton()
        return cls.__instance

    # 정적 메서드
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance