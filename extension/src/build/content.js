/* This file was auto-generated using RapydScript */
(function(){
getSiteHeight = function() {
  return window.innerHeight;
};

getSiteWidth = function() {
  return window.innerWidth;
};

foundWaldo = function() {
  alert("found waldo");
};

createPerson = function(size, isWaldo) {
  var left, person, top;
  if (typeof isWaldo === "undefined") {isWaldo = false};
  top = (Math.random() * getSiteHeight());
  left = (Math.random() * getSiteWidth());
  person = document.createElement("DIV");
  person.style.width = (size + "px");
  person.style.height = (size + "px");
  person.style.position = "absolute";
  person.style.top = (top + "px");
  person.style.left = (left + "px");
  person.style.zIndex = "9999";
  if (isWaldo) {
    person.style.background = "green";
    person.onclick = (function(event) {
      foundWaldo();
    });
  } else {
    person.style.backgroundImage = "url(\"001.png\")";
  }

  return person;
};

populateFakes = function(amt) {
  var fake, fakeContainer, i;
  fakeContainer = document.createElement("DIV");
  for (i = 0; i < amt; i++) {
    fake = createPerson(10);
    fakeContainer.appendChild(fake);
  }

  return fakeContainer;
};

document.body.appendChild(createPerson(10, true));
document.body.appendChild(populateFakes(300));

}());