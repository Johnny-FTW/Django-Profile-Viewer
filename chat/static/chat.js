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
    let chatMessage = document.getElementById("id_body").value;
    let friendUsername = document.getElementById("friend-username").value;

    console.log(chatMessage)
    const data = {msg: chatMessage};
    let url = `/sent_msg/${friendUsername}/`;

    fetch(url, {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            let chat_body = document.getElementById('chat-body')
            let chatMessageBox = document.createElement("div")
            chatMessageBox.classList.add("chat-box-sent")
            chatMessageBox.innerHTML = data.body
            chat_body.append(chatMessageBox)
            document.getElementById("id_body").value = ""
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}


let counter = num
setInterval(receiveMessages, 2000)



function receiveMessages() {

    let friendUsername = document.getElementById("friend-username").value;
    let url = `/rec_msg/${friendUsername}/`;

    fetch(url)

        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);

            if (data.length === 0) {
            } else {
                let lastMsg = data[data.length - 1]

                if (counter === data.length) {
                    console.log("there is no now chat")
                } else {
                    let chat_body = document.getElementById('chat-body')
                    let chatMessageBox = document.createElement("div")
                    chatMessageBox.classList.add("chat-box-received")
                    chatMessageBox.innerText = lastMsg
                    chat_body.append(chatMessageBox)
                    document.getElementById("id_body").value = ""

                }


            }
            counter = data.length
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}



