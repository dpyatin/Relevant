document.addEventListener('DOMContentLoaded', function() {
	initializeRecommender();
});

function initializeRecommender() {
	getTwitterHandle();

	$('a.close').click(function(e) {
		e.preventDefault();
		e.stopImmediatePropagation();

		window.close();
	});
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
	$('body').addClass('loading');

	var request = new XMLHttpRequest();
	request.open("GET", "http://stormy-dusk-3543.herokuapp.com/api/getBookRecommendation/?twitterHandle=" + twitterHandle, true);
	request.onreadystatechange = function() {
		if (request.readyState == 4) {
			updateUI(request.responseText, twitterHandle);
		}
	}
	request.send()
}

function updateUI(recommendedBook, twitterHandle) {
	$('body').removeClass('loading');
	$('body').off('click').on('click', function() {
		// TODO: update book link url
		if (typeof recommendedBook == 'undefined') {
			window.open('http://captiv.co');
		} else {
			bookData = $.parseJSON(recommendedBook);
			window.open("http://captive-viewbook-staging.herokuapp.com/?title=" + encodeURIComponent(bookData.title)  + "&quote=" + encodeURIComponent(bookData.quote) + "&user=" + twitterHandle);
		}
	});


	var validFields = ['title', 'author', 'image', 'quote', 'link', 'error'];
	_cleanDivs(validFields);
	
	bookRecommendation = $.parseJSON(recommendedBook);
	if(!bookRecommendation.hasOwnProperty("result")) { // when there is no book to recommend {result:"none"} gets returned
		$.each(bookRecommendation, function(k, v) {
			if (validFields.indexOf(k) >= 0) {
				$('#' + k).text(v);
			}
		});
		$("#image").wrapInner('<img src=\"' + $("#image").text()  +  ' \" />');
	}
}

function _cleanDivs(divs) {
	for (var i = 0; i < divs.length; i++) {
		$('#' + divs[i]).empty();
	}
}
