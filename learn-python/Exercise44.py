#EXERCISE 44  Inheritance verses Composition


class Parent():
    def override(self,name):
        self.name=name
        print(name)
        print("parent override()")
    def implicit(self):
        print("parent implicit()")
    def altered(self):
        print("parent altered")
class Child(Parent):
    def override(self):
        print("child override")
    def altered(self):
        print("child,before parent altered")
        super().altered()
        print("child,after parent altered")
dad=Parent()
son=Child()
dad.override("abcd")
son.override()
dad.implicit()
dad.altered()
son.altered()