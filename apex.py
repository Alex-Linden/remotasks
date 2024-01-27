import turtle

def apex():
    turtle.shape("square")
    turtle.color("gray")
    turtle.speed(5)
    turtle.penup()
    turtle.setpos(-250, 250)
    turtle.pendown()
    turtle.write("APEX", font=("Arial", 30, "bold"))

apex()
turtle.mainloop()