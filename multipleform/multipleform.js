$(document).ready(function(){
    $("#major").hide();
    $("#registration").hide();
    $("select#select_category").change(function(){
        var selected_category = $("option:selected").val();

        if(selected_category == "none")
        {
            // $("#form_submit").empty();
            $("#major").css({"display": "none"});
            $("#registration").css({"display": "none"});
        }

        else if(selected_category == "Classic")
        {
            $("#major").fadeIn("fast");
            $("select#select_major").change(function(){
                var selected_major = $("option:selected").val();
                if(selected_major != "none"){
                    $("#registration").fadeIn("fast");
                }
                else{
                    $("#registration").css({"display":"none"});
                }
            });
        }

    function create(selected_major) {
        $("#detailed_profile").fadeIn('fast');
        $("div#registration").append(
            $("#form_submit").append(
                $("<div/>", {id: 'head'}).append(
                    $("<h3/>").text("프로필을 입력하세요")),
                $("<input/>", {
                    type: 'text',
                    placeholder: 'Name',
                    name: 'name_'
                }), $("<br/>"), $("<input/>", {
                    type: 'text',
                    placeholder: 'Email',
                    name: 'email_'
                }), $("<br/>"), $("<textarea/>", {
                    placeholder: 'Message',
                    type: 'text',
                    name: 'msg_'
                }), $("<br/>"), $("<hr/>"), $("<br/>")))
    }

})
});
