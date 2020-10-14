from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import pygame

def chama_ar():
    root_ar = Tk()

    def play_ola_ar():
        pygame.init()
        pygame.mixer.music.load('audios/arabe/ola.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()

    bt_play_ola_ar = ttk.Button(root_ar, text='Olá', image=bt_img_play, command = play_ola_ar, compound="top")
    bt_play_ola_ar.grid(row = 0, column = 0)

    root_ar.mainloop()

root = Tk()
root.title('LanGlot')

style = ThemedStyle(root)
style.set_theme('breeze')

bt_style = ttk.Style()
bt_style.configure('estilo_bt.TButton', font=('Arial', 16, 'bold'))

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
bt_img_play = PhotoImage(file="IMGS/icones/play.png")

# BOTÕES
botao_de = ttk.Button(root, 
                      text='Deutsche', 
                      #command=chama_de, 
                      image=bt_img_de,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_en = ttk.Button(root, 
                      text='English', 
                      #command=chama_en, 
                      image=bt_img_en,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_es = ttk.Button(root, 
                      text='Español', 
                      #command=chama_es, 
                      image=bt_img_es,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_fr = ttk.Button(root, 
                      text='Français',
                      #command=chama_fr, 
                      image=bt_img_fr,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_it = ttk.Button(root, 
                      text='Italiano', 
                      #command=chama_it, 
                      image=bt_img_it,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_ru = ttk.Button(root, 
                      text='Русский', 
                      #command=chama_ru, 
                      image=bt_img_ru,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_he = ttk.Button(root, 
                      text='עברית', 
                      #command=chama_he, 
                      image=bt_img_he,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_pt_br = ttk.Button(root, 
                         text='Português Brasileiro', 
                         #command=chama_pt_br, 
                         image=bt_img_pt_br, 
                         compound="top", 
                         style='estilo_bt.TButton', 
                         width=20)

botao_ar = ttk.Button(root, 
                      text='اَلْعَرَبِيَّةُ', 
                      command=chama_ar, 
                      image=bt_img_ar,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_kr = ttk.Button(root, 
                      text='한국어', 
                      #command=chama_kr, 
                      image=bt_img_kr,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_ch = ttk.Button(root, 
                      text='中文', 
                      #command=chama_ch, 
                      image=bt_img_ch,
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)

botao_jp = ttk.Button(root, 
                      text='日本語', 
                      #command=chama_jp,
                      image=bt_img_jp, 
                      compound="top", 
                      style='estilo_bt.TButton', 
                      width=20)


botao_de.grid(row=0, column=0)
botao_en.grid(row=0, column=1)
botao_es.grid(row=0, column=2)
botao_fr.grid(row=1, column=0)
botao_it.grid(row=1, column=1)
botao_ru.grid(row=1, column=2)
botao_he.grid(row=2, column=0)
botao_pt_br.grid(row=2, column=1)
botao_ar.grid(row=2, column=2)
botao_kr.grid(row=3, column=0)
botao_ch.grid(row=3, column=1)
botao_jp.grid(row=3, column=2)

root.mainloop()
