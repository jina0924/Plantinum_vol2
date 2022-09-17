import board
import neopixel


pixels = neopixel.NeoPixel(board.D18,10)
pixels.fill((120,0,100))
#pixels[0] = (0,0,0)
