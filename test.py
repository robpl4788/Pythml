import pythml

htmlLocation = "test.html"
cssLocation = "test.css"

test = pythml.Page("images")
test.addGoogleFont("Audiowide")
test.addGoogleFont("Roboto")

parStyle = pythml.Style()
# parStyle.addElementSelector("p")
parStyle.text.setTextColor(pythml.Color(255, 0, 0))
parStyle.text.addTextShadow(2, 2, pythml.Color(255, 0, 100), 5)
parStyle.text.addFont("Audiowide")
parStyle.text.setFontSize(40, "px")
parStyle.text.setLetterSpacing(10)

im = pythml.Image("images/logowoo.png", "a logo")
imStyle = pythml.Style()
imStyle.setWidth(100, "vw")

im.addStyle(imStyle)


par = pythml.ParagraphElement()

# par.addStyle(parStyle)
par.addText("IDK")
par.addText(" other", parStyle)
par.addLink(" link?", "https://www.firestorm.industries")

test.addBlock(par)
test.addBlock(par)
test.addBlock(im)

test.addStyle(parStyle)
test.addStyle(imStyle)

html = open(htmlLocation, "w")

html.write(test.compileHTML(cssLocation))

html.close()

css = open(cssLocation, "w")

css.write(test.compileCSS())

css.close()
