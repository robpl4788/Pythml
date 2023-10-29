

class Color:
    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue
    
    def __str__(self) -> str:
        output = "rgb("
        output += str(self.red)
        output += ", "
        output += str(self.green)
        output += ", "
        output += str(self.blue)
        output += ")"
        return output
    

black = Color(0, 0, 0)