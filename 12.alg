Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor    : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/11/2023
Var
   // Seção de Declarações das variáveis
   num, aux ,contador, i: inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   escreval("Digite um numero")
   leia(num)
   //
   para i de 1 ate num faca
      aux <- num mod i
      se aux = 0 entao
         contador <- contador + 1
      fimse
   fimpara
   se contador = 2 entao
      escreva("é um numero primo")
   senao
      escreva("não é um numero primo")
   fimse

Fimalgoritmo