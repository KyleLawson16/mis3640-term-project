def getSiteHeight():
    return window.innerHeight

def getSiteWidth():
    return window.innerWidth

def foundWaldo():
    alert('found waldo')

def createPerson(size, isWaldo=False):
    top = Math.random() * getSiteHeight()
    left = Math.random() * getSiteWidth()
    person = document.createElement('DIV')
    person.style.width = size + 'px'
    person.style.height = size + 'px'
    person.style.position = 'absolute'
    person.style.top = top + 'px'
    person.style.left = left + 'px'
    person.style.zIndex = '9999'

    if isWaldo:
        person.style.background = 'green'
        person.onclick = def(event):
            foundWaldo()
    else:
        person.style.background = 'red'
    return person

def populateFakes(amt):
    fakeContainer = document.createElement('DIV')
    for i in range(amt):
        fake = createPerson(10)
        fakeContainer.appendChild(fake)
    return fakeContainer

# def createFakes():




document.body.appendChild(createPerson(10, True))
document.body.appendChild(populateFakes(300))
