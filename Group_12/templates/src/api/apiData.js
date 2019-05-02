var url = 'https://newsapi.org/v2/everything?' +
          'q=Apple&' +
          'from=2019-03-29&' +
          'sortBy=popularity&' +
          'apiKey=ed7767f07ae745dd9a229ca0b63d3a92';

var req = new Request(url);

fetch(req)
    .then(function(response) {
        console.log(response.json());
    })