class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, new_width: int) -> None:
        if new_width >= 0:
            self._width = new_width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, new_height: int) -> None:
        if new_height >= 0:
            self._height = new_height

    @property
    def area(self) -> int:
        return self._width*self._height
