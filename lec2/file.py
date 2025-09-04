"""Module for unit testing"""
import unittest
def get_area_of_rectangle(width:int, height:int) -> int:
    """Returns the area of a rectangle.
    Parameters
    -------
    width:int
        The width of the rectangle
    height:int
        The height of the rectangle

    Returns
    -------
    int
        The area of the rectangle

    Raises
    -------
    ValueError
        If width or height is negative
    """
    if(width<0 or height<0):
        raise ValueError("Rectangle dimensions cannot be negative")
    return width*height


class TestArea(unittest.TestCase):
    def test_3_by_4(self) -> None:
        self.assertEqual(12, get_area_of_rectangle(3,4))
    
    def test_negative_area(self) -> None:
        with self.assertRaises(ValueError):
            get_area_of_rectangle(-1,4)

if __name__ == "__main__":
    unittest.main()