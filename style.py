
class Style:
    usedClasses = []
    universal = False
    properties = {}

    def __init__(self) -> None:
        if len(self.usedClasses) == 0:
            self.className = "a0"
        else:
            num = int(self.usedClasses[-1][1:])
            self.className = "a" + str(num + 1)
        self.usedClasses.append(self.className)
        self.selectors = [self.className]

    def beginCSScompile(self):
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
        
        return output

    def addElementSelector(self, newElement):
        self.selectors.append(str(newElement))
    
    def setUniversal(self):
        self.selectors.append("*")
    
    def getClassName(self):
        return self.className

    

