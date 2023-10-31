from constants import lengthUnits

class BoxStyle:
    def __init__(self) -> None:
        self.properties = {}
        self.borderStyles = {
            "top" : None,
            "left" : None,
            "bottom" : None,
            "right" : None
        }
    
    def compileCSS(self):
        output = ""
        
        if self.borderStyles["top"] != None:
            output += "border-style: "
            output += self.borderStyles["top"] + " "
            output += self.borderStyles["right"] + " "
            output += self.borderStyles["bottom"] + " "
            output += self.borderStyles["left"] + ";\n"
        
        for property in self.properties:
            output += self.properties[property]


        return output


    def setPadding(self, top, left = None, bottom = None, right = None, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set padding, defaulting to pixels")
            unit = "px"
        if left == None:
            left = top
        if bottom == None:
            bottom = top
        if right == None:
            right = left
        instruction = "\tpadding: "
        instruction += str(top) + unit
        instruction += " " + str(right) + unit
        instruction += " " + str(bottom) + unit
        instruction += " " + str(left) + unit + ";\n"

        self.properties["padding"] = instruction
    
    def setBorderStyle(self, newBorderStyle, top = True, left = True, bottom = True, right = True):
        validBorderStyles = ["dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset", "none", "hidden"]

        if newBorderStyle not in validBorderStyles:
            print("WARNING: " + newBorderStyle + " is not a valid border style, setting to solid")
            newBorderStyle = "solid"
        
        if top:
            self.borderStyles["top"] = newBorderStyle
        
        if left:
            self.borderStyles["left"] = newBorderStyle
        
        if bottom:
            self.borderStyles["bottom"] = newBorderStyle
        
        if right:
            self.borderStyles["right"] = newBorderStyle
    
    def setBorderWidth(self, top, left = None, bottom = None, right = None, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set border width, defaulting to pixels")
            unit = "px"
        if left == None:
            left = top
        if bottom == None:
            bottom = top
        if right == None:
            right = left
        instruction = "\tborder-width: "
        instruction += str(top) + unit
        instruction += " " + str(right) + unit
        instruction += " " + str(bottom) + unit
        instruction += " " + str(left) + unit + ";\n"
    
        self.properties["borderWidth"] = instruction

    def setBorderColor(self, top, left = None, bottom = None, right = None):
        if left == None:
            left = top
        if bottom == None:
            bottom = top
        if right == None:
            right = left
        instruction = "\tborder-color: "
        instruction += str(top)
        instruction += " " + str(right)
        instruction += " " + str(bottom)
        instruction += " " + str(left) + ";\n"
    
        self.properties["borderColor"] = instruction
    
    def setBorderRadius(self, topLeft, topRight = None, bottomLeft = None, bottomRight = None, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set border radius, defaulting to pixels")
            unit = "px"
        if topRight == None:
            topRight = topLeft
        if bottomLeft == None:
            bottomLeft = topRight
        if bottomRight == None:
            bottomRight = topLeft
        instruction = "\tborder-width: "
        instruction += str(topLeft) + unit
        instruction += " " + str(topRight) + unit
        instruction += " " + str(bottomLeft) + unit
        instruction += " " + str(bottomRight) + unit + "\n;"
    
        self.properties["borderRadius"] = instruction

    def setMargin(self, top, left = None, bottom = None, right = None, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set border width, defaulting to pixels")
            unit = "px"
        if left == None:
            left = top
        if bottom == None:
            bottom = top
        if right == None:
            right = left
        instruction = "\margin: "
        instruction += str(top) + unit
        instruction += " " + str(right) + unit
        instruction += " " + str(bottom) + unit
        instruction += " " + str(left) + unit + ";\n"
        self.properties["margin"] = instruction


    def setMarginAutoHorizontal(self, top, bottom = None, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set border width, defaulting to pixels")
            unit = "px"
        if bottom == None:
            bottom = top
        instruction = "\margin: "
        instruction += str(top) + unit
        instruction += " auto "
        instruction += str(bottom) + unit
        instruction += " auto;\n"
        self.properties["margin"] = instruction
