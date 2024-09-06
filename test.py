import pcg


console = pcg.WindowConsole(120, 40)

text = pcg.TextImage("##\n##")
rect = text.get_rect()
rect.y_cor = 20

while True:
    pcg.draw.blit(console, text, rect)

    rect.x_cor += 0.1
    if rect.x_cor > console.size_x:
        rect.right = 0

    console.update()
    console.fill(" ")