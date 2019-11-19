<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// $command = "python3 -c 'import middleware
// #middleware.gerar_visualizacao_intensidade_campo_eletrico()'";
$command = escapeshellcmd("python test.py");

echo $command;
#$retorno_python = exec($command, $return, $status);
$retorno_python = shell_exec($command);
// echo "</br>";
// var_dump($return);
// echo "</br>";
// var_dump($status);
echo "</br>";
var_dump($retorno_python);


?>