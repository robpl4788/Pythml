import style
import color
from constants import lengthUnits


class TextStyle(style.Style):
    def __init__(self) -> None:
        super().__init__()

        self.shadows = []
        self.fonts = []

    

    def compileCSS(self):
        if len(self.properties) == 0 and len(self.shadows) == 0:
            return ""

        output = self.beginCSScompile()
        
        if len(self.shadows) != 0:
            output += "\ttext-shadow: "
            for shadow in self.shadows:
                output += str(shadow)
            output += "\n"
        
        if len(self.fonts) != 0:
            output += "\tfont-family: "
            firstLoop = True
            for font in self.fonts:
                if firstLoop:
                    firstLoop = False
                else:
                    output += ", "
                output += font

            output += ";\n"

        output += "}\n\n"
        return output
    



    def setTextColor(self, color):
        self.properties["color"] = "\tcolor: " + str(color) + ";\n"
    
    def setBackgroundColor(self, color):
        self.properties["backGroundColor"] = "\tbackground-color: " + str(color) + ";\n"
    
    #Main text alignment
    def setLeftAlign(self):
        self.properties["textAlign"] = "\ttext-align: left;\n"
    
    def setCenterAlign(self):
        self.properties["textAlign"] = "\ttext-align: center;\n"

    def setRightAlign(self):
        self.properties["textAlign"] = "\ttext-align: right;\n"
    
    def setJustifiedAlign(self):
        self.properties["textAlign"] = "\ttext-align: justify;\n"


    #Last line alignment
    def setLeftAlignLast(self):
        self.properties["textAlign"] = "\ttext-align-last: left;\n"
    
    def setCenterAlignLast(self):
        self.properties["textAlign"] = "\ttext-align-last: center;\n"

    def setRightAlignLast(self):
        self.properties["textAlign"] = "\ttext-align-last: right;\n"
    
    def setJustifiedAlignLast(self):
        self.properties["textAlign"] = "\ttext-align-last: justify;\n"


    #Vertical Alignment
    def setSubscript(self):
        self.properties["verticalAlign"] = "\tvertical-alignment: sub;"

    def setSuperScript(self):
        self.properties["verticalAlign"] = "\tvertical-alignment: super;"
    
    def setTextHeight(self, length, unit = "px"):
        if unit in lengthUnits:
            self.properties["verticalAlign"] = "\tvertical-alignment: " + str(length) + unit + ";\n"
        else:
            print("WARNING: " + str(unit) + " is not a valid length, defaulting to pixels")
            self.properties["verticalAlign"] = "\tvertical-alignment: " + str(length) + "px;\n"

    #Lines
    def setOverline(self):
        self.properties["overLine"] = "\ttext-decoration-line: overline;\n"

    def setUnderline(self):
        self.properties["underLine"] = "\ttext-decoration-line: underline;\n"
    
    def setStrikeThrough(self):
        self.properties["strikeThrough"] = "\ttext-decoration-line: line-through;\n"

    def setNoLines(self):
        self.properties["underLine"] = "\ttext-decoration-line: none;\n"
        self.properties["overLine"] = ""
        self.properties["strikeThrough"] = ""


    #Line Styles
    def setLineStyleDouble(self):
        self.properties["textLineStyle"] = "\ttext-decoration-style: double;\n"
    
    def setLineStyleDotted(self):
        self.properties["textLineStyle"] = "\ttext-decoration-style: dotted;\n"
    
    def setLineStyleUnderDashed(self):
        self.properties["textLineStyle"] = "\ttext-decoration-style: dashed;\n"
    
    def setLineStyleWavy(self):
        self.properties["textLineStyle"] = "\ttext-decoration-style: wavy;\n"
    
    def setLineColor(self, color):
        self.properties["textLineColor"] = "\ttext-decoration-color: " + str(color) + ";"
    
    def setLineThickness(self, length, unit = "px"):
        if unit in lengthUnits:
            self.properties["textLineThickness"] = "\ttext-decoration-thickness: " + str(length) + unit + ";\n"
        else:
            print("WARNING: " + str(unit) + " is not a valid length, defaulting to pixels")
            self.properties["textLineThickness"] = "\ttext-decoration-thickness: " + str(length) + "px;\n"




    #Text transformations
    def setUppercase(self):
        self.properties["textTransform"] = "\ttext-transform: uppercase;"
    
    def setLowercase(self):
        self.properties["textTransform"] = "\ttext-transform: lowercase;"
    
    def setCapitalize(self):
        self.properties["textTransform"] = "\ttext-transform: capitalize;"
    
    #Text Spacing
    def setIndent(self, pixels):
        self.properties["textIndent"] = "\ttext-indent: " + str(pixels) + "px;\n"
    
    def setLetterSpacing(self, length, unit = "px"):
        if unit in lengthUnits:
            self.properties["letterSpacing"] = "\tletter-spacing: " + str(length) + unit + ";\n"
        else:
            print("WARNING: " + str(unit) + " is not a valid length, defaulting to pixels")
            self.properties["letterSpacing"] = "\tletter-spacing: " + str(length) + "px;\n"


    def setLineSpacing(self, length, unit = "px"):
        if unit in lengthUnits:
            self.properties["lineHeight"] = "\tline-Height: " + str(length) + unit + ";\n"
        else:
            print("WARNING: " + str(unit) + " is not a valid length, defaulting to pixels")
            self.properties["lineHeight"] = "\tline-Height: " + str(length) + "px;\n"

    def setWordSpacing(self, length, unit = "px"):
        if unit in lengthUnits:
            self.properties["wordSpacing"] = "\ttword-spacing: " + str(length) + unit + ";\n"
        else:
            print("WARNING: " + str(unit) + " is not a valid length, defaulting to pixels")
            self.properties["wordSpacing"] = "\ttword-spacing: " + str(length) + "px;\n"
    

    #Font - Order added is priority, with first being highest
    def addFont(self, fontName):
        self.fonts.append(str(fontName))
    
    def setFontSize(self, length, unit = "px"):
        if unit in lengthUnits:
            self.properties["fontSize"] = "\tfont-size: " + str(length) + unit + ";\n"
        else:
            print("WARNING: " + str(unit) + " is not a valid length, defaulting to pixels")
            self.properties["fontSize"] = "\tfont-size: " + str(length) + "px;\n"

    #Shadows
    def addShadow(self, horizontal, vertical, color, blur):
        self.shadows.append(TextShadow(horizontal, vertical, color, blur))

class TextShadow:
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