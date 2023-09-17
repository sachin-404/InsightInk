

function login(){
    var username = document.getElementById("loginUsername").value
    var password = document.getElementById("loginPassword").value
    csrf= document.getElementById("csrf").value

    if(username == '' || password == ''){
        alert("username and password can not be blank")
    }

    var data = {
        'username': username,
        'password': password
    }

    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        body: JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        if (response.status == 200){
            window.location.href = '/'
        } else {
            alert(response.message)
        }
    })


}

function register(){
    var username = document.getElementById("loginUsername").value
    var password = document.getElementById("loginPassword").value
    csrf= document.getElementById("csrf").value

    if(username == '' || password == ''){
        alert("username and password can not be blank")
    }

    var data = {
        'username': username,
        'password': password
    }

    fetch('/api/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        body: JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if (response.status == 200){
            window.location.href = '/login'
            alert("Registration Succesfull. Please Login to continue")
        } else {
            alert(response.message)
        }
    })
}