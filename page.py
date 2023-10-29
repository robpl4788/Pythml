import block

class Page:
    blocks = []

    def addBlock(self, newBlock : block.Block):
        self.blocks.append(newBlock)

    def compileHTML(self):
        html = """<!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        """


        
        for block in self.blocks:
            html += block.compile()
            html += "\n"
        
        html += """
        </body>
        </html>"""
        
        return html