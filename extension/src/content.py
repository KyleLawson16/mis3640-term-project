def get_response(response):
    console.log(response)

def send_message(type, message):
    chrome.runtime.sendMessage({type: type, message: message}, def(response):
        get_response(response)
    )

def get_site_height():
    return window.innerHeight - photo_size

def get_site_width():
    return window.innerWidth - photo_size

def get_photo_number(index):
    if index < 9:
        return '00' + (index + 1)
    elif index < 99:
        return '0' + (index + 1)
    else:
        return (index + 1)

def found_waldo():
    send_message('winner', 'You found Professor Li!')



def create_person(size, index, is_waldo=False):
    top = Math.random() * get_site_height()
    left = Math.random() * get_site_width()
    person = document.createElement('DIV')
    person.style.width = size + 'px'
    person.style.height = size + 'px'
    person.style.position = 'absolute'
    person.style.top = top + 'px'
    person.style.left = left + 'px'
    person.style.zIndex = '9999'
    person.style.backgroundSize = 'cover'

    if is_waldo:
        person.id = 'waldo'
        person.style.backgroundImage = 'url("https://s3.amazonaws.com/mis3640/lizhinobackground.png")'
        person.onclick = def(event):
            found_waldo()

    else:
        photo_number = get_photo_number(index)
        person.style.backgroundImage = 'url("https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + photo_number + '.png")'

    return person

def populate_fakes(amt):
    fake_container = document.createElement('DIV')
    for i in range(amt):
        fake = create_person(photo_size, i)
        fake_container.appendChild(fake)
        fake_container.id = 'fake-container'
    return fake_container

# def createFakes():

# Constants
photo_size = 50
number_of_fakes = 100

chrome.runtime.onMessage.addListener( def(request, sender, sendResponse):
    if request.type == "start":
        sendResponse({message: "started"})
        document.body.appendChild(create_person(photo_size, 1, True))
        document.body.appendChild(populate_fakes(number_of_fakes))

    if request.type == "pause":
        sendResponse({message: "paused"})
        waldo = document.getElementById('waldo')
        fake_container = document.getElementById('fake-container')
        waldo.style.display = 'none'
        fake_container.style.display = 'none'

    if request.type == "continue":
        sendResponse({message: "continue"})
        waldo = document.getElementById('waldo')
        fake_container = document.getElementById('fake-container')
        waldo.style.display = 'block'
        fake_container.style.display = 'block'

    if request.type == "winner":
        sendResponse({message: "winner"})
        waldo = document.getElementById('waldo')
        fake_container = document.getElementById('fake-container')
        document.body.removeChild(waldo)
        document.body.removeChild(fake_container)
        alert(request.message)
)
