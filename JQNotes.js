修改min的值 $("#num").attr("min","值")
修改max的值 $("#num").attr("max","值")
获取min的值 $("#num").attr("min")
获取max的值 $("#num").attr("max")

// set charactor limit
<script type="text/javascript">
$(document).ready(function() { 
   $(".audience-other-limit input").attr("maxlength","20");
   $(".custom-order textarea").attr("maxlength","200");
   $(".order-notes textarea").attr("maxlength","1000");
});
</script>