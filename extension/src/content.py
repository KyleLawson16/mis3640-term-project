
def createWaldo():
    waldo = document.createElement('DIV')
    waldo.style.background = 'green'
    waldo.style.width = '50px'
    waldo.style.height = '50px'
    waldo.style.position = 'absolute'
    waldo.style.top = '0'
    waldo.style.left = '0'
    waldo.style.zIndex = '9999'
    return div

# waldo = createWaldo()


document.body.appendChild(createWaldo(waldo))
