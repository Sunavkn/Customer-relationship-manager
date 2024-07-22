var messageTimeout = document.getElementById("message-timer");
messageTimeout.style.opacity = "0";
setTimeout(function() {
    messageTimeout.style.transition = "opacity 1s";
    messageTimeout.style.opacity = "1";
    setTimeout(function() {
        messageTimeout.style.opacity = "0";
        setTimeout(function() {
            messageTimeout.style.display = "none";
        }, 1000);
    }, 3000); 
}, 100); 
