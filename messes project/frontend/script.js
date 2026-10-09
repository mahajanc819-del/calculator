function sendMessage() {

    let input = document.getElementById("messageInput");
    let messages = document.getElementById("messages");

    let text = input.value.trim();

    if (text === "") {
        return;
    }

    let message = document.createElement("div");

    message.className = "message sent";

    message.innerHTML = `
        <b>You</b>
        <p>${text}</p>
    `;

    messages.appendChild(message);

    input.value = "";

    messages.scrollTop = messages.scrollHeight;
}async function sendMessage() {

    const input = document.getElementById("messageInput");
    const messages = document.getElementById("messages");

    const text = input.value.trim();

    if (text === "") {
        return;
    }

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/messages?username=Chandan&message=${encodeURIComponent(text)}`,
            {
                method: "POST"
            }
        );

        const data = await response.json();

        const message = document.createElement("div");

        message.className = "message sent";

        message.innerHTML = `
            <b>${data.username}</b>
            <p>${data.message}</p>
        `;

        messages.appendChild(message);

        input.value = "";

        messages.scrollTop = messages.scrollHeight;

    } catch (error) {
        console.log("Error:", error);
        alert("Backend connect nahi hua!");
    }
}