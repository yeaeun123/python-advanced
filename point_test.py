from point import Point

def bound_instance_method():
    """
    bound instance method: 인스턴스에 직접 바인딩 된 메서드
    """
    p = Point() # Point 인스턴스 생성
    p.setX(10)
    p.setY(20)

    print(p.getX(), p.getY(), sep=",")
    print(p.getX, p.getY)   # bound method Point.getX of <point.Point object at 0x000001B37869B460>>

def unbound_instance_method():
    """
    unbound instance method : 클래스 메서드에 인스턴스 참조주소를 전달해서
                            우회 접근하는 방법.
                            인스턴스 메서드의 첫 번째 인자가 self인 이유
    """
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point.getX(p), Point.getY(p), sep=",")
    print(Point.getX, Point.getY)   # function Point.getX


def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)
    print(p1.getX(), p1.getY(), p1.instance_count)
    # p1.instance_count는 클래스 멤버(인스턴스 멤버 아님!)


    p2 = Point()
    p2.setX(20)
    p2.setY(30)
    print(p2.getX(), p2.getY(), p2.instance_count)
    # p2.instance_count는 클래스 멤버

    print(p1.x is p2.x) # False
    print(p1.instance_count is p2.instance_count)   # True

def constructor_test():
    p1 = Point(10, 20)
    print("instance_count:", Point.instance_count)

    p2 = Point()    # 생성자의 기본 값이 활용
    print("instance_count:", Point.instance_count)

    p3 = Point(x = 30, y = 40)
    print("instance_count:", Point.instance_count)

    del p1
    del p2

    print("instance_count:", Point.instance_count)


def stringify():
    p = Point(10, 20)
    print(p)    # 문자열화 -> __str__이 호출된다.
    print(repr(p))  # 문자열화 -> 원래 객체를 재현할 수 있는 문자열 / __repr__호출

    p_repr = eval(repr(p))
    print(p_repr)

    print(p.x == p_repr.x)
    print(p.y == p_repr.y)


from point import Singleton
def singleton_test():
    s = Singleton()
    print(s)
    # s2 = Singleton()  # 예외 발생
    s2 = Singleton.getClassinstance()
    print(s2)

    # s1, s2 객체가 동일 객체인가?
    print(s is s2)


def oper_overriding():
    # 산술연산자 오버로딩
    print(Point(10, 20) + Point(30, 40))
    print(Point(10, 20) + 30)

    # 역이항 산술연산자 오버로딩
    print(Point(30, 40) + Point(10, 20))
    print(30 + Point(10, 20))   # __radd__

    # 비교연산자
    print(Point(10, 20) == Point(10, 20))   # __eq__
    print(Point(10, 20) == Point(30, 40))


if __name__ == "__main__":
    # bound_instance_method()
    # unbound_instance_method()
    # class_member_test()
    # constructor_test()
    # stringify()
    # singleton_test()
    oper_overriding()