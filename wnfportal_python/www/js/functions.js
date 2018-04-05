var fn = (function(){
	/* changeAndShowPage (Seite wechseln) */
	function changeAndShowPage(aPage){
		//changePage wird unter v1.5 nicht mehr existieren
		$('body').pagecontainer('change', aPage, {changeHash: false, transition: 'none'});
	}
	
	/* pageloading (Seitenladen Bild ein ausblenden) */
	var pageloading = (function(){
		//start
		function start(){
			$.mobile.loading( 'show', {
				text: 'loading...',
				textVisible: false,
				theme: 'a',
				html: ''
			});
		}
		
		//stop
		function stop(){
			$.mobile.loading('hide');
		}
		
		return {
			start: start,
			stop: stop
		};
	})();
	
	/* navigateToHome (zur Home Seite) */
	function navigateToHome(){
		var page = $('body').pagecontainer('getActivePage').attr('id');
		if (signedIn && (page != 'page-home')){
			//Seite wechseln
			changeAndShowPage('#page-home');
		}
	}
	
	/* setDefaults (alle Elemente ausblenden) */
	function setDefaults(aLogin){
		if (!aLogin){
			$('#navbar').hide();
			$('#home-content').empty();
			$('#select-clients').empty();
			$('#select-clients-button > span').empty();			
		}
		
		$('#content-inventory').empty();				
		animal.reset;
	}
	
	/* function valueExistsInArray (überprüft, ob Wert im Array vorhanden ist, wenn aEmptyArrayReturnTrue -> wird bei einem leeren übergebenen Array trotzdem true zurückgeliefert) */
	function valueExistsInArray(aValue, aArray, aEmptyArrayReturnTrue){
		//Überprüfen ob Array leer ist 
		if(aArray.length == 0){
			if (aEmptyArrayReturnTrue){
				return true;
			} else {
				return false;
			}
		} else {
			//array iterieren
			for (var i = 0; i < aArray.length; i++) {
				//überprüfen ob Wert übereinstimmt
				if (aValue == aArray[i]){
					return true;
				}
			}
			return false;
		}
	}
	
	/* function preloadImages (lädt übergebene Bilder vor) */
	function preloadImages(aImages) {
	    $(aImages).each(function(){
	        $('<img/>')[0].src = this;
	    });
	}

    /* function getJSONHerde (erweitert die getJSON-Anweisung um den Parameter sessionid=) */
	function getJSONHerde(q1,q2,b,c) {
	    $.getJSON(q1.concat(SITZUNG).concat(q2),b,c)
	}


    /* function getJSONHerdeLogin (beim Login wird keine sessionid mit gesendet) */
	function getJSONHerdeLogin(q,b,c) {
	    $.getJSON(q,b,c)
	}

	function initHerdeSitzung() {
		// Falls es schon eine Sitzung gab, diese sessionid verwenden
		var a=$.cookie("sitzung");
		if (a!=undefined) {
			SITZUNG = '?sessionid='.concat(a);
		}
	}

	return {
		changeAndShowPage : changeAndShowPage,
		pageloading : pageloading,
		navigateToHome : navigateToHome,
		setDefaults : setDefaults,
		valueExistsInArray : valueExistsInArray,
		preloadImages : preloadImages,
		getJSONHerde : getJSONHerde,
		getJSONHerdeLogin : getJSONHerdeLogin,
		initHerdeSitzung : initHerdeSitzung
	};

})();
