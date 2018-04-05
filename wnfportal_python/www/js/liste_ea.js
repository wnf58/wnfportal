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

		//überprüfen ob Bestand nicht leer ist
		if (!$.isEmptyObject(aData.LISTEA)){
			//JSON sortieren
			aData.LISTEA.sort(_sortJSON);
			listeaJSON = aData;

			html = '';

			html += '<table> id="list-listea" data-role="listview">';

			//Listeneinträge hinzufügen
			html += _getHTMLLiElementAmount(listeaJSON.LISTEA, 20);

			//Hauptliste abschließen + Suchergebnis-Liste hinzufügen
			html += '</ul><ul id="list-listeaSearch" class="hidden" data-role="listview"></ul>';

			//Filter popup erstellen
			_createFilterPopup(aData);
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
		if (!$.isEmptyObject(listeaJSON.LISTEA)){
    		//Anzahl Tiere anzeigen
		    $('#state-animalCnt').empty().append(aData.LISTEA.length + ' ' + res.value(JKEY_ANIMALS));
            //Tiere anzeigen
			while (($('#page-listea').height() <= $(window).height()) && (listeaCnt < listeaJSON.LISTEA.length)) {
				$('#list-listea').append(_getHTMLLiElementAmount(listeaJSON.LISTEA, 10));
				$('#list-listea').listview().listview('refresh');
			}
		}

	}

	/* function _getHTMLLiElementAmount (Menge von Listeneinträgen zurückliefern (aCnt = Anzahl Elemente)) */
	function _getHTMLLiElementAmount(aData, aCnt){
		var liAmount = '';
		var len = aData.length;
		var fromIndex = 0;

		//ListCount unterscheiden, je nachdem welche Liste gerade angezeigt wird
		if ($('#list-listeaSearch').is(':visible')){
			fromIndex = listeaSearchCnt;
		} else {
			fromIndex = listeaCnt;
		}

		//länge berechnen, falls angeforderte Menge größer als Liste
		if ((fromIndex + aCnt) < len) {
			len = fromIndex + aCnt;
		}

		//Teil der Liste iterieren und die jeweiligen Listeneinträge erstellen
		for (var i = fromIndex; i < len; i++) {
			liAmount += _getHTMLRow(aData[i]);
			fromIndex++;
		}

		//Count merken
		if ($('#list-listeaSearch').is(':visible')){
			listeaSearchCnt = fromIndex;
		} else {
			listeaCnt = fromIndex;
		}

		return liAmount;
	}

	/* function _getHTMLLiElement (Ein Listenelement hinzufügen (aData = ein Listeneintrag)) */
	function _getHTMLRow(aData){
		var li = '<tr>';
		li += '<td>'+'<a data-ea-id="' + aData.ID + '" href="#">'+aData.ID+'</td>';
		li += '<td>' + aData.Datum + '</td> ';
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
					$('#list-listea').append(_getHTMLLiElementAmount(listeaJSON.LISTEA, 20));
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
