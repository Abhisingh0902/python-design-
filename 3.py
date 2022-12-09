from turtle import*
from colorsys import*

sides=2
color=["red","lime"]

tracer(5)
speed(1)
delay(0)
hideturtle()
bgcolor("black")
hue=2

for i in range(1000):
    color(hsv_to_rgb(hue, 1, 1))
    hue+=0.003
    fd(i*3//sides+i)
    it(360/sides+1)
    width(i*sides/250)
done()