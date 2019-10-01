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
  <img class="logo-img" height="40" alt="dsp-logo" src="/img/wlsoft_logo_wnfportal.png"/>
  <div class="logo-text">{{title}}</div>
</div>
<hr/>
<hr/>
<h1>{{Ueberschrift}}</h1>

<canvas id="myChart"></canvas>
<script>
  var ctx = document.getElementById('myChart').getContext('2d');
  var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: [{{!Labels}}],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [{{Data}}]
        }]
    },

    // Configuration options go here
    options: {
      scales: {yAxes: [{ticks: {beginAtZero: true}}]}
    }
  });

</script>
</body>
