import block

class Page:
    blocks = []
    styles = []

    def addBlock(self, newBlock):
        self.blocks.append(newBlock)
    
    def addStyle(self, newStyle):
        self.styles.append(newStyle)

    def compileHTML(self, stylesheet = None):
        html = """<!DOCTYPE html>
        <html>
        <head>\n"""

        if stylesheet != None:
            html += '<link rel="stylesheet" href = "'
            html += stylesheet
            html += '">\n'

        html += """<title>Page Title</title>
        </head>
        <body> \n"""


        
        for block in self.blocks:
            html += block.compileHTML()
            html += "\n"
        
        html += """
        </body>
        </html>"""
        
        return html
    
    def compileCSS(self):
        output = ""
        for style in self.styles:
            output += style.compileCSS()
        
        return output

