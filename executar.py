from pessoa import Pessoa

p = Pessoa('Carol', 16, 'Feminino', 59)
p.addFilho('maria')
p.addFilho('joao')
p.addFilho('camila')
 
p.imprimir()
p.imprimirPessoa()


from main import Conta

c = Conta('1867','8','Carol',250.00)
c.sacar(100)
c.extrato()
c