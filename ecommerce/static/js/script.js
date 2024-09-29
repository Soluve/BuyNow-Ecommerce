const buttons = document.querySelectorAll('.btn-success');

buttons.forEach(button => {
  button.addEventListener('click', () => {
    button.classList.add('clicked');
  });
});
buttons.forEach(button => {
  button.addEventListener('mouseup', () => {
    button.classList.add('clicked');
  });
});
