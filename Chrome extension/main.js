/**
 * @author Dmitry Pyatin
 */

document.addEventListener('DOMContentLoaded', function () {

	var submitButton = document.getElementById('submitbutton');
	//submitButton.addEventListener("click", function() { 
		/*if (document.getElementById('twitterid').value === "") {
  		
  		}
  		else {*/
  			var id = document.getElementById('twitterid').value;
  			var req = new XMLHttpRequest();
  			req.open("GET", "http://stormy-dusk-3543.herokuapp.com/api/getBookRecommendation/?twitterHandle=lucas", true);
  			req.onreadystatechange = function() {
    			if (req.readyState == 4) {
    				var bookHtml = "<div>";
        			var book = JSON.parse(req.responseText);
        			//document.getElementById('dataParagraph').innerHTML = "SUCCESS...OMFG\n" + book.title;
        			
				// actual getting image
				/*bookHtml += "<div style=\"float:left;\"><img src=" + book.image + " alt=\"Smiley face\" height=\"80\" width=\"80\"></div>";*/

        			bookHtml += "<div style=\"float:left;\"><img src=\"http://i.imgur.com/tMfdeDM.jpg\" alt=\"Smiley face\"></div>";

				// actual getting quote 
        			/* bookHtml += "<div><p><span style=\"font-size:40px;\">&#8220;</span>" 
+ book.quote + "<span style=\"font-size:40px;\">&#8221;</span></p></div>";*/

				bookHtml += "<div><p><span style=\"font-size:40px;\">&#8220;</span>" + "I like large parties, they're so intimate.<br />&nbsp;&nbsp; At small parties, there isn't privacy." + "<span style=\"font-size:40px;\">&#8221;</span>"

        			bookHtml += "</p><p><span style=\"font-size:14px;\">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; - <i><a target=\"_blank\" href=" + book.link + ">" + book.title + "</a></i></span></p>";
        			bookHtml += "</div></div>";	
        			$("#inputContainer").empty();
        			$("#bookRecommendations").html(bookHtml);
    			}
			}
    		req.send(null);
  		//}
	//});
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
  	

