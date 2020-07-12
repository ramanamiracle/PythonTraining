class A:
    def m(self):
        print('in Class A')


class B(A):
    def m(self):
        A.m(self)
        print('in Class B')


class C(A):
    def m(self):
        A.m(self)
        print('in Class C')


class D(B, C):
    def m(self):
        B.m(self)
        C.m(self)
        print('in Class D')


if __name__ == '__main__':
    x = D()
    x.m()