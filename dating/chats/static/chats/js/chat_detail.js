const csrfToken = Cookies.get('csrftoken');

    document.addEventListener('DOMContentLoaded', (event) => {

    const member1Id = JSON.parse(
        document.getElementById('member1_id').textContent
    );
    const member2Id = JSON.parse(
        document.getElementById('member2_id').textContent
    );
    const chatId = JSON.parse(
        document.getElementById('chat_id').textContent
    );

    const chatURL = `ws://${window.location.host}/ws/chats/${chatId}/`
    const chatSocket = new WebSocket(chatURL);

    // when we have a message from websocket
    chatSocket.onmessage = function(event) {

        const data = JSON.parse(event.data);
        const chat = document.getElementById('targetChat');
        const currentDate = new Date(data.sent).toLocaleString('ru');
        const isMe = data.user_id === member1Id;
        const messageClass = isMe ? 'my-message' : 'other-message';

        chat.innerHTML +=  `<div class="${messageClass}">
                                <span class="badge text-bg-secondary">
                                    ${data.user_username} ${currentDate}
                                </span>
                                <p>
                                    ${data.message}
                                </p>
                            </div>`;

        if (data['user_id'] === member1Id) {
            const saveURL = chat.dataset.saveUrl;
            let options = {
                method: 'POST',
                headers: {'X-CSRFToken': csrfToken},
                mode: 'same-origin'
            };

        // create message form
            let messageForm = new FormData();
            messageForm.append('chat_id', chatId);
            messageForm.append('content', data['message']);
            options['body'] = messageForm;

            fetch(saveURL, options)
            .then(response => response.json())
            .then(data => {
                if (data['status'] === 'saved') {
                } else {
                    console.log('error during saving');
                }
            });
        }
    };


    chatSocket.onclose = function(event) {
        console.log('chatSocket have been closed unexpectedly');
    }

    // send data in websocket
    const chatInput = document.getElementById('chatInput');
    const chatSubmit = document.getElementById('chatSubmit');

    chatSubmit.addEventListener('click', function(event) {
        const message = chatInput.value;
        if (message) {
            chatSocket.send(JSON.stringify({'message': message,
                                            'user_id': member1Id}));
            chatInput.value = '';
            chatInput.focus();
        }
    });

    // send data in websocket Enter
    chatInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            chatSubmit.click();
        }
    });

    chatInput.focus();
});