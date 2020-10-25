function deletevoc(element) {
    let data = { "id": element.id }
    console.log(data)
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/delete");
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

    // send the collected data as JSON
    xhr.send(JSON.stringify(data));

    xhr.onloadend = function () {
        console.log("Send");
        window.location.reload()
    };

}
