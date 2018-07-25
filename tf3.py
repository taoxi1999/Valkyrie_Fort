class tester(object):
    def __init__(obj, num):
        obj.num = num

    def report(self):
        print self.num

tes = tester(1)
tes.report()
