<?php
require_once dirname(__DIR__) . DIRECTORY_SEPARATOR . "config" . DIRECTORY_SEPARATOR . "constantes.php";

// La vue (HTML).
require_once __DIR__ . DS . "template" . DS . "header.php";
?>
<h1>Afficher l'IP</h1>
<p>Votre adresse IP: <?=$_SERVER['REMOTE_ADDR'];?></p>
<?php
require_once __DIR__ . DS . "template" . DS . "footer.php";
?>