chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse) {
		if (request == "getHtml")
			sendResponse({result: document.documentElement.outerHTML});
		else {
			sendResponse({result: "Invalid Request"});
		}
	}
);

// TODO: this doesn't work yet
chrome.browserAction.setIcon({path: 'icon_glow.png'});