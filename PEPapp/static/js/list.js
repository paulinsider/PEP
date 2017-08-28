$(function(){
    var $btn=$(".btn");


    var $url = "../manageApp/";
    $btn.on(
        "click",function(){
            var $formname = "#manageApp"  + $(this).attr('name');
            $(this).button('loading');
            $.ajax({
                url:$url,
                data:$($formname).serialize(),
                type:"post",
                async: true,
                success:function(callback){
                    var callback_dict = $.parseJSON(callback);
                    if(callback_dict.status == "failed"){
                        alert(callback_dict.comment);
                        $(this).button('reset');
                    }else{
                        alert("成功");
                        location.reload(true);
                    }
                }
            });
        }
    );
})