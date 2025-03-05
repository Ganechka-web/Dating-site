const csrfToken = Cookies.get('csrftoken');

document.addEventListener('DOMContentLoaded', (event) => {
    let cards = document.querySelectorAll('.card');
    let targetContainer = document.getElementById('container');

    cards.forEach(card => {
        const userURL = card.dataset.url 

        card.addEventListener('click', (event) => {
            fetch(userURL)
            .then(response => response.text())
            .then(html => { 
                const previousURL = window.location.href;

                let parser = new DOMParser();
                let detailPage = parser.parseFromString(html, 'text/html');

                // Add possibility to come back to filters
                let backButton = detailPage.getElementById('backButton');
                backButton.href = previousURL;

                targetContainer.innerHTML = '';
                targetContainer.insertAdjacentHTML('beforeEnd', html);

                let chatButton = document.getElementById('chatButton');
                chatButton.addEventListener('click', (chatEvent) => {
                    const createChatURL = chatButton.dataset.createURL;
                    let options = {
                        method: 'POST',
                        headers: {'X-CSRFToken': csrfToken},
                        mode: 'same-origin'
                    };

                    // create form
                    let createChatForm = new FormData();
                    createChatForm.append('member2_id', card.dataset.id);
                    options['body'] = createChatForm;

                    // POST request to create chat
                    fetch(createChatURL, options)
                    .then(response => response.json())
                    .then(data => {
                        if (data['status'] === 'ok') {
                            window.location.pathname = chatButton.listURL
                        } else if (data['status'] === 'blocked') {
                            alert('error');
                        }
                    });
                });

                // ai info sign event
                const aiInfoTemplate = document.getElementById('aiInfoTemplate');
                const aiButtonContainer = document.getElementById('aiButtonContainer');
                let aiInfoSign = document.getElementById('aiInfoSign')
                let shown = false;

                aiInfoSign.addEventListener('click', (aiEvent) => {
                    if (shown === false) {
                        aiButtonContainer.insertAdjacentHTML('afterend', aiInfoTemplate.innerHTML);
                        shown = true;
                    } else {
                        document.getElementById('aiInfoContent').remove();
                        shown = false;
                    }
                })
            });
        });
    });
});

