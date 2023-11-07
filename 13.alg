Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor    : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/11/2023
Var
   // Seção de Declarações das variáveis
   chico,ze, dias, anos: real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

   //tamanhos em cm
   chico <- 150 // cresce 2cm por ano
   ze <- 140 // cesce 3cm por ano.
   anos <- 0
   enquanto ze <= chico faca
         anos <- anos + 1
         chico <- chico + 2
         ze <- ze + 3
   fimenquanto
   chico <- chico / 100
   ze <- ze / 100
   escreva("em ", anos," anos. zé terá",ze," metros e será maior que chico com", chico,"metros")


Fimalgoritmo