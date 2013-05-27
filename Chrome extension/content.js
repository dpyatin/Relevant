chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse) {
		if (request == "getHtml") {
			sendResponse({result: document.documentElement.outerHTML});
		} else if (request == "getUsername") {
			var htmlBody = document.documentElement.outerHTML;
			
      		var username = "";
      		if ($(htmlBody).find("span.screen-name").length) {
				username = $(htmlBody).find("span.screen-name").text().substring(1,999);
	  		} 
	  		else {
				username = $(htmlBody).find(".account-group").data('screen-name');
			}
     		sendResponse({result: username});		
		}
		else {
			sendResponse({result: "Invalid Request"});
		}
	}
);

// TODO: this doesn't work yet
chrome.browserAction.setIcon({path: 'icon_glow.png'});
