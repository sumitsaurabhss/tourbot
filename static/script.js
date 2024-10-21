document.getElementById('submit').addEventListener('click', function() {
    let query = document.getElementById('query').value;
    if (query.trim() === '') return;

    document.getElementById('query').value = '';

    // Display user query
    let chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>You:</strong> ${query}</p>`;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
        // Display chatbot response
        // let htmlResponse = marked.parse(data.response)
        chatBox.innerHTML += marked.parse("**Bot**: " + data.response)  // `<p><strong>Bot:</strong> ${htmlResponse}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
});