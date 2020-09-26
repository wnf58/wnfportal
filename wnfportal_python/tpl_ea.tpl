<html>
<head>
    <title>{{title or 'No title'}}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, user-scalable=yes"/>
    <link href="/img/favicon.ico" rel="icon" type="image/x-icon"/>
    <link href="/img/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
    <link rel="stylesheet" href="/css/wnfportal_2.css"/>
</head>
<body>
<div class="bg-div">
    <img class="logo-img" height="40" alt="wnfPortalLogo" src="/img/wnfPortal.png"/>
    <div class="logo-text">{{title}}</div>
</div>
<hr />
<table>
    %for row in wnfPortalDaten:
  <tr>{{!row}}</tr>
    %end
</table>
<hr />
</body>
