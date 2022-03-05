class test:
    __x=10
    def m1(self):
        print(test.__x)
t1=test()
t1.m1()
print(t1._test__x)
