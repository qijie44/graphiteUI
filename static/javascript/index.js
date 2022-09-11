$(function() {
  $('button').on('click', function() {
    $.getJSON($SCRIPT_ROOT + '/_command', {
      command: $(this).attr('id')
    }, function(data) {
      $("#received-command").text(data.command);
    });
    return false;
  });

  $('input#Tape-Exfoliation').on('input', function() {
    $.getJSON($SCRIPT_ROOT + '/_tape-exfoliation', {
      times: $(this).val()
    });
    return false;
  });

  $('input#Substrate-Exfoliation').on('input', function() {
    $.getJSON($SCRIPT_ROOT + '/_substrate-exfoliation', {
      times: $(this).val()
    });
    return false;
  });

  $('input#Substrate-No').on('input', function() {
    $.getJSON($SCRIPT_ROOT + '/_substrate-no', {
      value: $(this).val()
    });
    return false;
  });

  $('input#Movement-Speed').on('input', function() {
    $.getJSON($SCRIPT_ROOT + '/_movement-speed', {
      value: $(this).val()
    });
    return false;
  });

});

window.setInterval(function() {
  $.getJSON($SCRIPT_ROOT + '/_progress', {
    command: $(this).attr('id')
  }, function(data) {
    $("#Progress-Bar").val(data.value);
  });
}, 5000);