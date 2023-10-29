from element import Element

class Image(Element):
    def __init__(self, imageSource, alternateText) -> None:
        super().__init__()
        self.imageSource = str(imageSource)
        self.alternateText = str(alternateText)
    
    def compileHTML(self):
        output = '<img src = "'
        output += self.imageSource
        output += '" alt ="'
        output += self.alternateText
        output += '"'
        if len(self.styles) != 0:
            output += self.getStyles()
        output += '>'

        return output