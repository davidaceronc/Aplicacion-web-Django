$(document).ready(function () {

    $("#button_schema").click(function () {
        $.ajax({
            url: $("#url").val(),
            type: "POST",
            data: $("#form_service").serialize(),
            beforeSend: function () {
                $("#loader").show();
            },
            success: function (data) {
                $("#loader").hide();
                $("#button_schema").hide();
                $("#fields_type").show();

                $("#name_type").html($("#id_type_name").val());
                $("#fields").empty();

                data.forEach(element => {
                    if (element.fields.hidden) {
                        checkbox = "<input type='checkbox' checked>"
                    } else {
                        checkbox = "<input type='checkbox'>"
                    }

                    $("#fields").append(
                        "<tr>\
                            <td>"+ element.fields.name + "</td>\
                            <td><input type='text' class='form-control' value='"+ element.fields.label + "'></td>\
                            <td>"+checkbox+"</td>\
                        </tr>"
                    );
                });
            },

            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert(XMLHttpRequest.responseText)
                $("#loader").hide();
                $("#alert_error").show().hide(2000);
            }
        });

    });

    $("#id_type_name").keydown(function () {
        $("#fields_type").hide();
        $("#button_schema").show();
    });

    $("#id_query_sql").keydown(function () {
        $("#fields_type").hide();
        $("#button_schema").show();
    });

    $("#id_connection").change(function () {
        $("#fields_type").hide();
        $("#button_schema").show();
    });

    $("#form_service").submit(function (evt) {
        var dict = {};
        $("#fields_type input").each(function () {
            if ($(this).val() != "") {
                dict[String($(this).id())] = $(this).val();
            }
        });
        $("#id_description_fields").val(dict);
    });

});