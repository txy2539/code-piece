    // Fix caldera form issue. submit seems not work when using advanced file uploader 

    $(document).ready(function(){
        $(".button").mouseup(function(){
            setTimeout(function(){
                var uploadDisplay = $(".cf-uploader-trigger").css('display');
                if(uploadDisplay == 'none') {
                    $(".caldera-grid").addClass("cf_processing");
                }
            }, 1000);
        });

        // Fix FF cursor not start at the end.
        $("#fld_2007293_1").click(function(){
            var copyValue = $("#fld_2007293_1").val();
            $("#fld_2007293_1").val("").val(copyValue);
        });
    });