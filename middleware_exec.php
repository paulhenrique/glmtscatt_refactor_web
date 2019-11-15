<?php
$command = escapeshellcmd('python3 middleware.py');
$last_line = exec($command, $output, $return);
var_dump($last_line);
?>