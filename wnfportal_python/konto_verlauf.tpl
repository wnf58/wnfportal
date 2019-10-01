<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{{title or 'Kontoverlauf'}}</title>
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
    <script type="text/javascript" src="js/dygraph.min.js"></script>
    <link rel="stylesheet" src="css/dygraph.css"/>
    <link rel="stylesheet" href="/css/ls_status.css"/>
</head>
<body>
<div class="bg-div">
    <img class="logo-img" height="80" alt="wnfPortal-logo" src="/img/wlsoft_logo_weißer_kreis_120x120.svg"/>
    <div class="logo-text">wnfPortal</div>
</div>
<hr/>
<h1>Kontoverlauf</h1>
<div id="graphdiv1" style="width:500px; height:300px;"></div>
<script type="text/javascript">
  g1 = new Dygraph(
    document.getElementById("graphdiv1"),
    "daten/kontoverlauf.csv", // path to CSV file
    {}          // options
  );
</script>
</body>
</html>
