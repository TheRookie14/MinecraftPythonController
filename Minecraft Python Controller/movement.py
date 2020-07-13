import minecraft

while True:
    minecraft.waitFor("#")

    minecraft.walk(5)
    minecraft.jump("up")
    minecraft.turn(90)
    minecraft.sendMessage("done")
