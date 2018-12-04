/* This file was auto-generated using RapydScript */
(function(){
get_site_dimensions = function() {
  
  return [(window.innerWidth - photo_size), (window.innerHeight - photo_size)];
};

get_img_url_string = function(index) {
  if ((index < 9)) {
    return ("00" + (index + 1));
  } else if ((index < 99)) {
    return ("0" + (index + 1));
  } else {
    return (index + 1);
  }

};

get_random_position = function() {
  var _$rapyd_tuple$_, left, site_height, site_width, top;
  _$rapyd_tuple$_ = get_site_dimensions();
  site_width = _$rapyd_tuple$_[0];
  site_height = _$rapyd_tuple$_[1];
  left = (Math.random() * site_width);
  top = (Math.random() * site_height);
  if (((left > (site_width - 250)) && (top < 150))) {
    return get_random_position();
  } else {
    return [top, left];
  }

};

timer = null;
current_time = 0;
paused = false;
finished = false;
create_timer_div = function() {
  var timer;
  timer = document.createElement("DIV");
  timer.style.width = "200px";
  timer.style.padding = "20px";
  timer.style.textAlign = "center";
  timer.style.position = "absolute";
  timer.style.top = 0;
  timer.style.right = 0;
  timer.style.zIndex = "9999";
  timer.style.backgroundColor = "rgb(38,168,232)";
  timer.id = "waldo-timer-div";
  return timer;
};

create_timer_text = function() {
  var timer_text;
  timer_text = document.createElement("p");
  timer_text.style.color = "white";
  timer_text.style.fontSize = "25px";
  timer_text.style.marginBottom = "10px";
  timer_text.innerText = "0.00";
  timer_text.id = "waldo-timer-text";
  return timer_text;
};

create_timer_btn = function() {
  var timer_btn;
  
  timer_btn = document.createElement("button");
  timer_btn.style.width = "100%";
  timer_btn.style.height = "40px";
  timer_btn.style.backgroundColor = "white";
  timer_btn.style.border = "none";
  timer_btn.style.borderRadius = "5px";
  timer_btn.innerText = "Pause";
  timer_btn.id = "waldo-timer-btn";
  timer_btn.onclick = (function(event) {
    timer_btn_click();
  });
  return timer_btn;
};

tick = function() {
  var new_tick, timer_text;
  
  
  
  clearTimeout(timer);
  if ((!paused)) {
    current_time += 0.02;
    timer_text = document.getElementById("waldo-timer-text");
    timer_text.innerText = current_time.toFixed(2);
    new_tick = (function() {
      tick(current_time);
    });
    timer = setTimeout(new_tick, 20);
  }

};

start_timer = function(restart) {
  var timer_btn, timer_div, timer_text;
  if (typeof restart === "undefined") {restart = false};
  
  
  
  
  current_time = 0;
  if ((!restart)) {
    timer_div = create_timer_div();
    timer_text = create_timer_text();
    timer_btn = create_timer_btn();
    timer_div.appendChild(timer_text);
    timer_div.appendChild(timer_btn);
    document.body.appendChild(timer_div);
  }

  create_and_append_images(photo_size, photo_count, waldo_url);
  tick();
};

timer_btn_click = function() {
  var fake_container, timer_btn, timer_text, waldo;
  
  
  
  timer_btn = document.getElementById("waldo-timer-btn");
  timer_text = document.getElementById("waldo-timer-text");
  if ((finished == true)) {
    finished = false;
    paused = false;
    timer_btn.innerText = "Pause";
    timer_text.style.fontSize = "25px";
    waldo = document.getElementById("waldo");
    document.body.removeChild(waldo);
    start_timer(true);
  } else if ((paused == true)) {
    paused = false;
    timer_btn.innerText = "Pause";
    tick();
    waldo = document.getElementById("waldo");
    fake_container = document.getElementById("fake-container");
    waldo.style.display = "block";
    fake_container.style.display = "block";
  } else {
    paused = true;
    timer_btn.innerText = "Continue";
    clearTimeout(timer);
    waldo = document.getElementById("waldo");
    fake_container = document.getElementById("fake-container");
    waldo.style.display = "none";
    fake_container.style.display = "none";
  }

};

photo_size = 50;
photo_count = 100;
waldo_url = "https://s3.amazonaws.com/mis3640/lizhinobackground.png";
create_img = function(size, index, is_waldo) {
  var _$rapyd_tuple$_, img, left, photo_number, top;
  if (typeof is_waldo === "undefined") {is_waldo = false};
  
  console.log(waldo_url);
  _$rapyd_tuple$_ = get_random_position();
  top = _$rapyd_tuple$_[0];
  left = _$rapyd_tuple$_[1];
  img = document.createElement("DIV");
  img.style.width = (size + "px");
  img.style.height = (size + "px");
  img.style.position = "absolute";
  img.style.top = (top + "px");
  img.style.left = (left + "px");
  img.style.zIndex = "999";
  img.style.backgroundSize = "cover";
  if (is_waldo) {
    img.id = "waldo";
    img.style.zIndex = "9999";
    img.style.backgroundImage = (("url(\"" + waldo_url) + "\")");
    img.onclick = (function(event) {
      found_waldo();
    });
  } else {
    photo_number = get_img_url_string(index);
    img.style.backgroundImage = (("url(\"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/" + photo_number) + ".png\")");
  }

  return img;
};

create_fakes = function(amt) {
  var fake, fake_container, i;
  
  fake_container = document.createElement("DIV");
  for (i = 0; i < amt; i++) {
    fake = create_img(photo_size, i);
    fake_container.appendChild(fake);
    fake_container.id = "fake-container";
  }

  return fake_container;
};

create_and_append_images = function(photo_size, photo_count, waldo_url) {
  document.body.appendChild(create_img(photo_size, 1, true));
  document.body.appendChild(create_fakes(photo_count));
};

found_waldo = function() {
  var fake_container, message, timer_btn, timer_text;
  
  
  
  fake_container = document.getElementById("fake-container");
  document.body.removeChild(fake_container);
  paused = true;
  finished = true;
  clearTimeout(timer);
  message = (("Winner! You found the correct image in " + current_time.toFixed(2)) + " seconds!");
  timer_text = document.getElementById("waldo-timer-text");
  timer_btn = document.getElementById("waldo-timer-btn");
  timer_text.style.fontSize = "14px";
  timer_text.innerText = message;
  timer_btn.innerText = "Play again!";
};

chrome.runtime.onMessage.addListener((function(request, sender, sendResponse) {
  
  
  
  if ((request.type == "start")) {
    sendResponse({
      message: "started"
    });
    photo_size = request.message["photo_size"];
    photo_count = request.message["photo_count"];
    if (request.message["waldo_url"]) {
      waldo_url = request.message["waldo_url"];
    }

    start_timer();
  }

}));

}());