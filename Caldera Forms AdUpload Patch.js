    // file uploader

    $(document).on("touchstart", ".cf-uploader-trigger",function(){
        $(".cf-uploader-trigger").trigger("focus").trigger("click");
        $(".cf-uploader-trigger").trigger("touchcancel");
    });

    // Fix caldera form issue. 
    $(document).ready(function(){

        //submit seems not work when using advanced file uploader 
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

        $("#fld_645468_1").click(function(){
            var copyValue = $("#fld_645468_1").val();
            $("#fld_645468_1").val("").val(copyValue);
        });

        // store select
        $("#fld_9970286_1").on("touchend",function(){
            $("#fld_9970286Label").click();
        });

        // join us title 
        $("#fld_1529543_1").on("touchend",function(){
            $("#fld_1529543Label").click();
        });
    });