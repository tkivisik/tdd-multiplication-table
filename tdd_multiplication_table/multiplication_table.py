class NotPositiveDimensionsException(Exception):
    pass

class TooBigDimensionsException(Exception):
    pass

class MultiplicationTable(object):
    def __init__(self, height, width, DIMENSION_MAX=20):
        self.DIMENSION_MAX = DIMENSION_MAX
        self.height = height
        self.width = width

        self.verify_dimensions()

    def verify_dimensions(self):
        if self.height <= 0 or self.width <= 0:
            raise NotPositiveDimensionsException("MultiplicationTable expects positive height and width")
        if self.height > self.DIMENSION_MAX or self.width > self.DIMENSION_MAX:
            raise TooBigDimensionsException("Dimensions must be <= {}".format(self.DIMENSION_MAX))

    def show_table_string(self):
        self.verify_dimensions()
        table_string = ""
        for h in range(1, self.height + 1):
            line = ''
            for w in range(1, self.width + 1):
                new_element = str(h*w).rjust(4)
                line = "{}{}".format(line, new_element)
            table_string = "{}{}\n".format(table_string, line)
        return table_string
    
    def update_height(self, amount):
        amount = MultiplicationTable.verify_intable(amount)
        self.height = self.height + amount
        self.verify_dimensions()

    def update_width(self, amount):
        amount = MultiplicationTable.verify_intable(amount)
        self.width = self.width + amount
        self.verify_dimensions()

    @staticmethod
    def verify_intable(element):
        if isinstance(element, int):
            return element
        else:
            try:
                if abs(int(float(element)) - float(element)) < 0.00001:
                    return int(float(element))
            except:
                raise TypeError("Was expecting a whole number")


def main():
    table = MultiplicationTable(10,10)
    while True:
        print("This is your multiplication table")
        print(table.show_table_string())
        print('')
        print("Enter 'x' to exit")
        print("Enter how much you would like to change the dimenstions")
        input = raw_input("Separate amounts by commas (height, width):")
        if input in ['x', 'exit', 'quit']:
            break
        if input.find(",") == -1:
            continue
        height_change, width_change = input.split(",")[0], input.split(",")[1]
        table.update_height(height_change)
        table.update_width(width_change)

if __name__ == '__main__':
    main()