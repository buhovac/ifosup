<?php
require_once dirname(__DIR__, 2) . DIRECTORY_SEPARATOR . "config" . DIRECTORY_SEPARATOR . "constantes.php";

// La vue (HTML).
require_once dirname(__DIR__) . DS . "template" . DS . "header.php";
?>
<h1>Bienvenue dans la zone protégée par mot de passe</h1>
<?php
require_once dirname(__DIR__) . DS . "template" . DS . "footer.php";
?>