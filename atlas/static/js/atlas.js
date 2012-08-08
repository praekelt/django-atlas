var atlas = {
    
    getLocation: function () {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(atlas.setLocation, atlas.onLocationError);
        }
        else {
            console.log("The client does not support geolocation.");
            atlas.setLocation();
        }
    },
    
    // can call this with or without a location - the server will IP geolocate the client
    setLocation: function (location) {
        settings = {
            url: "set-location",
            success: function (data, textStatus, jqXHR) {atlas.onLocationSet(data);},
            error: function (jqXHR, textStatus, error) {
                if (textStatus == 'timeout') {
                    this.retries++;
                    if (this.retries <= this.max_retries) {
                        $.ajax(this);
                        return;
                    }
                    console.log("The max retry limit has been reached and the client location could not be set.");
                    return;
                }
                else {
                    console.log("An error has occurred and the client location could not be set.");
                }
            },
            retries: 0,
            max_retries: 5,
        };
        if (location) {
            settings.data = {lon: location.coords.longitude, lat: location.coords.latitude};
            console.log("The client has been located.");
            console.log(location);
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
    
    onLocationSet: function(data) {
        document.cookie = "atlas_id=" + data + "; path=/";
    },
    
    isLocationSet: function() {
        return document.cookie.indexOf("atlas_id") > -1
    },

}