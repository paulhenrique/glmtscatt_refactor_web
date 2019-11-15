<?php

class glmtscatt{
	public $file = "middleware.py";
	public $type = "bessel";
	public $axicon = "";
	public $resolucao = 200;
	public $titulo = "";
	public $script = "python3 ";

	public function executar_python(){
		if($this->type == "bessel"){
			$this->script .= $this->file . " ";
		}
		
		return shell_exec($this->script);
	}
}
?>