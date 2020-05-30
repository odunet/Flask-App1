window.onload = function(){
var createTodo = function(todo) {
  var lst = document.createElement('li');
  var inp = document.createElement('INPUT');
  inp.setAttribute('type','checkbox');
  //inp.setAttribute('name','ayo');
  lst.appendChild(inp);
  var lbl = document.createElement('label');
  var para = document.createElement('p');
  lst.appendChild(lbl);
  lbl.appendChild(para);
  para.innerHTML = todo.value;
  var btn = document.createElement('button');
  btn.setAttribute('class','delete');
  var par = document.createElement('p');
  par.innerHTML = 'Delete'
  btn.innerHTML = par.innerHTML;
  lst.appendChild(btn);

  btn.onclick = function() {
    lst.parentNode.removeChild(lst);
  }

  inp.onchange = function(){
  lst.classList.toggle('checked')}
  //lst.style.textDecoration = 'line-through'};

  return lst;

}



var ul = document.querySelector('#todoList');

document.getElementById('add').onclick = function() {

  var todos = document.querySelector('#newTodo');
  // store the button's parent element (.addTodo <div>) in a variable
  var parent = this.parentNode;
  // store the input, which is the *first* child element of the .addTodo <div>
  var input = parent.children[0];
  var ln = document.createElement('li');
  ln = createTodo(todos);
  if (todos.value === ''){
    var yy = document.querySelector('h1');
    yy.innerHTML = 'You did not type anything';
    yy.style.color = 'red';
    setTimeout(function(){
      yy.innerHTML = 'To-Dos';
      yy.style.color = 'black'},3000);
  }else{
   ul.appendChild(ln);
  }
  input.value = '';
  input.placeholder = 'Next Value';
  event.preventDefault();

}
}
