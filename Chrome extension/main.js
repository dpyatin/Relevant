/**
 * @author Dmitry Pyatin
 */

document.addEventListener('DOMContentLoaded', function () {
	
	chrome.runtime.onMessage.addListener(
    	function(request, sender, sendResponse) {
        	if(request.method == "getHTML2"){
            	sendResponse({data: document.body.outerHTML, method: "getHTML2"}); //same as innerText
        	}
    	}
	);
	
	var submitButton = document.getElementById('submitbutton');
	//submitButton.addEventListener("click", function() { 
		/*if (document.getElementById('twitterid').value === "") {
  		
  		}
  		else {*/
  			var id = "";//document.getElementById('twitterid').val;
  			var allHtml = "";
  			chrome.tabs.getSelected(null, function(tab) {
  				chrome.tabs.sendMessage(tab.id, {method: "getHTML2"}, function(response) {
        			if(response.method=="getHTML2"){
            			allHtml = response.data;
        			}
    			});
  			});
  		    id = $(allHtml).find("span.screen_name").text().substring(1,999)
  			var req = new XMLHttpRequest();
  			req.open("GET", "http://stormy-dusk-3543.herokuapp.com/api/getBookRecommendation/?twitterHandle=" + id, true);
  			req.onreadystatechange = function() {
    			if (req.readyState == 4) {
    				var bookHtml = "<div>";
        			var book = JSON.parse(req.responseText);
        			document.getElementById('bookRecommendations').innerHTML = "SUCCESS...OMFG\n" + id;
        			
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
  	

