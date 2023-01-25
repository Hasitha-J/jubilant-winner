// select Season of the year    

$(function () {
    $("#slider").slider({
        value: 2015,
        min: 2015,
        max: 2020,
        step: 1,
        slide: function (event, ui) {
          $("#amount").val(ui.value);
        },
      })
      .each(function () {
        var opt = $(this).data().uiSlider.options;
        var vals = opt.max - opt.min;
        for (var i = 0; i <= vals ; i++) {
          var el = $("<label>" + (i + opt.min) + "</label>").css("left",((i / vals) * 100)-3 + "%");
          $("#slider").append(el);
        }
      });
    $("amount").val(
      $("#slider").slider("value") - 1 + "-" + $("#slider").slider("value")
    );
  });
