/**
 * @author Dmitry Pyatin
 */

setInterval(function() {
	chrome.tabs.getSelected(null, function(tab) {
        var tabUrl = tab.url;
        
        if (tabUrl.indexOf("twitter") != -1) {
        	chrome.tabs.sendMessage(tab.id, "getUsername", function(response) {
        		// response.result contains html of the page
        		var username = response.result;
        		//alert(username);
        		// Ask the server if there are new tweets available for this user
        		// if response true -> glow
        		// if response false -> unglow
        		
        		var ajaxRequest = new XMLHttpRequest();
				ajaxRequest.open("GET", "http://stormy-dusk-3543.herokuapp.com/api/areNewTweetsAvailable/?username=" + username, true);
				ajaxRequest.onreadystatechange = function() {
					if (ajaxRequest.readyState == 4) {
						if(ajaxRequest.responseText == true) {
							chrome.browserAction.setIcon({path: 'logo_glow.png'});
						} else if (ajaxRequest.responseText == false) {
							// As an enhacement for the future, no need to keep checking for same user if server reported that new tweets are available
							chrome.browserAction.setIcon({path: 'icon.png'});
						}
					}
				}
				ajaxRequest.send()
			});
        }
	});
},3000);