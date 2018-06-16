class Foo(object):
    objs = []  # registrar

    def __init__(self, num):
        # register the new object with the class
        Foo.objs.append(self)
        self.my_value = num

    #@classmethod
    def crunch_all(cls):
        for obj in cls.objs:
            obj.new_value = obj.my_value + 1

ts1 = Foo(1)
ts2 = Foo(10)
Foo.crunch_all()
