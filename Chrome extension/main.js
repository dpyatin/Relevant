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
  			req.open("GET", "http://stormy-dusk-3543.herokuapp.com/api/getBookRecommendation/?twitterHandle=" + id, true);
  			req.onreadystatechange = function() {
    			if (req.readyState == 4) {
    				var bookHtml = "<div>";
        			var book = JSON.parse(req.responseText);
        			//document.getElementById('dataParagraph').innerHTML = "SUCCESS...OMFG\n" + book.title;
        			bookHtml += "<div style=\"float:left;\"><img src=" + book.image + " alt=\"Smiley face\" height=\"80\" width=\"42\"></div>";
        			bookHtml += "<div><p style=\"font:garamont\"><i>" + book.quote + "</i></p></div>";
        			bookHtml += "<a target=\"_blank\" href=" + book.link + ">" + book.title + "</a>";
        			bookHtml += "</div>";	
        			$("#inputContainer").empty();
        			$("#bookRecommendations").html(bookHtml);
    			}
			}
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
  	

