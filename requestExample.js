var rp = require('request-promise');
var cheerio = require('cheerio');

var url = 'https://www.pizzapizza.ca/'

//'https://padmapper.com/';

rp(url)
.then((html) => {

    let $ = cheerio.load(html);
    console.log(html);
    $('span.comhead').each(function(i,element){
        var a = $(this).prev();
        var b = myFunction(a,"Price")
        console.log(a.text());

    });
})

.catch(console.error.bind(console));


function myFunction(myString, myWord)
{

    var myResult = myString.split(" ");

    for(var i=0; i<myResult.length; i++) {
        var result = myResult[i].match(myPattern);
        if(result) break;
    }

    return myResult;

}
