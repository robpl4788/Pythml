import textStyle
import boxStyle
from constants import lengthUnits
from shadows import Shadow
import color

class Style:
    usedClasses = []

    def __init__(self) -> None:
        self.properties = {}
        self.text = textStyle.TextStyle()
        self.box = boxStyle.BoxStyle()


        if len(self.usedClasses) == 0:
            self.className = "a0"
        else:
            num = int(self.usedClasses[-1][1:])
            self.className = "a" + str(num + 1)
        self.usedClasses.append(self.className)
        self.selectors = [self.className]

    def compileCSS(self):
        output = ""

        firstLoop = True
        for selector in self.selectors:
            if firstLoop:
                firstLoop = False
            else:
                output += ", "
            output += "." + str(selector)
        
        output += " {\n"
        
        for property in self.properties:
            output += self.properties[property]
        
        output += self.text.compileCSS()

        output += "}\n\n"        
        return output

    def addElementSelector(self, newElement):
        self.selectors.append(str(newElement))
    
    def setUniversal(self):
        self.selectors.append("*")
    
    def getClassName(self):
        return self.className

    def setWidth(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set width, defaulting to pixels")
            unit = "px"
        self.properties["width"] = "\twidth: " + str(length) + unit + ";\n"

    def setHeight(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set height, defaulting to pixels")
            unit = "px"
        self.properties["height"] = "\theight: " + str(length) + unit + ";\n"
    
    def setMinWidth(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set min width, defaulting to pixels")
            unit = "px"
        self.properties["minWidth"] = "\tmin-width: " + str(length) + unit + ";\n"

    def setMinHeight(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set min height, defaulting to pixels")
            unit = "px"
        self.properties["minHeight"] = "\min-height: " + str(length) + unit + ";\n"
    
    def setMaxWidth(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set max width, defaulting to pixels")
            unit = "px"
        self.properties["maxWidth"] = "\tmax-width: " + str(length) + unit + ";\n"

    def setMaxHeight(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set max height, defaulting to pixels")
            unit = "px"
        self.properties["maxHeight"] = "\tmax-height: " + str(length) + unit + ";\n"
    

    def setBackgroundColor(self, color):
        self.properties["backgroundColor"] = "\tbackground-color: " + str(color)
    


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