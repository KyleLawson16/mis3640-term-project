/* This file was auto-generated using RapydScript */
(function(){
get_response = function(response) {
  console.log(response);
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

start_timer = function() {
  tick();
};

timer = null;
paused = false;
started = false;
clicked = false;
current_time = 0;
tick = function() {
  var new_tick;
  
  
  
  clearTimeout(timer);
  if ((paused == false)) {
    current_time += 0.02;
    timer = document.getElementById("timer");
    timer.innerText = parseFloat(current_time).toFixed(2);
    new_tick = (function() {
      tick(current_time);
    });
    timer = setTimeout(new_tick, 20);
  }

};

start_btn = document.getElementById("start-btn");
start_btn.onclick = (function(event) {
  
  
  
  
  if ((!clicked)) {
    if ((!started)) {
      started = true;
      send_message("start", "start button clicked");
    } else {
      send_message("continue", "continue button clicked");
    }

    paused = false;
    clicked = true;
    start_btn.innerText = "Stop";
    start_timer();
  } else {
    send_message("pause", "pause button clicked");
    paused = true;
    clicked = false;
    start_btn.innerText = "Continue";
    clearTimeout(timer);
  }

});
chrome.runtime.onMessage.addListener((function(request, sender, sendResponse) {
  
  
  console.log(request);
  if ((request.type == "winner")) {
    send_message("winner", (("You found Professor Li in " + parseFloat(current_time).toFixed(2)) + " seconds!"));
    paused = true;
    start_btn.style.display = "none";
    clearTimeout(timer);
  }

}));

}());