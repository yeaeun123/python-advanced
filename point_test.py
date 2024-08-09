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




if __name__ == "__main__":
    # bound_instance_method()
    # unbound_instance_method()
    class_member_test()