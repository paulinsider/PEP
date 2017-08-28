$(function(){
    var $btn=$(".btn");


    var $url = "../manageApp/";
    $btn.on(
        "click",function(){
            var $formname = "#manageApp"  + $(this).attr('name');
            var buttons = this;
            $(this).button('loading');
            $.ajax({
                url:$url,
                data:$($formname).serialize(),
                type:"post",
                async: true,
                success:function(callback){
                    var callback_dict = $.parseJSON(callback);
                    if(callback_dict.status == "failed"){
                        $(buttons).button('reset')
                        alert(callback_dict.comment);
                    }else{
                        alert("成功");
                        location.reload(true);
                    }
                }
            });
        }
    );
})