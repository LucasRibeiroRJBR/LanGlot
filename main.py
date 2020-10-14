from tkinter import *

root = Tk()
root.title('LanGlot')

letreiro = Label(root, text = '')
letreiro.grid(row = 0, column = 0)

#IMAGENS
bt_img_de = PhotoImage(file="IMGS/bandeiras_paises/alemao.png")
bt_img_ar = PhotoImage(file="IMGS/bandeiras_paises/arabia-saudita.png")
bt_img_kr = PhotoImage(file="IMGS/bandeiras_paises/coreano.png")
bt_img_es = PhotoImage(file="IMGS/bandeiras_paises/espanhol.png")
bt_img_fr = PhotoImage(file="IMGS/bandeiras_paises/frances.png")
bt_img_en = PhotoImage(file="IMGS/bandeiras_paises/ingles.png")
bt_img_it = PhotoImage(file="IMGS/bandeiras_paises/italiano.png")
bt_img_jp = PhotoImage(file="IMGS/bandeiras_paises/japones.png")
bt_img_pt_br = PhotoImage(file="IMGS/bandeiras_paises/portugues.png")
bt_img_ch = PhotoImage(file="IMGS/bandeiras_paises/china.png")
bt_img_ru = PhotoImage(file="IMGS/bandeiras_paises/russia.png")
bt_img_he = PhotoImage(file="IMGS/bandeiras_paises/israel.png")

root.mainloop()