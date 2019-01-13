$('.modal').modal({
  dismissible: true,
  inDuration: 300,
  outDuration: 200,
  ready: function(modal, trigger) {}
});

$('deny_modal').modal({
  dismissible: true,
  inDuration: 300,
  outDuration: 200,
  ready: function(modal, trigger) {}
});

$(document).ready(function() {
  $('.dropdown-button').dropdown({
    constrainWidth: false,
    hover: true,
    belowOrigin: true,
    alignment: 'left'
  });

  // JAVASCRIPT START HERE //

  $('.button-collapse').sideNav();

  $('.dropdown-button').dropdown({
    constrainWidth: false,
    hover: true,
    belowOrigin: true,
    alignment: 'left'
  });

  // JAVASCRIPT START HERE //

  // INIT DATEPICKER
  $('.datepicker').pickadate({
    selectMonths: true,
    selectYears: 440,
    closeOnSelect: true
  });

  // INIT TIMEPICKER
  $('.timepicker').pickatime({
    default: 'now',
    twelvehour: true,
    donetext: 'ok',
    cleartext: 'clear',
    canceltext: 'cancel',
    autoclose: true
  });

  // INIT SELECT LIST
  $('select').material_select();

  $('a').hover(function() {
    $(this).css('cursor', 'pointer');
  });
  $('.mso_row').hover(function() {
    // $(this).css('cursor', 'pointer');
    $(this).toggleClass('z-depth-5');
  });
  $('.li').hover(function() {
    // $(this).css('cursor', 'pointer');
    $(this).toggleClass('z-depth-5');
  });

  $('#comment_modal').click(function() {
  });

  $('#cancel_modal').click(function() {
  });
});

$('.approve').click(function(e) {
  // Hide row
  var divId = $(this)
    .parents('.mso_row')
    .attr('id');
  var msoNumber = parseInt(event.target.id);
  Materialize.toast('MSO-' + msoNumber + ' Approved!', 5000);
  e.preventDefault();
  $('#' + divId).toggle(1000, 'swing', function() {});

  // Get Job job title
  var job_title = $('p').text();

  $.getJSON('/mso/approve_mso/' + msoNumber + '/' + job_title, function(data) {
    console.log()
    //do nothing
  });
  return false;
});

$('.mso_request_toast').click(function(e) {
  Materialize.toast(' MSO Requested Successfully', 5000);
  e.preventDefault();
});

$('.delete').click(function(e) {
  // Hide row
  var divId = $(this)
    .parents('.mso_row')
    .attr('id');
  var msoNumber = parseInt(event.target.id);
  Materialize.toast('MSO-' + msoNumber + ' Deleted!', 5000);
  e.preventDefault();
  $('#' + divId).toggle(1000, 'swing', function() {});

  $.getJSON('/mso/delete/' + msoNumber, function(data) {
     //do nothing
   });
   return false;
});

$.ajax({
  url: '/mso/delete/44/',
  datatype: 'json',
  type: 'GET',
  success: function(data) {
      $.each(data.events, function(index, element) {
          $('body').append($('<div>', {
              text: element.name
          }));
      });
  }
});