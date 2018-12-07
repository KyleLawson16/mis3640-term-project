##########################
# HELPER FUNCTIONS
##########################
def get_site_dimensions():
    '''
    Returns width and height of the website window
    '''
    nonlocal photo_size
    return window.innerWidth - photo_size, window.innerHeight - photo_size

def get_img_url_string(index):
    '''
    returns a string with correct number of leading zeros
    ---
    index: int -- img number
    '''
    if index < 9:
        return '00' + (index + 1)
    elif index < 99:
        return '0' + (index + 1)
    else:
        return (index + 1)

def get_random_position():
    '''
    Returns random position for img that isn't behind timer box
    '''
    site_width, site_height = get_site_dimensions()
    # generate random positions
    left = Math.random() * site_width
    top = Math.random() * site_height
    if left > site_width - 250 and top < 150:
        # if position is behind timer box than recursively call itself until it isn't
        return get_random_position()
    else:
        return top, left


##########################
# CONTROL BOX
##########################
timer = None
current_time = 0
paused = False
finished = False

def create_timer_div():
    '''
    Creates div that holds the timer and button
    '''
    timer = document.createElement('DIV')
    timer.style.width = '200px'
    timer.style.padding = '20px'
    timer.style.textAlign = 'center'
    timer.style.position = 'absolute'
    timer.style.top = 0
    timer.style.right = 0
    timer.style.zIndex = '9999'
    timer.style.backgroundColor = 'rgb(38,168,232)'
    timer.id = 'waldo-timer-div'
    return timer

def create_timer_text():
    '''
    creates paragraph that holds the timer text
    '''
    timer_text = document.createElement('p')
    timer_text.style.color = 'white'
    timer_text.style.fontSize = '25px'
    timer_text.style.marginBottom = '10px'
    timer_text.innerText = '0.00'
    timer_text.id = 'waldo-timer-text'
    return timer_text

def create_timer_btn():
    '''
    creates the timer button
    '''
    nonlocal paused
    timer_btn = document.createElement('button')
    timer_btn.style.width = '100%'
    timer_btn.style.height = '40px'
    timer_btn.style.backgroundColor = 'white'
    timer_btn.style.border = 'none'
    timer_btn.style.borderRadius = '5px'
    timer_btn.innerText = 'Pause'
    timer_btn.id = 'waldo-timer-btn'
    # Set click event handler to trigger timer_btn_click function
    timer_btn.onclick = def(event):
        timer_btn_click()
    return timer_btn

def tick():
    '''
    recursive function that increases the timer text by 0.02 every 20 ms
    '''
    nonlocal timer
    nonlocal paused
    nonlocal current_time
    # First clear the previous timeout
    clearTimeout(timer)
    # Check that it's not paused
    if not paused:
        current_time += 0.02
        timer_text = document.getElementById('waldo-timer-text')
        timer_text.innerText = current_time.toFixed(2)
        # Set recursive function to be called
        new_tick = def():
            tick(current_time)
        # Set a timeout that will call that function in 20 ms
        timer = setTimeout(new_tick, 20)

def start_timer(restart=False):
    '''
    Starts the timer from 0
    ---
    restart: boolean -- if it's the first game than create the timer box
    '''
    nonlocal current_time
    nonlocal photo_size
    nonlocal photo_count
    nonlocal waldo_url
    current_time = 0
    if not restart:
        # Create timer box
        timer_div = create_timer_div()
        timer_text = create_timer_text()
        timer_btn = create_timer_btn()
        timer_div.appendChild(timer_text)
        timer_div.appendChild(timer_btn)
        document.body.appendChild(timer_div)
    # Add all images to website
    create_and_append_images(photo_size, photo_count, waldo_url)
    # Begin recursive function
    tick()

def timer_btn_click():
    '''
    Called when btn in timer box is clicked
    ---
    Three possible conditions:
    1. finished -- game has been completed and needs to restart on click
    2. paused -- game is currently paused and needs to resume on click
    3. running -- game is currently running and needs to pause on click
    '''
    nonlocal timer
    nonlocal paused
    nonlocal finished
    timer_btn = document.getElementById('waldo-timer-btn')
    timer_text = document.getElementById('waldo-timer-text')
    if finished:
        finished = False
        paused = False
        timer_btn.innerText = 'Pause'
        timer_text.style.fontSize = '25px'
        # Remove Waldo Image
        waldo = document.getElementById('waldo')
        document.body.removeChild(waldo)
        start_timer(True)

    elif paused:
        paused = False
        timer_btn.innerText = 'Pause'
        tick()
        # Unhide Pokemon and Waldo
        waldo = document.getElementById('waldo')
        fake_container = document.getElementById('fake-container')
        waldo.style.display = 'block'
        fake_container.style.display = 'block'

    else:
        paused = True
        timer_btn.innerText = 'Continue'
        clearTimeout(timer)
        # Hide Pokemon and Waldo
        waldo = document.getElementById('waldo')
        fake_container = document.getElementById('fake-container')
        waldo.style.display = 'none'
        fake_container.style.display = 'none'


##########################
# IMAGES ON SITE
##########################
# Defaults
photo_size = 50
photo_count = 100
waldo_url = 'https://s3.amazonaws.com/mis3640/lizhinobackground.png'

def create_img(size, index, is_waldo=False):
    '''
    Creates div element with background image of pokemon or waldo
    ---
    size: int -- width and height of image in pixels
    index: int -- number photo in total
    is_waldo: boolean -- whether or not it is the waldo img
    '''
    nonlocal waldo_url
    console.log(waldo_url)
    # Randomly generate position of img
    top, left = get_random_position()
    # Create img div
    img = document.createElement('DIV')
    img.style.width = size + 'px'
    img.style.height = size + 'px'
    img.style.position = 'absolute'
    img.style.top = top + 'px'
    img.style.left = left + 'px'
    img.style.zIndex = '999'
    img.style.backgroundSize = 'cover'
    if is_waldo:
        img.id = 'waldo'
        img.style.zIndex = '9999'
        img.style.backgroundImage = 'url("' + waldo_url + '")'
        # Set click event handler so that found_waldo function is called when clicked
        img.onclick = def(event):
            found_waldo()
    else:
        # generate correct img url based on index of img
        photo_number = get_img_url_string(index)
        img.style.backgroundImage = 'url("https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + photo_number + '.png")'
    return img

def create_fakes(amt):
    '''
    Creates all of the fake images requested
    ---
    amt: int -- number of fake imgs to be created
    '''
    nonlocal photo_size
    # Create a container to store them in
    fake_container = document.createElement('DIV')
    fake_container.id = 'fake-container'
    for i in range(amt):
        # Create each img and store it in container
        fake = create_img(photo_size, i)
        fake_container.appendChild(fake)
    return fake_container

def create_and_append_images(photo_size, photo_count, waldo_url):
    '''
    Calls create functions and actually appends them to the DOM
    '''
    document.body.appendChild(create_img(photo_size, 1, True))
    document.body.appendChild(create_fakes(photo_count))

def found_waldo():
    '''
    Called when a user clicks on correct image.
    ---
    Removes all images besides correct one and updates timer text to display a win message.
    '''
    nonlocal current_time
    nonlocal paused
    nonlocal finished
    # Remove all fakes
    fake_container = document.getElementById('fake-container')
    document.body.removeChild(fake_container)
    paused = True
    finished = True
    # Stop timer
    clearTimeout(timer)
    # Update text
    message = 'Winner! You found the correct image in ' + current_time.toFixed(2) + ' seconds!'
    timer_text = document.getElementById('waldo-timer-text')
    timer_btn = document.getElementById('waldo-timer-btn')
    timer_text.style.fontSize = '14px'
    timer_text.innerText = message
    timer_btn.innerText = 'Play again!'


##########################
# MESSAGE LISTENER
##########################
chrome.runtime.onMessage.addListener( def(request, sender, sendResponse):
    nonlocal photo_size
    nonlocal photo_count
    nonlocal waldo_url
    # If message received from extension
    if request.type == "start":
        # Send a response so that extension knows to close window
        sendResponse({message: "started"})
        # Update all default values
        photo_size = request.message['photo_size']
        photo_count = request.message['photo_count']
        if request.message['waldo_url']:
            waldo_url = request.message['waldo_url']
        # Start the timer
        start_timer()
)
