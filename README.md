Este projeto cria uma simulação visual de uma máquina modificada de Atwood, mostrando duas massas suspensas por cordas que passam por uma polia e se movem seguindo as leis da física.

1. Importação das Bibliotecas:

from vpython import sphere, color, box, ring, rate, vector, cylinder

-Importa as funções necessárias da biblioteca vpython para criar objetos 3D e manipular a cena.

2. Parâmetros do Sistema:

m1 = 10.5  # Massa suspensa 1 (em kg)
m2 = 20.0  # Massa suspensa 2 (em kg)
g = 9.81   # Aceleração de gravidade (em m/s^2)
L = 3.0    # Comprimento da corda (em metros)
brown = vector(0.6, 0.3, 0.1)         # Cor marrom
marrom_claro = vector(0.8, 0.7, 0.6)  # Cor marrom claro
d_gray = vector(0.3, 0.3, 0.3)        # Cor cinza escuro


-Define valores para as massas, aceleração da gravidade, comprimento da corda e algumas cores

3. Criação da Cena:

scene = canvas(title='Máquina Modificada de Atwood', width=800, height=600, center=vector(0, 2, 0), background=vector(0, 0, 0))
scene.camera.pos = vector(0, 4, 10)

-Configura a janela de visualização 3D com título, tamanho, posição central e cor de fundo. Ajusta a posição inicial da câmera.

4. Criação dos Objetos:

-Teto: 

teto = box(pos=vector(0, 8, 0), axis=vector(2.5, 0, 0), radius=0.01, color=brown)

Cria um teto representado por uma caixa marrom.

-Corda do teto: 

corda_teto = cylinder(pos=vector(-0.01, 8, 0), axis=vector(0, -L, 0), radius=0.09, color=marrom_claro)

Cria uma corda cilíndrica conectada ao teto.

-Polia Redonda: 

polia = cylinder(pos=vector(0, 5, 0), axis=vector(0, 0, 0.1), radius=0.6, color=d_gray)
polia_borda = ring(pos=vector(0, 5, 0), axis=vector(0, 0, 1), radius=0.5, thickness=0.21, color=brown)

Cria a polia e sua borda com formato cilíndrico e anelar.

-Cordas:

corda1 = cylinder(pos=vector(-0.5, 5, 0), axis=vector(0, -L, 0), radius=0.05, color=marrom_claro)
corda2 = cylinder(pos=vector(0.5, 5, 0), axis=vector(0, -L, 0), radius=0.05, color=marrom_claro)

-Cria duas cordas suspensas conectadas à polia.


-Massas Suspensas:

massa1 = sphere(pos=vector(-0.5, 5 - L / 2, 0), size=vector(0.5, 0.5, 0.5), color=color.blue)
massa2 = sphere(pos=vector(0.5, 5 - L / 2, 0), size=vector(0.5, 0.5, 0.5), color=color.red)

-Cria duas esferas representando as massas suspensas, uma azul e outra vermelha.

-Chão: 

chão = box(pos=vector(0, 1.9, 0), size=vector(4, 0.1, 4), axis=vector(4, 0, 0), radius=0, color=brown)

-Cria o chão como uma caixa marrom.

5. Vetores de Velocidade das Massas:

v1 = vector(0, 0, 0)  # Vetor de velocidade da massa 1
v2 = vector(0, 0, 0)  # Vetor de velocidade da massa 2

-Inicializa os vetores de velocidade das massas com zero.

6. Loop de Simulação:

dt = 0.001  # Intervalo de tempo
while True:
    rate(200)  # Taxa de atualização da cena (200 frames por segundo)

    # Atualização das forças nas massas
    f1 = m1 * g * vector(0, -1, 0)  # Força peso na massa 1
    f2 = m2 * g * vector(0, -1, 0)  # Força peso na massa 2

    # Aceleração das massas (considerando o sistema ideal, corda inextensível)
    a = (f2 - f1) / (m1 + m2)  # Aceleração comum às duas massas

    # Atualização das velocidades
    v1.y += a.y * dt  # Atualiza a velocidade da massa 1
    v2.y -= a.y * dt  # Atualiza a velocidade da massa 2

    # Atualização das posições das massas
    nova_pos1 = massa1.pos + v1 * dt  # Nova posição da massa 1
    nova_pos2 = massa2.pos + v2 * dt  # Nova posição da massa 2

    # Verifica os limites de movimento
    if nova_pos1.y < 2.5 or nova_pos2.y < 2.5:
        break  # Para a simulação se qualquer massa atingir o limite inferior

    # Atualiza as posições das massas
    massa1.pos = nova_pos1  # Atualiza a posição da massa 1
    massa2.pos = nova_pos2  # Atualiza a posição da massa 2

    # Atualização das cordas
    corda1.axis = massa1.pos - corda1.pos  # Atualiza a corda 1
    corda2.axis = massa2.pos - corda2.pos  # Atualiza a corda 2

-Define o intervalo de tempo dt para a simulação.
-Executa um loop onde a cena é atualizada a cada 200 frames por segundo.
-Calcula as forças peso nas massas.
-Calcula a aceleração comum às duas massas.
-Atualiza as velocidades das massas.
-Atualiza as posições das massas.
-Verifica se as massas atingem o limite inferior e para a simulação se isso acontecer.
-Atualiza as posições das cordas conforme as massas se movem.

7. Manutenção da Cena:

while True:
    rate(10)  # Mantém a cena aberta com uma taxa de atualização baixa

-Mantém a cena aberta e atualizada com uma taxa de 10 frames por segundo após o término da simulação.

