/* This file was auto-generated using RapydScript */
(function(){
createWaldo = function() {
  var div;
  div = $("<div></div>");
  div.css("background", "green");
  div.css("width", "50px");
  div.css("height", "50px");
  return div[0];
};

waldo = createWaldo().outerHTML;
populateWaldo = function(waldo) {
  console.log(window.document);
};

populateWaldo(waldo);

}());