def get_response(response):
    console.log(response)

def send_message(type, message):
    chrome.tabs.query({active: true, currentWindow: true}, def(tabs):
        chrome.tabs.sendMessage(tabs[0].id, {type: type, message: message}, def(response):
            get_response(response)
        )
    )

def start_timer():
    tick()

timer = None
paused = False
started = False
clicked = False
current_time = 0

def tick():
    nonlocal timer
    nonlocal paused
    nonlocal current_time
    clearTimeout(timer)
    if paused == False:
        current_time += 0.02
        timer = document.getElementById('timer')
        timer.innerText = parseFloat(current_time).toFixed(2)
        new_tick = def():
            tick(current_time)
        timer = setTimeout(new_tick, 20)



# Start Btn
start_btn = document.getElementById('start-btn')
start_btn.onclick = def(event):
    nonlocal clicked
    nonlocal paused
    nonlocal timer
    nonlocal started
    if not clicked:
        if not started:
            started = True
            send_message('start', 'start button clicked')
        else:
            send_message('continue', 'continue button clicked')
        paused = False
        clicked = True
        start_btn.innerText = 'Stop'
        start_timer()
    else:
        send_message('pause', 'pause button clicked')
        paused = True
        clicked = False
        start_btn.innerText = 'Continue'
        clearTimeout(timer)


chrome.runtime.onMessage.addListener( def(request, sender, sendResponse):
    nonlocal paused
    nonlocal timer
    console.log(request)
    if request.type == "winner":
        send_message('winner', 'You found Professor Li in ' + parseFloat(current_time).toFixed(2) + ' seconds!')
        paused = True
        start_btn.style.display = 'none'
        clearTimeout(timer)
)
