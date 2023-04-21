function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


let form = document.getElementById("myform")
form.addEventListener("submit", sendChat)


function sendChat(e) {
    e.preventDefault()
    let chatMessage = document.getElementById("id_body").value
    console.log(chatMessage)

    async function postJSON(data) {
        try {
            const response = await fetch(url, {
                method: "POST", // or 'PUT'
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            console.log("Success:", result);
            let chat_body = document.getElementById('chat-body')
            let chatMessageBox = document.createElement("div")
            chatMessageBox.classList.add("chat-box-sent")
            chatMessageBox.innerText = data
            chat_body.append(chatMessageBox)
            document.getElementById("id_body").value=""
        } catch (error) {
            console.error("Error:", error);
        }
    }

    const data = {msg: chatMessage};
    let url = `/sent_msg/${friend.username}/`;

    // let url = "{% url 'sent_messages' username=friend.username %}";

    postJSON(data);

}



