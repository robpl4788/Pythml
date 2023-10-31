import color
from constants import lengthUnits
from shadows import Shadow


class TextStyle:
    def __init__(self) -> None:
        self.properties = {}
        self.shadows = []
        self.fonts = []

    
    def compileCSS(self):
        output = ""
        
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
        
        for property in self.properties:
            output += self.properties[property]


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
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set text height, defaulting to pixels")
            unit = "px"
        self.properties["verticalAlign"] = "\tvertical-alignment: " + str(length) + unit + ";\n"
    
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
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set line thickness, defaulting to pixels")
            unit = "px"
        self.properties["textLineThickness"] = "\ttext-decoration-thickness: " + str(length) + unit + ";\n"



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
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set letter spacing, defaulting to pixels")
            unit = "px"
        self.properties["letterSpacing"] = "\tletter-spacing: " + str(length) + unit + ";\n"


    def setLineSpacing(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set line spacing, defaulting to pixels")
            unit = "px"
        self.properties["lineHeight"] = "\tline-Height: " + str(length) + unit + ";\n"

    def setWordSpacing(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set word spacing, defaulting to pixels")
            unit = "px"
        self.properties["wordSpacing"] = "\ttword-spacing: " + str(length) + unit + ";\n"
    

    #Font - Order added is priority, with first being highest
    def addFont(self, fontName):
        self.fonts.append(str(fontName))
    
    def setFontSize(self, length, unit = "px"):
        if unit not in lengthUnits:
            print("WARNING: " + str(unit) + " is not a valid length to set font size, defaulting to pixels")
            unit = "px"
        self.properties["fontSize"] = "\tfont-size: " + str(length) + unit + ";\n"

    #Shadows
    def addTextShadow(self, horizontal, vertical, color, blur):
        self.shadows.append(Shadow(horizontal, vertical, color, blur))