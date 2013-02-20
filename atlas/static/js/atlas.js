var atlas = {
    
    getLocation: function (successCallback, errorCallback) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(successCallback ? successCallback : atlas.setLocation,
                                                     errorCallback ? errorCallback : atlas.onLocationError);
        }
        else {
            console.log("The client does not support geolocation.");
            if (errorCallback)
                errorCallback();
            else
                atlas.setLocation();
        }
    },
    
    // can call this with or without a location - the server will IP geolocate the client
    setLocation: function (location) {
        if (location) {
            document.cookie = "atlas_id=" + location.coords.longitude + "+" + location.coords.latitude + "; path=/";
            console.log("The client has been located.");
        }
        else {
            document.cookie = "atlas_id=no-location; path=/";
        }
        var retries = 0;
        var max_retries = 5;
        var errback = function (req) {
            if (req.status == 408) {
                retries++;
                if (retries <= max_retries) {
                    atlas.sendRequest('/set-location/', function(req){}, errback);
                    return;
                }
                console.log("The max retry limit has been reached.");
            }
            else {
                console.log("Some error occurred.");
            }
        };
        atlas.sendRequest('/set-location/', function(req){}, errback, 'POST');           
    },

    onLocationError: function (error) {
        // Can do more specific error handling below
        switch(error.code) {
            case error.PERMISSION_DENIED:
                console.log("Geolocation permission denied.");
                break;
            case error.POSITION_UNAVAILABLE:
                console.log("The client position is unavailable.");
                break;
            case error.TIMEOUT:
                console.log("Geolocation timed out.");
                break;
            case error.UNKNOWN_ERROR:
                console.log("The client encountered an unknown error during geolocation.");
                break;
        }
        atlas.setLocation();
    },
    
    isLocationSet: function() {
        return document.cookie.indexOf("atlas_id") > -1
    },
    
    XMLHttpFactories: [
        function () {return new XMLHttpRequest()},
        function () {return new ActiveXObject("Msxml2.XMLHTTP")},
        function () {return new ActiveXObject("Msxml3.XMLHTTP")},
        function () {return new ActiveXObject("Microsoft.XMLHTTP")}
    ],

    sendRequest: function(url, callback, errback, method, postData) {
        var req = atlas.createXMLHTTPObject();
        if (!req) return;
        if (!method) method = (postData) ? "POST" : "GET";
        req.open(method,url,true);
        if (postData)
            req.setRequestHeader('Content-type','application/x-www-form-urlencoded');
        req.onreadystatechange = function () {
            if (req.readyState != 4) return;
            if (req.status != 200 && req.status != 304) {
                errback(req);
                return;
            }
            callback(req);
        }
        if (req.readyState == 4) return;
        req.send(postData);
    },

    createXMLHTTPObject: function() {
        var xmlhttp = false;
        for (var i=0;i<atlas.XMLHttpFactories.length;i++) {
            try {
                xmlhttp = atlas.XMLHttpFactories[i]();
            }
            catch (e) {
                continue;
            }
            break;
        }
        return xmlhttp;
    },

}