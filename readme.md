# Solução do modelo Blume-Capel usando `Python`

Usando a função analítica para a magnetização:

<img src="https://render.githubusercontent.com/render/math?math=\color{white}m=\frac{2\sinh\beta(Jm%2BH)}{2\cosh\beta(Jm%2BH)%2Be^{\beta D}}">

Onde o método de zero de função é utilizado (`fsolve`).

Em adição a susceptibilidade magnética é calculada usando uma derivada simples de *m*.
