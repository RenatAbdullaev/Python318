class AreaCalculator:
    count = 0

    @staticmethod
    def triangle_area_by_heron(a, b, c):
        AreaCalculator.count += 1
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    @staticmethod
    def triangle_area_by_base_height(base, height):
        AreaCalculator.count += 1
        return 0.5 * base * height

    @staticmethod
    def square_area(side):
        AreaCalculator.count += 1
        return side ** 2

    @staticmethod
    def rectangle_area(length, width):
        AreaCalculator.count += 1
        return length * width

    @staticmethod
    def get_count():
        return AreaCalculator.count


print("площадь треугольника по формуле герона (3, 4, 5):", AreaCalculator.triangle_area_by_heron(3, 4, 5))
print("площадь треугольника через основание и высоту (6, 7):", AreaCalculator.triangle_area_by_base_height(6, 7))
print("площадь квадрата (7):", AreaCalculator.square_area(7))
print("площадь прямоугольника (2, 6):", AreaCalculator.rectangle_area(2, 6))
print("количество подсчетов площади:", AreaCalculator.get_count())
