class A(object):
    def display(self):
        print("display from class A")
        super().display()
class B(object):
    def display(self):
        print("display from class B")
        super().display()
class C(object):
    def display(self):
        print("display from class C")
class D(A,B):
    def display(self):
        print("display from class D")
        super().display()
class E(B,C):
    def display(self):
        print("display from class E")
        super().display()
class X(D,E):
    def display(self):
        print("display from class X")
        super().display()
x1=X()
x1.display()
print(X.mro())

