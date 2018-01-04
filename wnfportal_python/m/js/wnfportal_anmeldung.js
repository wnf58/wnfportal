/* Anmeldung*/
$(document).on("mobileinit", function() {
});

$(document).on("pagecreate", "#anmeldung", function() {
    $("#anmeldung .ui-btn").click(anmeldung);
    $.getJSON("q/status", "", status_verarbeiten);
});

$(document).on("pagecreate", "#main", function() {
    $("[data-dsp-page]").click(umschalten);
    $("[data-dsp-such]").click(such_panel);
    $("#main .ui-btn").click(abmeldung);
});

//$(document).on("pagecreate","#konten",function(){
 
//});
function anmeldung(event) {
    $.getJSON($(this).attr("href") + "?" + $("#anmeldung").serialize(), "", status_verarbeiten);
    event.preventDefault();
}

function abmeldung(event) {
    $.getJSON($(this).attr("href"), "", status_verarbeiten);
    event.preventDefault();
}

function status_verarbeiten(status) {
    if (status.Anmeldung) {
        $("body").pagecontainer("change", "#main", {changeHash: false});
    }
    else {
        $("body").pagecontainer("change", "#anmeldung", {changeHash: false});
    }
}

function umschalten(event) {
    $("body").pagecontainer("change", "#"+$(this).attr("data-dsp-page"), {changeHash: false});
    if ($(this).attr("data-dsp-page")==="termine") 
        $.getJSON("q/termine","",termine_anzeigen);
    if ($(this).attr("data-dsp-page")==="konten") 
        $.getJSON("q/konten","",konten_anzeigen);
    if ($(this).attr("data-dsp-page")==="konten-ea") 
        $.getJSON("q/konten_ea","",konten_ea_anzeigen);
    if ($(this).attr("data-dsp-page")==="konten-allejahre") 
        $.getJSON("q/konten_allejahre","",konten_allejahre_anzeigen);
    if ($(this).attr("data-dsp-page")==="aufgaben") 
        $.getJSON("q/aufgaben","",aufgaben_anzeigen);
    if ($(this).attr("data-dsp-page")==="adressen") 
        $.getJSON("q/adressen","",adressen_anzeigen);
    if ($(this).attr("data-dsp-page")==="adrtop10") 
        $.getJSON("q/adrtop10","",adrtop10_anzeigen);
    if ($(this).attr("data-dsp-page")==="adrdetails") {
        var s = event.target.attributes.getNamedItem("href").nodeValue;
        $.getJSON(s,"",adrdetails_anzeigen);
    }
    event.preventDefault();
}

function such_panel(event){
    $("#"+$(this).attr("data-dsp-such")).panel("open");
    event.preventDefault;
}

function konten_anzeigen(konten){
    var k=konten.konten;
    // (1) Alte Listview löschen
    $('#konten-allejahre-liste ul li').remove();
    $.each(k,function(konto){
        var sp=$("#konten-template ul").clone();
        sp.find("span.table-left").text(this.konto);
        sp.find("span.table-right-currency").text(this.saldo);
        sp.appendTo($("#kontenliste ul.kontenliste"));
    });
    //alert($("#kontenliste ul.kontenliste").html());
    $("#konten").find("[data-role=footer]").find("span.table-right-currency").html(konten.summe);
}

function konten_ea_anzeigen(ea){
    var k=ea.ea;
    // (1) Alte Listview löschen
    $('#kontenliste-ea ul li').remove();
    $.each(k,function(konto){
        var sp=$("#konten-ea-template ul").clone();
        sp.find("span.table-left").text(this.datumkurz);
        sp.find("span.table-right-currency").text(this.betrag);
        sp.appendTo($("#konten-ea-liste ul.konten-ea-liste"));
    });
    console.log($("#kontenliste ul.kontenliste").html());
    $("#konten-ea").find("[data-role=footer]").find("span.table-right-currency").html(ea.summe);
}

function konten_allejahre_anzeigen(ea){
    var k=ea.ea;
    // (1) Alte Listview löschen
    $('#kontenliste-allejahre ul li').remove();
    $.each(k,function(konto){
        var sp=$("#konten-allejahre-template ul").clone();
        sp.find("span.table-left").text(this.jahr);
        sp.find("span.table-right-currency").text(this.sDM);
        sp.appendTo($("#konten-allejahre-liste ul.konten-allejahre-ul"));
    });
    console.log($("#kontenliste-allejahre ul.kontenliste").html());
    $("#konten-allejahre").find("[data-role=footer]").find("span.table-right-currency").html(ea.summe);
}


function aufgaben_anzeigen(aufgaben){
    var k=aufgaben.aufgaben;
    // (1) Alte Listview löschen
    $('#aufgabenliste ul li').remove();
    $.each(k,function(aufgabe){
        var sp=$("#aufgaben-template ul").clone();
        sp.find("span.table-left").text(this.aufgabe);
        sp.find("span.table-right").text(this.prio);
        sp.appendTo($("#aufgaben ul.aufgabenliste"));
    });
    //alert($("#kontenliste ul.kontenliste").html());
    $("#aufgaben").find("[data-role=footer]").find("span.table-right").html(aufgaben.anzahl);
}

function termine_anzeigen(termine){
    var k=termine.termine;
    // (1) Alte Listview löschen
    $('#termineliste ul li').remove();
    $.each(k,function(termin){
        var sp=$("#termine-template ul").clone();
        sp.find("span.table-left").text(this.termin);
        sp.find("span.table-right").text(this.von);
        sp.appendTo($("#termine ul.termineliste"));
    });
    //alert($("#kontenliste ul.kontenliste").html());
    $("#termine").find("[data-role=footer]").find("span.table-right").html(termine.anzahl);
}


function adressen_anzeigen(adressen){
    //Rückkehehradresse für Adrdetails einstellen
    var sp = $("#adrdetails");
    sp.find("a").attr("data-dsp-page", "adressen");
    var k=adressen.adressen;
    // (1) Alte Listview löschen
    $('#adressenliste ul li').remove();
    $.each(k,function(adresse){
        var sp=$("#adressen-template ul").clone();
        sp.find("#ui-li-adr-kurz").text(this.kurz);
        sp.find("#ui-li-adr-tel").text('Telefon '+this.tel);
        sp.find("#ui-li-adr-handy").text('Handy '+this.handy);
        sp.find("#ui-li-adr-email").text('E-Mail '+this.email);
        sp.find("a").text('ID '+this.adr_id);
        sp.find("a").attr("href", "/q/adrdetails/"+this.adr_id);
        sp.click(umschalten);
        sp.appendTo($("#adressen ul.adressenliste"));
    });
    //alert($("#kontenliste ul.kontenliste").html());
    $("#adressen").find("[data-role=footer]").find("span.table-right").html(adressen.anzahl);
}

function adrtop10_anzeigen(adressen){
    //Rückkehehradresse für Adrdetails einstellen
    var sp = $("#adrdetails");
    sp.find("a").attr("data-dsp-page", "adrtop10");
    // (1) Alte Listview löschen
    var k=adressen.adressen;
    $('#adrtop10liste ul li').remove();
    $.each(k,function(adresse){
        sp=$("#adrtop10-template ul").clone();
        sp.find("#ui-li-adr-kurz").text(this.kurz);
        sp.find("#ui-li-adr-tel").text('Telefon '+this.tel);
        sp.find("#ui-li-adr-handy").text('Handy '+this.handy);
        sp.find("#ui-li-adr-email").text('E-Mail '+this.email);
        sp.find("a").text('ID '+this.adr_id);
        sp.find("a").attr("href", "/q/adrdetails/"+this.adr_id);
        sp.click(umschalten);
        sp.appendTo($("#adrtop10 ul.adrtop10liste"));
    });
    //alert($("#kontenliste ul.kontenliste").html());
    $("#adrtop10").find("[data-role=footer]").find("span.table-right").html(adressen.anzahl);
}

function adrdetails_anzeigen(adresse){
    //alert($("#adrdetails ul").html());
    var sp = $("#adrdetails");
    sp.find("h1").text(adresse.kurz);
    sp.find("#ui-li-adrdetails-kurz").text(adresse.kurz);
    sp.find("#ui-li-adrdetails-tel").text('Telefon ' + adresse.tel);
    sp.find("#ui-li-adrdetails-handy").text('Handy ' + adresse.handy);
    sp.find("#ui-li-adrdetails-email").text('E-Mail ' + adresse.email);
}
