import turtle

# Configurações iniciais
t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(-300, 0)  # Posiciona a tartaruga à esquerda para começar

# Funções para desenhar cada letra

def draw_C():
    t.pendown()
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.penup()
    t.backward(50)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.pendown()

def draw_O():
    t.pendown()
    t.forward(20)
    t.circle(50)
    t.penup()
    t.forward(100)

def draw_D():
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-50, 180)
    t.penup()
    t.right(90)
    t.left(270)
    t.forward(100)

def draw_E():
    t.pendown()
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.penup()
    t.forward(20)

# Desenhando cada letra
draw_C()
draw_O()
draw_D()
draw_E()

# Finaliza o desenho
t.hideturtle()
turtle.done()
