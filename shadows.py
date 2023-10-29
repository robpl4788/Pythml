import color

class Shadow:
    def __init__(self, horizontal, vertical, color = color.black, blur = 0):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.blur =  blur
    
    def __str__(self):
        output = " "
        output += str(self.horizontal)
        output += "px "
        output += str(self.vertical)
        output += "px "
        output += str(self.blur)
        output += "px "
        output += str(self.color)
        output += ";"
        return output