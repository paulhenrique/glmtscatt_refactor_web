<?php
// $command = "python3 -c 'import middleware
// #middleware.gerar_visualizacao_intensidade_campo_eletrico()'";
ob_start();
$command = "python3 middleware.py > saida.test";

echo $command;
$retorno_python = passthru($command, $return);
// $retorno_python = shell_exec($command);
echo "</br>";
var_dump($return);
echo "</br>";
var_dump($retorno_python);
echo "</br>";
var_dump($mode);

?>