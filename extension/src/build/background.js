/* This file was auto-generated using RapydScript */
(function(){
get_response = function(response) {
  if ((response.message == "started")) {
    window.close();
  }

};

send_message = function(type, message) {
  chrome.tabs.query({
    active: true,
    currentWindow: true
  }, (function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, {
      type: type,
      message: message
    }, (function(response) {
      get_response(response);
    }));
  }));
};

start_btn = document.getElementById("start-btn");
start_btn.onclick = (function(event) {
  var params, photo_count, photo_size, waldo_url;
  photo_size = document.getElementById("photo-size").value;
  photo_count = document.getElementById("photo-count").value;
  waldo_url = document.getElementById("waldo-url").value;
  params = {
    "photo_size": photo_size,
    "photo_count": photo_count,
    "waldo_url": waldo_url
  };
  send_message("start", params);
});

}());