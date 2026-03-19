class A:
    def __init__(self, value):
        if value < 0:
            raise ValueError("Giá trị phải >= 0")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if v < 0:
            raise ValueError("Giá trị phải >= 0")
        self._value = v

    def __str__(self):
        return f"A(value={self._value})"

    def method(self):
        return f"Phương thức đối tượng với value={self._value}"

    @classmethod
    def class_method(cls):
        return "Đây là class method của A"

    @staticmethod
    def static_method():
        return "Đây là static method của A"

    def __eq__(self, other):
        return self._value == other._value

class B(A):  # kế thừa từ A
    def __init__(self, value, name):
        super().__init__(value)
        self.name = name

    def __str__(self):
        return f"B(name={self.name}, value={self._value})"

#Ví dụ:
a1 = A(10)
a2 = A(10)
b1 = B(20, "Test")

print(a1)
print(a1.method())
print(A.class_method())
print(A.static_method())
print("a1 == a2:", a1 == a2)
print(b1)