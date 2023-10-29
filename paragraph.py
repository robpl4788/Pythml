import block

class ParagraphElement(block.Block):
    content = []

    def addText(self, newText : str):
        self.content.append(newText)
    

    def compileHTML(self):
        html = "<p>"

        for text in self.content:
            html += text

        html += "</p>"

        return html

class ParagraphBlock:
    paragrah = ParagraphElement()

    def addText(self, newText : str):
        self.paragrah.addText(newText)
    
    def compileHTML(self):
        return self.paragrah.compileHTML()


