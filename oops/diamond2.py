class A:
    def m(self):
        print('in Class A')


class B(A):
    def m(self):
        super().m()
        print('in Class B')


class C(A):
    def m(self):
        super().m()
        print('in Class C')


class D(C, B):
    def m(self):
        super().m()
        print('in Class D')


if __name__ == '__main__':
    x = D()
    x.m()
    print(D.mro())
