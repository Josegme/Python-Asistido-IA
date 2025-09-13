$(document).ready(function () {
    $("#chat-form").on("submit", function (e) {
        e.preventDefault();
        let message = $("#user-input").val();

        if (!message) return;

        $("#chat-box").append(`<div class="user"><b>Tú:</b> ${message}</div>`);
        $("#user-input").val("");

        $.ajax({
            url: "/chat",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ message: message }),
            success: function (data) {
                if (data.reply) {
                    $("#chat-box").append(`<div class="bot"><b>Bot:</b> ${data.reply}</div>`);
                } else if (data.error) {
                    $("#chat-box").append(`<div class="bot"><b>Error:</b> ${data.error}</div>`);
                }
                $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight);
            },
            error: function (xhr) {
                $("#chat-box").append(`<div class="bot"><b>Error:</b> ${xhr.responseText}</div>`);
            }
        });
    });
});
