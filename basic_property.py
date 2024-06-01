# @property로 getter, setter를 설정하면
class Person:
    def __init__(self) -> None:
        self.__friendname = "default name"
    
    @property
    def name(self):
        return self.__friendname
    
    @name.setter
    def name(self, name):
        self.__friendname = name

#get, set도 달리짐
gyumin = Person()
gyumin.name = "gyumin"
print(gyumin.name)