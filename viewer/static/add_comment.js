document.addEventListener("DOMContentLoaded", () => {
  const commentButtons = document.querySelectorAll('.comment-button');
  const commentForms = document.querySelectorAll('.card-footer.py-3.border-0#comment-form');
  const cancelButtons = document.querySelectorAll('.btn-outline-dark');

  commentButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
      commentForms[index].classList.toggle('d-none');
    });

    cancelButtons[index].addEventListener('click', () => {
      commentForms[index].classList.add('d-none');
    });
  });
});