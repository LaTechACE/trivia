$('.obcus').change(function(e){
  box = this
  console.log(box.checked)
  $("#"+($(box).attr('target'))).css("color",((box.checked)?"white":"black"));
});
