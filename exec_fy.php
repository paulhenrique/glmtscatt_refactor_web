<?php
$tipo           = "tipo=0";
$step           = "step=1";
$rangeInicial   = "rangeInicial=1";
$rangeFinal     = "rangeFinal=1";
$option         = "option=1";
$ordem          = "ordem=1";
$user           = "usuario=test";

$comando = 'python fw.py '.$tipo.' '.$step." ".$option." ".$ordem." ".$user;
echo $comando . "<br>";
$retorno_python= shell_exec($comando);
echo $retorno_python;
?>