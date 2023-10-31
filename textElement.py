import element
from constants import validLinkTargets



class TextElement(element.Element):
    def __init__(self, type) -> None:
        super().__init__()
        validTextElements = ["p", "h1", "h2", "h3", "h4", "h5", "h6"]

        if type in validTextElements:
            self.type = type
        else:
            print("WARNING: " + str(type) + " is not a valid text element type, using p")
            self.type = "p"

        self.content = []
        self.links = []
        self.targets = []
        self.textStyles = []

    def addText(self, newText : str, style = None):
        self.content.append(str(newText))
        self.links.append(None)
        self.targets.append(None)
        if style != None:
            self.textStyles.append(style.getClassName())
        else:
            self.textStyles.append(None)

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
            self.textStyles.append(style.getClassName())
        else:
            self.textStyles.append(None)
        



    def compileHTML(self):
        html = "<"
        html += self.type
        html += self.getStyles()
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
                if self.textStyles[i] != None:
                    html += ' class="'
                    html += self.textStyles[i]
                    html += '"'
                html += '>'

                html += self.content[i]
                html += "</a>"
            
            elif self.textStyles[i] != None:
                html += '<span class="'
                html += self.textStyles[i]
                html += '">'
                html += self.content[i]
                html += "</span>"
            
            else:
                html += self.content[i]
                

        html += "</"
        html += self.type
        html += ">"

        return html

class ParagraphElement(TextElement):
    def __init__(self) -> None:
        super().__init__("p")

class Header1Element(TextElement):
    def __init__(self) -> None:
        super().__init__("h1")

class Header2Element(TextElement):
    def __init__(self) -> None:
        super().__init__("h2")

class Header3Element(TextElement):
    def __init__(self) -> None:
        super().__init__("h3")

class Header4Element(TextElement):
    def __init__(self) -> None:
        super().__init__("h4")

class Header5Element(TextElement):
    def __init__(self) -> None:
        super().__init__("h5")

class Header6Element(TextElement):
    def __init__(self) -> None:
        super().__init__("h6")


