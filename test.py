import pythml

htmlLocation = "test.html"
cssLocation = "test.css"

test = pythml.Page()

parStyle = pythml.TextStyle("p")
parStyle.setTextColor(pythml.Color(255, 0, 0))

par = pythml.ParagraphBlock()


par.addText("IDK")

test.addBlock(par)
test.addBlock(par)
test.addStyle(parStyle)



html = open(htmlLocation, "w")

html.write(test.compileHTML(cssLocation))

html.close()

css = open(cssLocation, "w")

css.write(test.compileCSS())

css.close()
