class A:
    def m(self):
        print('in Class A')


class B(A):
    def m(self):
        print('in Class B')


class C(A):
    def m(self):
        print('in Class C')


# Inherits from B, then C. It does not override m()
class D1(B, C):
    pass


# Different order of subclass list
class D2(C, B):
    pass


# Override m()
class D3(B, C):
    def m(self):
        print('in Class D3')


if __name__ == '__main__':
    x = D1()
    x.m()  # 'in Class B' (first in subclass list)

    x = D2()
    x.m()  # 'in Class C' (first in subclass list)

    x = D3()
    x.m()  # 'in Class D3' (overridden version)