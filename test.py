import pythml

htmlLocation = "test.html"
cssLocation = "test.css"

test = pythml.Page()
test.addGoogleFont("Audiowide")
test.addGoogleFont("Roboto")

parStyle = pythml.TextStyle()
# parStyle.addElementSelector("p")
parStyle.setTextColor(pythml.Color(255, 0, 0))
parStyle.addShadow(2, 2, pythml.Color(255, 0, 100), 5)
parStyle.addFont("Audiowide")
parStyle.setFontSize(20, "px")
parStyle.setLetterSpacing(10)


par = pythml.ParagraphElement()

par.addStyle(parStyle)
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
