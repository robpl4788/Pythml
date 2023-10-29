import style
import color

enumerate

class TextStyle(style.Style):
    properties = {}


    shadows = []

    def compileCSS(self):
        if len(self.properties) == 0 and len(self.shadows) == 0:
            return ""
        
        output = self.selector + " {\n"
        for property in self.properties:
            output += self.properties[property]
        
        if len(self.shadows) != 0:
            output += "text-shadow: "
            for shadow in self.shadows:
                output += str(shadow)
            output += "\n"
        
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
    
    def setHeightPixel(self, pixels):
        self.properties["verticalAlign"] = "\tvertical-alignment: " + str(pixels) + ";"

    def setHeightPercentage(self, percentage):
        self.properties["verticalAlign"] = "\tvertical-alignment: " + str(percentage) + ";"
    
    #Lines
    def setOverline(self):
        self.properties["overLine"] = "\ttext-decoration-line: overline;\n"

    def setUnderline(self):
        self.properties["underLine"] = "\ttext-decoration-line: underline;\n"
    
    def setStrikeThrough(self):
        self.properties["strikeThrough"] = "\ttext-decoration-line: line-through;\n"

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
    
    def setLineThicknessPixels(self, pixels):
        self.properties["textLineThickness"] = "\ttext-decoration-thickness: " + str(pixels) + "px;\n"
    
    def setLineThicknessPercent(self, percent):
        self.properties["textLineThickness"] = "\ttext-decoration-thickness: " + str(percent) + "%;\n"


    #Text transformations
    def setUppercase(self):
        self.properties["textTransform"] = "\ntext-transform: uppercase;"
    
    def setLowercase(self):
        self.properties["textTransform"] = "\ntext-transform: lowercase;"
    
    def setCapitalize(self):
        self.properties["textTransform"] = "\ntext-transform: capitalize;"
    
    #Text Spacing - More units theorettically available
    def setIndent(self, pixels):
        self.properties["textIndent"] = "\ntext-indent: " + str(pixels) + "px;\n"
    
    def setLetterSpacing(self, pixels):
        self.properties["letterSpacing"] = "\nletter-spacing: " + str(pixels) + "px;\n"

    def setLineSpacing(self, spacing):
        self.properties["lineHeight"] = "\nline-Height: " + str(spacing) + ";\n"

    def setWordSpacing(self, pixels):
        self.properties["wordSpacing"] = "\word-spacing: " + str(pixels) + "px;\n"
    

    #Font?

    #Shadow?

class TextShadow:
    def __init__(self, horizontal, vertical, color = color.black, blur = 0):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.blur =  blur
    
    def compileCSS(self):
        output = " "
        output += self.horizontal
        output += "px "
        output += self.vertical
        output += "px "
        output += self.blur
        output += "px "
        output += str(self.color)
        output += ";"
        return 