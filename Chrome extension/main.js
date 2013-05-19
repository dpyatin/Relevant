/**
 * @author Dmitry Pyatin
 */

document.addEventListener('DOMContentLoaded', function () {

	var submitButton = document.getElementById('submitbutton');
	submitButton.addEventListener("click", function() { 
		if (document.getElementById('twitterid').value === "") {
  		
  		}
  		else {
  			var id = document.getElementById('twitterid').value;
  			var req = new XMLHttpRequest();
  			req.open("GET", "http://angelhack-travel-253.usw1.actionbox.io:5000/api/getBookRecommendation/?twitterHandle=" + id, true);
  			req.onreadystatechange = function() {
    			if (req.readyState == 4) {
    				var bookHtml = "<div>";
        			var book = JSON.parse(req.responseText);
        			document.getElementById('dataParagraph').innerHTML = "SUCCESS...OMFG\n" + book;
        			for (var key in book) {
        				bookHtml += "<p>" + book[key] + "</p>";
        			}
        			bookHtml += "</div>";	
        			var parent = document.getElementById('dataParagraph');
        			parent.insertAfter(bookHtml, parent.firstChild);
    			}
			}
    		//req.onload = handleBookMetadata.bind(this);
    		req.send(null);
  		}
	}
	);
});


handleBookMetadata =  function (e) {
    var kittens = e.target.responseXML.querySelectorAll('photo');
    for (var i = 0; i < kittens.length; i++) {
      var img = document.createElement('img');
      img.src = this.constructKittenURL_(kittens[i]);
      img.setAttribute('alt', kittens[i].getAttribute('title'));
      document.body.appendChild(img);
    }
}
  	

