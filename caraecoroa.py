
import random
import Tkinter

jogo = Tkinter.Label()
jogo.pack()
jogo["font"] = "Helvetica 120 bold"

moeda = random.randint(0,1)

print("RESULTADO:")
if moeda == 1:
  jogo["text"]= "cara" 
else:
  jogo["text"]= "coroa" 

jogo.mainloop()
