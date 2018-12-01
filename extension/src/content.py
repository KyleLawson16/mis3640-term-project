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
    alert('found waldo')

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
        person.style.backgroundImage = 'url("https://assets.pokemon.com/assets/cms2/img/pokedex/detail/00")'
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
    return fake_container

# def createFakes():


# Constants
photo_size = 40
number_of_fakes = 200

document.body.appendChild(create_person(photo_size, 1, True))
document.body.appendChild(populate_fakes(number_of_fakes))
