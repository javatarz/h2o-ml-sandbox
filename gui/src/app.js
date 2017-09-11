$(document).ready(function(){
  $response = $('#responseField');

  function predict() {
    var data = {};

    $('input').each(function(){
      var $field = $(this);
      data[$field.attr('data-column')] = $field.val();
    });

    $('select').each(function(){
      var $field = $(this);
      data[$field.attr('data-column')] = $field.val();
    });

    $.ajax({
      url: 'http://127.0.0.1:8080/score',
      type: 'POST',
      data: JSON.stringify(data),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      async: false,
      success: function(msg) {
        console.log(data);
        if(data.label === '1') {
          $response.text('Declined!');
        } else {
          $response.text('Approved!');
        }
      },
      failure: function(error) {
        console.error(error.responseText ? error.responseText : error);
        $response.text('(Invalid input)');
      }
    });
  }

  var updatePrediction = _.debounce(predict, 250);

  $('input').each(function(){
    $(this).keydown(updatePrediction);
  });

  $('select').each(function(){
    $(this).change(updatePrediction);
  });

  $("form").bind("keypress", function (e) {
    if (e.keyCode === 13) {
      return false;
    }
  });

  updatePrediction();

});

