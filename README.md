# Validador_Numero_Inteiro

Este programa solicita ao usuário a digitação de um número inteiro e realiza validações até que um valor válido seja informado.
São aceitos apenas números que atendam às seguintes condições:

* Devem ser inteiros (não aceita letras ou números decimais);
* Devem ser menores ou iguais a 100;
* Não podem ser múltiplos de 10 entre 10 e 90, pois esses valores estão na lista de proibidos (10, 20, 30, 40, 50, 60, 70, 80 e 90).

Dessa forma, números como 1, 37, 55, 99 e 100 são aceitos, pois respeitam todas as regras.
Já números como 20, 50 ou 90 são rejeitados por estarem na lista de proibidos, e valores como 150 são rejeitados por ultrapassarem o limite máximo.

O programa continua solicitando a entrada até que um número válido seja digitado.
