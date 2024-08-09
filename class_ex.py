class MyString(str):    # str을 상속받은 새로운 클래스
    pass

s = MyString()
print(s, "type:", type(s))

s = MyString("My Class")
print(MyString.__bases__)   # MyString의 부모 / (<class 'str'>,)
print(MyString.__bases__[0].__bases__)  # MyString의 1번째 부모의 부모 / (<class 'object'>,)

# s 의 부모는 str이므로 str의 모든 메서드를 활용 할 수 있다.
print(s.lower())

class myobj:
    pass


class Chimera(str, myobj):
    pass

print(type(Chimera))
print(Chimera.__bases__)    # (<class 'str'>, <class '__main__.myobj'>)

print(issubclass(Chimera, str))     # 서브클래스 여부 확인


from point import Point

p = Point()
p.setX(10)
p.setY(20)
print(p, type(p), "x=", p.getX(),"y=",p.getY())

