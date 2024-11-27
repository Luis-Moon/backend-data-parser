class Processador:
    def processar(self, dados: list | str, tipo_filtro: str = "split") -> list:
        """
        Processa os dados fornecidos
        Args:
        dados (list | str): Os dados a serem processados
        tipo_filtro (str): O tipo de filtro a ser aplicado. Padrão é "split". opções = {split, regex}
        Returns:
        list: Os dados processados
        """
        match tipo_filtro:
            case "split":
                filtro = self.filtro_str
            case "regex":
                filtro = self.filtro_str_re
        if isinstance(dados, list):
            return [filtro(item) for item in dados]
        else:
            return [filtro(dados)]
    
    def filtro_str(self, info_pessoal: str, separador: str = ", "):
        """
        Filtro de string baseado na função split embutida
        """
        return info_pessoal.split(separador)
    
    def filtro_str_re(self, info_pessoal: str, expressao: str = r"([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+)"):
        """
        Filtro de string baseado em expressão regular
        """
        import re
        return re.findall(expressao, info_pessoal)[0]
