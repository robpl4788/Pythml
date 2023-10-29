import pythml

test = pythml.Page()

par = pythml.ParagraphBlock()
par.addText("IDK")

test.addBlock(par)
test.addBlock(par)



html = open("test.html", "w")

html.write(test.compileHTML())

html.close()
