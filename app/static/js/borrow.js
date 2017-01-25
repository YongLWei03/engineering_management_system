$(document).ready(function(){
    $("#equipmentBorrow").steps({
        headerTag: "h3",
        bodyTag: "section",
        transitionEffect: "slideLeft",
        autoFocus: true
    });

    $("#grid-data-user").bootgrid({
        ajax: true,
        ajaxSettings: {
            method:"POST",
            cache: false
        },
        post: function() {
            return {
                "search_name":$("input[name=search_name]").val()
            }
        },
        url: "/staff/data/",
        selection: true,
        multiSelect:true,
        rowSelect:true,
        navigation: 2,
        padding:1,
    });
    var templete_user_id=[];
    $("#grid-data-user").bootgrid().on("selected.rs.jquery.bootgrid", function (e,row){
        if(templete_id.length!=0){
            $("#grid-data-user").bootgrid("deselect", templete_id);
        }
        templete_user_id[0] = row[0].id;
    });

    $("input[name=search_name]").keyup(function() {
        $("#grid-data-user").bootgrid("reload");
    });

    $("#grid-data-equipment").bootgrid({
        ajax: true,
        ajaxSettings: {
            method:"POST",
            cache: false
        },
        post: function() {
            return {
                "search_equipment":$("input[name=search_equipment]").val()
            }
        },
        url: "/equipment/data/",
        selection: true,
        multiSelect:true,
        rowSelect:true,
        navigation: 2,
        padding:1,
    });
    $("#grid-data-user").bootgrid().on("selected.rs.jquery.bootgrid", function (e,row){

    });

    $("input[name=search_equipment]").keyup(function() {
        $("#grid-data-equipment").bootgrid("reload");
    });


})
