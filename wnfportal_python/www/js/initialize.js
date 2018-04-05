//Seite ListeEA
$(document).on('pagecreate', '#page-listea',  function() {
	//Aktualisierung Button
	$('#btn-listea-refresh').bind('click', function(){
		listea.get();
		//focus entfernen
		$(this).blur();
	});

	//Zurück Button
	$('#btn-listeaBack').bind('click', fn.navigateToHome);
});
