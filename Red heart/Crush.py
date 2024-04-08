from PythonTurtle import *
speed(1)
pencolor("gray")
fillcolor("red")

def draw_heart():
  begin_fill()
  left(40)
  forward(100)
  circle(50, 210)
  right(138)
  circle(50, 210)
  forward(100)
  end_fill()
penup()
goto(-80, -80)
pendown()
draw_heart()

penup()
goto(0, 0)
down()
draw_heart()

speed(0)
def draw_str(s):
  penup()
  goto(-150, -150)
  pendown()
  write(s, font=('Ariel', 10))
draw_str('I Love You')
done()


  