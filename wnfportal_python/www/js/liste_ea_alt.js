/* Liste EA */
var listea = (function(){
	var listeaJSON = {};
	var performed = false;

	/* function get (Informationen abfragen und Callback-Funktion aufrufen) */
	function get(){
		$("#listeaHeader").empty().append('xxxx');
		$("#btn-listea-refresh").show();
		fn.getJSONHerde(QUERY_LISTEA,'', '', _process);
	}

	/* function setListEA (wird nach Einzeltiersuche aufgerufen, wenn mehrere Tiere gefunden wurden) */
	function setListEA(aData){
		//Header setzen
		$("#listeaHeader").empty().append(res.value(JKEY_FOUNDANIMALS));
		$("#btn-listea-refresh").hide();
		_process(aData);
	}

	/* function process (Antwort auswerten) */
	function _process(aData){
		listeaCnt = 0;
		var html = '';
    //console.log(aData);
		//überprüfen ob Bestand nicht leer ist
		if (!$.isEmptyObject(aData)){
			//JSON sortieren
			//aData.LISTEA.sort(_sortJSON);
			listeaJSON = aData;

			html = '';

			html += '<table id="list-listea" data-role="listview">';

			//Listeneinträge hinzufügen
			html += _getHTMLLiElementAmount(listeaJSON, 20);

		} else {
			html = '<h3 class="centerText">Keine Daten vorhanden</h3>';
		}

		//Content einfügen
		$('#content-listea').empty().append(html);

		//Style aktualisieren !wichtig! sonst werden css Einstellungen nicht erneut geladen
		$('#content-listea').trigger('create');

		//Events setzen
		_setListEAEvents();

		//zum Seitenanfang disablen
		$('#btn-listea-scrollup').addClass('ui-state-disabled');


		//Elemente hinzufügen, solange bis Seite scrollbar ist
		if (!$.isEmptyObject(listeaJSON)){
    		//Anzahl Tiere anzeigen
		    $('#state-animalCnt').empty().append(aData.length + ' Buchungssätze');
            //Tiere anzeigen
			while (($('#page-listea').height() <= $(window).height()) && (listeaCnt < listeaJSON.length)) {
				$('#list-listea').append(_getHTMLLiElementAmount(listeaJSON, 10));
				$('#list-listea').listview().listview('refresh');
			}
		}

	}

	/* function _getHTMLLiElementAmount (Menge von Listeneinträgen zurückliefern (aCnt = Anzahl Elemente)) */
	function _getHTMLLiElementAmount(aData, aCnt){
	  var fromIndex = 0;
		var liAmount = '';
		var len = aData.length;

		fromIndex = listeaCnt;

		//länge berechnen, falls angeforderte Menge größer als Liste
		if ((fromIndex + aCnt) < len) {
			len = fromIndex + aCnt;
		}

		//Teil der Liste iterieren und die jeweiligen Listeneinträge erstellen
		for (var i = fromIndex; i < len; i++) {
			liAmount += _getHTMLRow(i+1,aData[i]);
			fromIndex++;
		}

		//Count merken
		listeaCnt = fromIndex;

		return liAmount;
	}

	/* function _getHTMLLiElement (Ein Listenelement hinzufügen (aData = ein Listeneintrag)) */
	function _getHTMLRow(aLfdNr,aData){
		var li = '<tr>';
		li += '<td>' + aLfdNr + '</td> ';
		li += '<td>'+'<a data-ea-id="' + aData.id + '" href="#">'+aData.id+'</td>';
		li += '<td>' + aData.datum + '</td> ';
		li += '<td>' + aData.kurz + '</td> ';
		li += '<td>' + aData.betrag + '</td> ';
		return li += '</tr>';
	}


	/* function _setListEAEvents (Events setzen) */
	function _setListEAEvents(){
		//dynamisches Laden hinzufügen
		$(document).on('scroll', function(){
				var wintop = $(window).scrollTop(), docheight = $(document).height(), winheight = $(window).height();
				var  scrolltrigger = 0.95;

				//zum Seitenanfang disablen/enablen
				if ($(window).scrollTop() == 0){
					$('#btn-listea-scrollup').addClass('ui-state-disabled');
				} else {
					if (!$('#btn-listea-scrollup').is('ui-state-disabled')){
						$('#btn-listea-scrollup').removeClass('ui-state-disabled');
					}
				}

				if  ((wintop/(docheight-winheight)) > scrolltrigger) {
					$('#list-listea').append(_getHTMLLiElementAmount(listeaJSON, 20));
					$('#list-listea').listview().listview('refresh');
					}
		});
	}

	return {
		get: get,
		setListEA: setListEA,
		performed: performed
	};
})();
