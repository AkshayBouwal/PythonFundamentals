import abc


class Parent(abc.ABC):

    def meth1(self):
        print("Parent method1 called")

    @abc.abstractmethod
    def meth2(self):
        pass


class Child(Parent):

    def meth3(self):
        print("Child method3 called")

    def meth2(self):
        print("Child method2 called - Overridden")


if __name__ == '__main__':
    c = Child()
    c.meth2()
