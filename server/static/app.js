function getURL(url, success) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            success(xmlHttp.responseText);
        }
    }
    xmlHttp.open("GET", url, true);
    xmlHttp.send();
}

redLed = Led(24)
blueLed = Led(18)


//setInterval(getTemp, 2000);

function getLight() {
    getURL('/api/light', function (result) {
        var response = JSON.parse(result);
        if(response.light < 100) {
            //Light mode
            document.getElementById("status").innerHTML="Les Toilettes sont libres";
            blueLed.on;
        } else {
            //Dark mode
            document.getElementById("status").innerHTML="Les Toilettes sont occupées";
            redLed.on;
        }
    });
}
getLight()
setInterval(getLight, 1000)
