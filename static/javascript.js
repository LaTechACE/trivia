$('.obcus').change(function(e){
  $("#"+($(this).attr('target'))).css("color",((this.checked)?"white":"black"));
});
