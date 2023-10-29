import block
from constants import validLinkTargets

class ParagraphElement(block.Block):
    def __init__(self) -> None:
        super().__init__()
        self.content = []
        self.links = []
        self.targets = []
        self.classNames = []

    def addText(self, newText : str, style = None):
        self.content.append(str(newText))
        self.links.append(None)
        self.targets.append(None)
        if style != None:
            self.classNames.append(style.getClassName())
        else:
            self.classNames.append(None)

    def addLink(self, newText, newLink, target = None, style = None):
        self.content.append(str(newText))
        self.links.append(str(newLink))
        if target in validLinkTargets:
            self.targets.append(str(target))
        else:
            if target != None:
                print("WARNING: " + target + " is an invalid target for a link")
            self.targets.append(None)

        if style != None:
            self.classNames.append(style.getClassName())
        else:
            self.classNames.append(None)
        



    def compileHTML(self):
        html = "<p"
        html += self.getClasses()
        html += ">"

        for i in range(len(self.content)):
            if self.links[i] != None:
                html += '<a href="'
                html += self.links[i]
                html += '"'
                if self.targets[i] != None:
                    html += ' target="'
                    html += self.targets[i]
                    html += '"'
                if self.classNames[i] != None:
                    html += ' class="'
                    html += self.classNames[i]
                    html += '"'
                html += '>'

                html += self.content[i]
                html += "</a>"
            
            elif self.classNames[i] != None:
                html += '<span class="'
                html += self.classNames[i]
                html += '">'
                html += self.content[i]
                html += "</span>"
            
            else:
                html += self.content[i]
                

        html += "</p>"

        return html

class ParagraphBlock:
    def __init__(self) -> None:
        self.paragrah = ParagraphElement()

    def addText(self, newText : str, style = None):
        self.paragrah.addText(newText, style)
    
    def addLink(self, newText :str, newLink : str, target = None, style = None):
        self.paragrah.addLink(newText, newLink, target, style)
    
    def compileHTML(self):
        return self.paragrah.compileHTML()


