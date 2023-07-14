### Aufgabe 4
import math
class Vector2d():
    def __init__(self, x_ :int, y_:int) -> None:
        self.__x = x_
        self.__y = y_
    def __add__(self, v :"Vector2d") -> "Vector2d":
        vr = Vector2d(0,0)
        vr.__x = self.__x + v.__x
        vr.__y = self.__y + v.__y
        return vr
        
    def __sub__(self, v: "Vector2d") -> "Vector2d":
        vr = Vector2d(0,0)
        vr.__x = self.__x - v.__x
        vr.__y = self.__y - v.__y
        return vr
    
    def __mul__(self, v: "Vector2d") -> int:
        return self.__x*v.__x + self.__y*v.__y
    
    def __abs__(self) -> float:
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def __eq__(self, v: "Vector2d") -> bool:
        return (self.__x == v.__x and self.__y == v.__y)
    
    def __str__(self) -> str:
        return f"(x={self.__x}, y={self.__y})"

if __name__ == "__main__":
    v1: Vector2d = Vector2d(2,3)
    v2: Vector2d = Vector2d(4,5)

    print(v1+v2,v1-v2,v1*v2,abs(v1))
    print(v1==v2,v2==v2,v1,v2)