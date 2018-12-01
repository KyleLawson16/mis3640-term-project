def createWaldo():
    div = $('<div></div>')
    div.css('background', 'green')
    div.css('width', '50px')
    div.css('height', '50px')
    return div[0]

waldo = createWaldo().outerHTML

def populateWaldo(waldo):
    console.log(window.document)


populateWaldo(waldo)


# document.getElementById("result").innerHTML =
