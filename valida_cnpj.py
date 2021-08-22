class ValidaCNPJ:
    def __init__(self):
        self.pesos = {
            '0': [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
            '1': [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        }
        self.digitos = ''
    
    def Get_CNPJ(self):
        # Valida a entrada do CNPJ.
        try:
            cnpj = int(input("Insira o CNPJ: "))
        except ValueError:
            print("Erro: Tipo de entrada inválida")
            exit()
        
        # Valida os digitos.
        if len(str(cnpj)) < 14:
            print('Erro: Tamanho de CNPJ inválido')
        else:
            for c in range(2):
                mult = [int(digito) * self.pesos[str(c)][i] for i, digito in enumerate(str(cnpj)[0:12 + c])]
                soma = sum(mult)
                resto = soma % 11
                self.digitos += str(11 - resto)
            
            if self.digitos not in str(cnpj):
                print("Erro: Tipo de CNPJ inválido")
            else:
                print("Success: CNPJ válido")
            
usuario = ValidaCNPJ()
usuario.Get_CNPJ()