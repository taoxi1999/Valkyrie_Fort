class Foo(object):
    objs = []  # registrar

    def __init__(obj, num):
        # register the new object with the class
        Foo.objs.append(obj)
        obj.my_value = num

    def report(self):
        print self.my_value

    @classmethod
    def crunch_all(cls):
        for obj in cls.objs:
            obj.my_value = obj.my_value + 1

ts1 = Foo(1)
ts2 = Foo(10)
ts1.report()
ts2.report()

Foo.crunch_all()
ts1.report()
ts2.report()
