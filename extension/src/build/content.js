/* This file was auto-generated using RapydScript */
(function(){
get_site_height = function() {
  return (window.innerHeight - photoSize);
};

get_site_width = function() {
  return (window.innerWidth - photoSize);
};

get_photo_number = function(index) {
  if ((index < 9)) {
    return ("00" + (index + 1));
  } else if ((index < 99)) {
    return ("0" + (index + 1));
  } else {
    return (index + 1);
  }

};

found_waldo = function() {
  alert("found waldo");
};

create_person = function(size, index, isWaldo) {
  var left, person, photoNumber, top;
  if (typeof isWaldo === "undefined") {isWaldo = false};
  top = (Math.random() * get_site_height());
  left = (Math.random() * get_site_width());
  person = document.createElement("DIV");
  person.style.width = (size + "px");
  person.style.height = (size + "px");
  person.style.position = "absolute";
  person.style.top = (top + "px");
  person.style.left = (left + "px");
  person.style.zIndex = "9999";
  if (isWaldo) {
    person.style.backgroundImage = "url(\"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/00\")";
    person.onclick = (function(event) {
      found_waldo();
    });
  } else {
    photoNumber = get_photo_number(index);
    person.style.backgroundImage = (("url(\"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/" + photoNumber) + ".png\")");
    person.style.backgroundSize = "cover";
  }

  return person;
};

populate_fakes = function(amt) {
  var fake, fakeContainer, i;
  fakeContainer = document.createElement("DIV");
  for (i = 0; i < amt; i++) {
    fake = create_person(photoSize, i);
    fakeContainer.appendChild(fake);
  }

  return fakeContainer;
};

photoSize = 40;
document.body.appendChild(create_person(photoSize, 1, true));
document.body.appendChild(populate_fakes(200));

}());