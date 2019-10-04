<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, user-scalable=yes"/>

  <link href="/img/favicon.ico" rel="icon" type="image/x-icon"/>
  <link href="/img/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
  <!-- erstellt von https://www.ionos.de/tools/favicon-generator -->
  <link rel="apple-touch-icon" sizes="57x57" href="/img/apple-icon-57x57.png">
  <link rel="apple-touch-icon" sizes="60x60" href="/img/apple-icon-60x60.png">
  <link rel="apple-touch-icon" sizes="72x72" href="/img/apple-icon-72x72.png">
  <link rel="apple-touch-icon" sizes="76x76" href="/img/apple-icon-76x76.png">
  <link rel="apple-touch-icon" sizes="114x114" href="/img/apple-icon-114x114.png">
  <link rel="apple-touch-icon" sizes="120x120" href="/img/apple-icon-120x120.png">
  <link rel="apple-touch-icon" sizes="144x144" href="/img/apple-icon-144x144.png">
  <link rel="apple-touch-icon" sizes="152x152" href="/img/apple-icon-152x152.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/img/apple-icon-180x180.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/img/android-icon-192x192.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="96x96" href="/img/favicon-96x96.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/img/favicon-16x16.png">
  <link rel="manifest" href="/manifest.json">
  <meta name="msapplication-TileColor" content="#ffffff">
  <meta name="msapplication-TileImage" content="/img/ms-icon-144x144.png">
  <meta name="theme-color" content="#ffffff">
  <script type="text/javascript" src="js/chart.min.js"></script>
  <link rel="stylesheet" href="/css/ls_status.css"/>
</head>
<body>
<div class="bg-div">
  <a href="/index"><img class="logo-img" height="40" alt="wlsoft-logo" src="/img/wnfPortal.png"/></a>
  <div class="logo-text">{{Ueberschrift}}</div>
</div>
<hr/>
<canvas id="myChart"></canvas>
<script>
  var ctx = document.getElementById('myChart').getContext('2d');
  		var chartData = {
			labels: [{{!Labels}}],
			datasets: [{
				label: 'Kontoverlauf',
				fill: false,
				backgroundColor: '#4dc9f6',
        borderWidth:1,
        borderColor:'blue',
        pointRadius: 0,
				pointHoverRadius: 10,
				data: [{{Daten}}]
			}]
		};
  var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: chartData,
    // Configuration options go here
    options: {
    }
  });


</script>
<hr/>
</body>
