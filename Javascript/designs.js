//making all important items available

var color = document.getElementById("colorPicker");
var width = document.getElementById("inputWidth");
var height = document.getElementById("inputHeight");
var table = document.getElementById("pixelCanvas");

//prevent height and width from resetting on submit
sizePicker.addEventListener("submit", function(event){
  event.preventDefault();
  table.innerHTML = "";

  makeGrid(height.value,width.value);
  
});

function makeGrid(height, width){

  //loops to create columns and rows.
  for (var i = 1; i <= height; i++){
    var row = document.createElement("tr");
    table.appendChild(row);
    for (var j = 1; j <= width; j++){
      cell = row.appendChild(document.createElement("td"))
    }
  }
  //ability to change the canvas boxes
  table.addEventListener('click', function(event){
    cell = event.target;
    cell.style.backgroundColor = color.value;
  });
}