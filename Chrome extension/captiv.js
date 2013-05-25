document.addEventListener('DOMContentLoaded', function() {
	initializeRecommender();
});

function initializeRecommender() {
	getTwitterHandle();
}

function getTwitterHandle() {
	chrome.tabs.query(
		{windowId: chrome.windows.WINDOW_ID_CURRENT, active: true}, function(tab) {
			chrome.tabs.sendMessage(tab[0].id, "getHtml", function(response) {
				var twitterHandle = "";
				if ($(response.result).find("span.screen-name").length) {
					twitterHandle = $(response.result).find("span.screen-name").text().substring(1,999);
				} else {
					twitterHandle = $(response.result).find(".account-group").data('screen-name');
				}
				getRecommendedBook(twitterHandle);
			});
		}
	);
}

function getRecommendedBook(twitterHandle) {
	var request = new XMLHttpRequest();
	request.open("GET", "http://stormy-dusk-3543.herokuapp.com/api/getBookRecommendation/?twitterHandle=" + twitterHandle, true);
	request.onreadystatechange = function() {
		if (request.readyState == 4) {
			updateUI(request.responseText);
		}
	}
	request.send()
}

function updateUI(recommendedBook) {
	var validFields = ['title', 'author', 'image', 'quote', 'link', 'error'];
	_cleanDivs(validFields);

	bookRecommendation = $.parseJSON(recommendedBook);
	$.each(bookRecommendation, function(k, v) {
		if (validFields.indexOf(k) >= 0) {
			$('#' + k).text(v);
		}
	});
	$("#image").wrapInner('<img src=\"' + $("#image").text()  +  ' \" />');
	$("#quote").wrapInner('<p class="quotestyle">');
}

function _cleanDivs(divs) {
	for (var i = 0; i < divs.length; i++) {
		$('#' + divs[i]).empty();
	}
}
