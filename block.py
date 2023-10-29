

class Block:
    backgroundColor = [5, 5, 5]
    classes = []

    def addStyle(self, style):
        self.classes.append(style.getClassName())
    
    def getClasses(self):
        if len(self.classes) == 0:
            return ""
        
        output = ' class="'
        firstLoop = True
        for className in self.classes:
            if firstLoop:
                firstLoop = False
            else:
                output += " "
            output += className
        
        output += '"'

        return output
