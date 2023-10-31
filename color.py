

class Color:
    def __init__(self, red, green, blue, alpha = 1.0) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
    
    def __str__(self) -> str:
        output = "rgb("
        output += str(self.red)
        output += ", "
        output += str(self.green)
        output += ", "
        output += str(self.blue)
        output += ", "
        output += str(self.alpha)
        output += ")"
        return output
    

black = Color(0, 0, 0)