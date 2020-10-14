from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import pygame

def chama_ar():
    root_ar = Toplevel()


    def play_1_ar():
        pygame.init()
        pygame.mixer.music.load('audios/arabe/1.mp3')
        pygame.mixer.music.play()


    def play_2_ar():
        pygame.init()
        pygame.mixer.music.load('audios/arabe/2.mp3')
        pygame.mixer.music.play()

    def play_3_ar():
        pygame.init()
        pygame.mixer.music.load('audios/arabe/3.mp3')
        pygame.mixer.music.play()

    def play_4_ar():
        pygame.init()
        pygame.mixer.music.load('audios/arabe/4.mp3')
        pygame.mixer.music.play()

    def play_5_ar():
        pygame.init()
        pygame.mixer.music.load('audios/arabe/5.mp3')
        pygame.mixer.music.play()

    def play_6_ar():
        pygame.init()
        pygame.mixer.music.load('audios/arabe/6.mp3')
        pygame.mixer.music.play()

    letreiro_ar = Label(root_ar, image = lb_titulo_ar, font=('Arial', 16, 'bold'))

    bt_1_ar = ttk.Button(root_ar, 
                        text = 'Hello\nمرحبا', 
                        image=bt_img_play, 
                        command = play_1_ar, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_2_ar = ttk.Button(root_ar, 
                        text='How are you?\nكيف حالكم؟ ', 
                        image=bt_img_play, 
                        command = play_2_ar, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)


    bt_3_ar = ttk.Button(root_ar, 
                        text='I\'m fine. Thank you!\n!أنا بخير ,شكرا لك', 
                        image=bt_img_play, 
                        command = play_3_ar, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_4_ar = ttk.Button(root_ar, 
                        text='Good morning\nصباح الخير', 
                        image=bt_img_play, 
                        command = play_4_ar, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_5_ar = ttk.Button(root_ar, 
                        text='Good afternoon\nمساء الخير', 
                        image=bt_img_play, 
                        command = play_5_ar, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_6_ar = ttk.Button(root_ar, 
                        text='Good night\nتصبح على خير', 
                        image=bt_img_play, 
                        command = play_6_ar, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    # GRIDS
    letreiro_ar.grid(row = 0, columnspan = 4)
    bt_1_ar.grid(row = 1, column = 0)
    bt_2_ar.grid(row = 1, column = 1)   
    bt_3_ar.grid(row = 1, column = 2)
    bt_4_ar.grid(row = 2, column = 0)
    bt_5_ar.grid(row = 2, column = 1)
    bt_6_ar.grid(row = 2, column = 2)

    root_ar.mainloop()


def chama_kr():
    root_kr = Toplevel()


    def play_1_kr():
        pygame.init()
        pygame.mixer.music.load('audios/coreano/1.mp3')
        pygame.mixer.music.play()


    def play_2_kr():
        pygame.init()
        pygame.mixer.music.load('audios/coreano/2.mp3')
        pygame.mixer.music.play()

    def play_3_kr():
        pygame.init()
        pygame.mixer.music.load('audios/coreano/3.mp3')
        pygame.mixer.music.play()

    def play_4_kr():
        pygame.init()
        pygame.mixer.music.load('audios/coreano/4.mp3')
        pygame.mixer.music.play()

    def play_5_kr():
        pygame.init()
        pygame.mixer.music.load('audios/coreano/5.mp3')
        pygame.mixer.music.play()

    def play_6_kr():
        pygame.init()
        pygame.mixer.music.load('audios/coreano/6.mp3')
        pygame.mixer.music.play()

    letreiro_kr = Label(root_kr, image = lb_titulo_kr, font=('Arial', 16, 'bold'))

    bt_1_kr = ttk.Button(root_kr, 
                        text = 'Hello\n안녕', 
                        image=bt_img_play, 
                        command = play_1_kr, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_2_kr = ttk.Button(root_kr, 
                        text='How are you?\n어떻게 지내?', 
                        image=bt_img_play, 
                        command = play_2_kr, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)


    bt_3_kr = ttk.Button(root_kr, 
                        text='I\'m fine!\n괜찮아요', 
                        image=bt_img_play, 
                        command = play_3_kr, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_4_kr = ttk.Button(root_kr, 
                        text='Good morning\n좋은 아침입니다', 
                        image=bt_img_play, 
                        command = play_4_kr, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_5_kr = ttk.Button(root_kr, 
                        text='Good afternoon\n좋은 오후입니다', 
                        image=bt_img_play, 
                        command = play_5_kr, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_6_kr = ttk.Button(root_kr, 
                        text='Good night\n     잘 자', 
                        image=bt_img_play, 
                        command = play_6_kr, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    # GRIDS
    letreiro_kr.grid(row = 0, columnspan = 4)
    bt_1_kr.grid(row = 1, column = 0)
    bt_2_kr.grid(row = 1, column = 1)   
    bt_3_kr.grid(row = 1, column = 2)
    bt_4_kr.grid(row = 2, column = 0)
    bt_5_kr.grid(row = 2, column = 1)
    bt_6_kr.grid(row = 2, column = 2)

    root_kr.mainloop()


def chama_es():
    root_es = Toplevel()


    def play_1_es():
        pygame.init()
        pygame.mixer.music.load('audios/espanhol/1.mp3')
        pygame.mixer.music.play()


    def play_2_es():
        pygame.init()
        pygame.mixer.music.load('audios/espanhol/2.mp3')
        pygame.mixer.music.play()

    def play_3_es():
        pygame.init()
        pygame.mixer.music.load('audios/espanhol/3.mp3')
        pygame.mixer.music.play()

    def play_4_es():
        pygame.init()
        pygame.mixer.music.load('audios/espanhol/4.mp3')
        pygame.mixer.music.play()

    def play_5_es():
        pygame.init()
        pygame.mixer.music.load('audios/espanhol/5.mp3')
        pygame.mixer.music.play()

    def play_6_es():
        pygame.init()
        pygame.mixer.music.load('audios/espanhol/6.mp3')
        pygame.mixer.music.play()

    letreiro_es = Label(root_es, image = lb_titulo_es, font=('Arial', 16, 'bold'))

    bt_1_es = ttk.Button(root_es, 
                        text = 'Hello\nHola', 
                        image=bt_img_play, 
                        command = play_1_es, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_2_es = ttk.Button(root_es, 
                        text='How are you?\nComo estás?', 
                        image=bt_img_play, 
                        command = play_2_es, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)


    bt_3_es = ttk.Button(root_es, 
                        text='I\'m fine!\nEstoy muy bién!', 
                        image=bt_img_play, 
                        command = play_3_es, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_4_es = ttk.Button(root_es, 
                        text='Good morning\nBuenos días', 
                        image=bt_img_play, 
                        command = play_4_es, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_5_es = ttk.Button(root_es, 
                        text='Good afternoon\nBuenas tardes', 
                        image=bt_img_play, 
                        command = play_5_es, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_6_es = ttk.Button(root_es, 
                        text='Good night\nBuenas noches', 
                        image=bt_img_play, 
                        command = play_6_es, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    # GRIDS
    letreiro_es.grid(row = 0, columnspan = 4)
    bt_1_es.grid(row = 1, column = 0)
    bt_2_es.grid(row = 1, column = 1)   
    bt_3_es.grid(row = 1, column = 2)
    bt_4_es.grid(row = 2, column = 0)
    bt_5_es.grid(row = 2, column = 1)
    bt_6_es.grid(row = 2, column = 2)

    root_es.mainloop()


root = Tk()
root.title('LanGlot')

style = ThemedStyle(root)
style.set_theme('breeze')

bt_style = ttk.Style()
bt_style.configure('estilo_bt.TButton', 
                    font=('Arial', 16, 'bold'), 
                    ANCHOR=CENTER)

letreiro = Label(root, text = '')
letreiro.grid(row = 0, column = 0)

#IMAGENS BANDEIRAS
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

#IMAGENS TÍTULOS
lb_titulo_de = PhotoImage(file="IMGS/titulos/alemao.png")
lb_titulo_ar = PhotoImage(file="IMGS/titulos/arabe.png")
lb_titulo_kr = PhotoImage(file="IMGS/titulos/coreano.png")
lb_titulo_es = PhotoImage(file="IMGS/titulos/espanhol.png")
lb_titulo_fr = PhotoImage(file="IMGS/titulos/frances.png")
lb_titulo_en = PhotoImage(file="IMGS/titulos/ingles.png")
lb_titulo_it = PhotoImage(file="IMGS/titulos/italiano.png")
lb_titulo_jp = PhotoImage(file="IMGS/titulos/japones.png")
lb_titulo_pt_br = PhotoImage(file="IMGS/titulos/portugues_portugal.png")
lb_titulo_ch = PhotoImage(file="IMGS/titulos/mandarim.png")
lb_titulo_ru = PhotoImage(file="IMGS/titulos/russo.png")
lb_titulo_he = PhotoImage(file="IMGS/titulos/hebraico.png")

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
                      command=chama_es, 
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
                      command=chama_kr, 
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
