const csrfToken = Cookies.get('csrftoken');

let optionsPost = {
    method: 'POST',
    headers: {'X-CSRFToken': csrfToken},
    mode: 'same-origin'
};

document.addEventListener('DOMContentLoaded', (event) => {
    let cards = document.querySelectorAll('.card');
    let targetContainer = document.getElementById('container');

    // Adding events to all buttons on detail page  
    cards.forEach(card => {
        const userURL = card.dataset.url 
        const previousURL = window.location.href;
        const createRecommendationUrl = card.dataset.createRecommendationUrl

        card.addEventListener('click', (event) => {
            fetch(userURL)
            .then(response => response.text())
            .then(html => { 
                let parser = new DOMParser();
                let detailPage = parser.parseFromString(html, 'text/html');

                // Add possibility to come back to filters
                let backButton = detailPage.getElementById('backButton');
                backButton.href = previousURL;

                targetContainer.innerHTML = '';
                targetContainer.insertAdjacentHTML('beforeEnd', html);
                
                // Creation chat with current member
                let chatButton = document.getElementById('chatButton');
                chatButton.addEventListener('click', (chatEvent) => {
                    const createChatURL = chatButton.dataset.createUrl;

                    let createChatForm = new FormData();
                    createChatForm.append('member2_id', card.dataset.memberId);
                    optionsPost['body'] = createChatForm;

                    fetch(createChatURL, optionsPost)
                    .then(response => response.json())
                    .then(data => {
                        if (data['status'] === 'ok') {
                            chatButton.dataset.chatUrl
                        } else if (data['status'] === 'blocked') {
                            alert('error');
                        }
                    });
                });

                // Display ai info to click on sing
                const aiInfoTemplate = document.getElementById('aiInfoTemplate');
                const aiButtonContainer = document.getElementById('aiButtonContainer');
                let aiInfoSign = document.getElementById('aiInfoSign')
                let shown = false;

                aiInfoSign.addEventListener('click', (aiInfoEvent) => {
                    if (shown === false) {
                        aiButtonContainer.insertAdjacentHTML('afterend', aiInfoTemplate.innerHTML);
                        shown = true;
                    } else {
                        document.getElementById('aiInfoContent').remove();
                        shown = false;
                    }
                })

                // Send request to create ai recommendation
                let askAiButton = document.getElementById('askAiButton');
                askAiButton.addEventListener('click', (askAiEvent) => {
                    askAiEvent.preventDefault();

                    let createRecommendationForm = new FormData();
                    createRecommendationForm.append('target_id', card.dataset.memberId);
                    optionsPost['body'] = createRecommendationForm

                    fetch(createRecommendationUrl, optionsPost)
                    .then(response => response.json())
                    .then(data => {
                        if (data['status'] === 'ok') {
                        } else {
                            // implementation recommendation count in future
                        }
                    })
                });
            });
        });
    });
});

