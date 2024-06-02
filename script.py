from vpython import sphere, color, box, ring, rate, vector, cylinder

#Parâmetros do sistema
m1 = 10.5 # Massa suspensa 1 (em kg)
m2 = 20.0 # Massa suspensa 2 (em kg)
g = 9.81 # Aceleração de gravidade (em m/s^2)h
L = 3.0 # Comprimento da corda (em metros)
brown = vector(0.6,0.3,0.1)
marrom_claro = vector(0.8,0.7,0.6)
d_gray = vector(0.3,0.3,0.3)

# Criação da cenascene = canvas(title='Máquina Modificada de Atwood',width=800, height=600,center=vector(0, 2, 0),background= vector(0,0,0))scene.camera.pos = vector(0, 4, 10)

#Criação do teto
teto = box(pos=vector(0, 8, 0), axis=vector(2.5, 0, 0),
radius=0.01, color=brown)
#Criação da corda do teto
corda_teto = cylinder(pos=vector(-0.01, 8, 0), axis=vector(0, -L, 0),
radius=0.09, color=marrom_claro)

# Criação da polia redonda
polia = cylinder(pos=vector(0, 5, 0), axis=vector(0, 0, 0.1),
radius=0.6, color=d_gray)
polia_borda = ring(pos=vector(0, 5, 0), axis=vector(0, 0, 1), radius=0.5, thickness=0.21, color=brown)


# Criação das cordas
corda1 = cylinder(pos=vector(-0.5, 5, 0), axis=vector(0, -L, 0),
radius=0.05, color=marrom_claro)
corda2 = cylinder(pos=vector(0.5, 5, 0), axis=vector(0, -L, 0),
radius=0.05, color=marrom_claro)

# Criação das massas suspensas
massa1 = sphere(pos=vector(-0.5, 5 - L / 2, 0), size=vector(0.5, 0.5, 0.5), color=color.blue)
massa2 = sphere(pos=vector(0.5, 5 - L / 2, 0), size=vector(0.5, 0.5, 0.5), color=color.red)

#Criação do Chão
chão = box(pos=vector(0, 1.9, 0),size=vector(4,0.1,4), axis=vector(4, 0, 0),
radius=0, color=brown)

# Vetores de velocidade das massas
v1 = vector(0, 0, 0)
v2 = vector(0, 0, 0)

# Loop de simulação
dt = 0.001 # Intervalo de tempo
while True:
    rate(200) # Taxa de atualização da cena

# Atualização das forças nas massas
    f1 = m1 * g * vector(0, -1, 0) # Força peso na massa1
    f2 = m2 * g * vector(0, -1, 0) # Força peso na massa2

# Aceleração das massas (considerando o sistema ideal, corda inextensível)
    a = (f2 - f1) / (m1 + m2) # Aceleração comum às duas massas

# Atualização das velocidades
    v1.y += a.y * dt
    v2.y -= a.y * dt

# Atualização das posições das massas
    nova_pos1 = massa1.pos + v1 * dt
    nova_pos2 = massa2.pos + v2 * dt

# Verifica os limites de movimento
    if nova_pos1.y < 2.5 or nova_pos2.y < 2.5:
        break

# Atualiza as posições das massas
    massa1.pos = nova_pos1
    massa2.pos = nova_pos2

# Atualização das cordas
    corda1.axis = massa1.pos - corda1.pos
    corda2.axis = massa2.pos - corda2.pos

while True:
    rate(10)
