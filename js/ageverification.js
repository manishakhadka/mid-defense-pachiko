// script.js
function verifyAge() {
    var data = {
        // Include relevant user data for age verification
    };

    fetch('/verify_age', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the result from the server
        if (data.result === 'allowed') {
            // Grant access to the hard drinks section
            window.location.href = 'hard_drinks.html';
        } else {
            // Deny access and show an appropriate message
            alert('Sorry, you are not allowed access.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}