class Person:
    name = 'default'
    gender = 'Male/Female'

    def Hello(self):
        print(self.name + ': 안녕')

gyumin = Person()
gyumin.name = "규민이"
gyumin.gender = 'Male'
gyumin.Hello()