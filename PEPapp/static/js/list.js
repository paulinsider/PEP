function startapp(id){
$(function() {
        $("#stopapp .btn").click(function(){
            var post_data = {
                "id" : id,
            }
            $.ajax({
                url: '../startapp',
                type: "POST",
                data: post_data,
                success: function (data) {
                    data = JSON.parse(data);
                    if (data["status"] == 1) {
                        setSceneTd(data["result"], scece_name, td);
                    } else {
                        alert(data["result"]);
                    }
                }
            });
        });
    });
}