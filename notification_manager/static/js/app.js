$(function () {
    $("#send").click(function () {

            socket = new WebSocket("ws://" + window.location.host + "/chat/");
            socket.onmessage = function (e) {
                // alert(e.data);
                $('#message_log').val(
                    $('#message_log').val() + e.data + '\n'
                );
            };
            socket.onopen = function () {
                socket.send($('#text_to_send').val());
            };
            // Call onopen directly if socket is already open
            if (socket.readyState == WebSocket.OPEN) socket.onopen();

        }
    );

    $("#clear_log").click(function () {
            $('#message_log').val('');

        }
    );

});
