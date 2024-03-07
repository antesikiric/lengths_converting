
class Length:
    units_of_lengths = {"mm": 0.001, "cm": 0.01, "dm": 0.1, "m": 1, "km": 1000}
    sorted_units = sorted(units_of_lengths.items(), key=lambda x: x[1], reverse=True)

    def __init__(self, length, normalization=False):
        if type(length) is str:
            data = length.split(" ")
            if len(data) == 1:
                self._value = float(data[0])
                self._unit = "m"
            else:
                self._value = float(data[0])
                self._unit = data[1]
        else:
            self._value = float(length)
            self._unit = "m"
        if normalization:
            self.normalization()

    def __str__(self):
        return "{0} {1}".format(self._value, self._unit)
    
    def length_in_meters(self):
        return Length.units_of_lengths[self._unit] * self._value

    def normalization(self):
        """

        """
        length = self.length_in_meters()
        value = abs(length)
        for (unit, multiplier) in Length.sorted_units:
            if value / multiplier > 1:
                break
        self._value = length / multiplier
        self._unit = unit

    def __add__(self, other):
        """
            Support for adding the number to length.
        """
        first_operand = self.length_in_meters()
        if isinstance(other, Length):
            second_operand = other.length_in_meters()
        elif isinstance(other, int) or isinstance(other, float):
            second_operand = Length(other).length_in_meters()
        else:
            raise TypeError("Inappropriate type of right operand argument!")
        return Length(first_operand + second_operand, True)
    
    def __radd__(self, left_operand):
        """
            Support for adding length to the number
        """
        first_operand = self.length_in_meters()
        if isinstance(left_operand, int) or isinstance(left_operand, float):
            second_operand = Length(left_operand).length_in_meters()
        else:
            raise TypeError("Inappropriate type of left operand argument!")
        return Length(first_operand + second_operand, True)
    
    def __sub__(self, other):
        """
            Support for subtracting the number from the length.
            When only the number without units is specified we
            assume that it is in meters.
        """
        first_operand = self.length_in_meters()
        if isinstance(other, Length):
            second_operand = other.length_in_meters()
        elif isinstance(other, int) or isinstance(other, float):
            second_operand = Length(other).length_in_meters()
        else:
            raise TypeError("Inappropriate type of right operand argument!")
        return Length(first_operand - second_operand, True)
    
    def __rsub__(self, left_operand):
        """
            Support for subtracting the length from the number.
        """
        first_operand = self.length_in_meters()
        if isinstance(left_operand, int) or isinstance(left_operand, float):
            second_operand = Length(left_operand).length_in_meters()
        else:
            raise TypeError("Inappropriate type of left operand argument!")
        return Length(second_operand - first_operand, True)
    
    def __mul__(self, factor):
        """
            Support for multiplying length by number
        """
        first_operand = self.length_in_meters()
        if isinstance(factor, int) or isinstance(factor, float):
            return Length(first_operand * factor, True)
        raise TypeError("Inappropriate type of factor argument!")
        
    
    def __rmul__(self, left_factor):
        """
            Support for multiplying a number by length
        """
        first_operand = self.length_in_meters()
        if isinstance(left_factor, int) or isinstance(left_factor, float):
            second_operand = Length(left_factor).length_in_meters()
            return Length(first_operand * second_operand, True) 
        raise TypeError("Inappropriate type of left factor argument!")
    
    def __truediv__(self, divisor):
        if divisor != 0 and isinstance(divisor, int):
            numerator = self.length_in_meters()
            return Length(numerator / divisor, True)
        elif divisor == 0:
            raise ZeroDivisionError()
        else:
            raise TypeError()














