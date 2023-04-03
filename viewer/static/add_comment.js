document.addEventListener("DOMContentLoaded", () => {
  const commentButton = document.querySelector('.comment-button');
  const commentForm = document.querySelector('.card-footer.py-3.border-0#comment-form');
  const cancelButton = commentForm.querySelector('.btn-outline-dark');

  commentButton.addEventListener('click', () => {
    commentForm.classList.toggle('d-none');
  });

  cancelButton.addEventListener('click', () => {
    commentForm.classList.add('d-none');
  });
});