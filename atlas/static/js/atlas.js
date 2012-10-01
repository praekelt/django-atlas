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
        settings = {
            url: "/set-location/",
            error: function (jqXHR, textStatus, error) {
                if (textStatus == 'timeout') {
                    this.retries++;
                    if (this.retries <= this.max_retries) {
                        $.ajax(this);
                        return;
                    }
                    console.log("The max retry limit has been reached.");
                    return;
                }
                else {
                    console.log("Some error occurred.");
                }
            },
            retries: 0,
            max_retries: 5,
        };
        if (location) {
            document.cookie = "atlas_id=" + location.coords.longitude + "+" + location.coords.latitude + "; path=/";
            console.log("The client has been located.");
        }
        else {
            document.cookie = "atlas_id=no-location; path=/";
        }
        $.ajax(settings);
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

}