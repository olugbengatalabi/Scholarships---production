$('#chooseFile').bind('change', function () {
  var filename = $("#chooseFile").val();
  if (/^\s*$/.test(filename)) {
    $(".file-upload").removeClass('active');
    $("#noFile").text("No file chosen...");
  } else {
    $(".file-upload").addClass('active');
    $("#noFile").text(filename.replace("C:\\fakepath\\", ""));
  }
});
$('#chooseFile2').bind('change', function () {
  var filename = $("#chooseFile2").val();
  if (/^\s*$/.test(filename)) {
    $(".file-upload2").removeClass('active');
    $("#noFile2").text("No file chosen...");
  } else {
    $(".file-upload2").addClass('active');
    $("#noFile2").text(filename.replace("C:\\fakepath\\", ""));
  }
});
$('#chooseFile3').bind('change', function () {
  var filename = $("#chooseFile3").val();
  if (/^\s*$/.test(filename)) {
    $(".file-upload3").removeClass('active');
    $("#noFile3").text("No file chosen...");
  } else {
    $(".file-upload3").addClass('active');
    $("#noFile3").text(filename.replace("C:\\fakepath\\", ""));
  }
});
