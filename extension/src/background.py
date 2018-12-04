##########################
# MESSAGE FUNCTIONS
##########################
def get_response(response):
    '''
    Response received from content script after sending a message.
    '''
    if response.message == 'started':
        # Close extension window
        window.close()

def send_message(type, message):
    '''
    Finds active chrome tab and sends a message to the content script.
    ---
    type: string -- the type of message being sent
    message: string or dict -- the content of the message
    '''
    chrome.tabs.query({active: true, currentWindow: true}, def(tabs):
        chrome.tabs.sendMessage(tabs[0].id, {type: type, message: message}, def(response):
            get_response(response)
        )
    )


##########################
# START BUTTON
##########################
start_btn = document.getElementById('start-btn')
start_btn.onclick = def(event):
    photo_size = document.getElementById('photo-size').value
    photo_count = document.getElementById('photo-count').value
    waldo_url = document.getElementById('waldo-url').value
    params = {'photo_size': photo_size, 'photo_count': photo_count, 'waldo_url': waldo_url}
    send_message('start', params)
