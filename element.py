

class Element:
    def __init__(self) -> None:
        self.styles = []

    def addStyle(self, style):
        if style.getClassName() == None:
            a = "1 " + 1
        self.styles.append(style.getClassName())
    
    def getStyles(self):
        if len(self.styles) == 0:
            return ""
        
        output = ' class="'
        firstLoop = True
        for style in self.styles:
            if firstLoop:
                firstLoop = False
            else:
                output += " "
            output += style
        
        output += '"'

        return output
