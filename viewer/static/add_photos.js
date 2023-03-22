$(document).ready(function() {
  $("#addPhotoBtn").click(function() {
    $("#photoContainer").append(
      '<div class="form-group">' +
        '<label for="photo">Photo link:</label>' +
        '<input type="text" class="form-control" name="photos[]">' +
      '</div>'
    );
  });
  $("#removePhotoBtn").click(function() {
    if ($("#photoContainer .form-group").length > 1) {
      $("#photoContainer .form-group").last().remove();
    }
  });
});