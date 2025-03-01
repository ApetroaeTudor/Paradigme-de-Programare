var http = require('http'),
    fs = require('fs');

var request = http.get("http://chrisseaton.com/truffleruby/tenthings/", function(response) {
    if (response.statusCode === 200) {
        var file = fs.createWriteStream("data.html");
        response.pipe(file);
    }
    // Add timeout.
    request.setTimeout(12000, function () {
        request.abort();
    });
});

