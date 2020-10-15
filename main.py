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

    letreiro_ar = Label(root_ar, image=lb_titulo_ar,
                        font=('Arial', 16, 'bold'))

    bt_1_ar = ttk.Button(root_ar,
                         text='Hello\nمرحبا',
                         image=bt_img_play,
                         command=play_1_ar,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_2_ar = ttk.Button(root_ar,
                         text='How are you?\nكيف حالكم؟ ',
                         image=bt_img_play,
                         command=play_2_ar,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_3_ar = ttk.Button(root_ar,
                         text='I\'m fine. Thank you!\n!أنا بخير ,شكرا لك',
                         image=bt_img_play,
                         command=play_3_ar,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_4_ar = ttk.Button(root_ar,
                         text='Good morning\nصباح الخير',
                         image=bt_img_play,
                         command=play_4_ar,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_5_ar = ttk.Button(root_ar,
                         text='Good afternoon\nمساء الخير',
                         image=bt_img_play,
                         command=play_5_ar,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_6_ar = ttk.Button(root_ar,
                         text='Good night\nتصبح على خير',
                         image=bt_img_play,
                         command=play_6_ar,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    # GRIDS
    letreiro_ar.grid(row=0, columnspan=4)
    bt_1_ar.grid(row=1, column=0)
    bt_2_ar.grid(row=1, column=1)
    bt_3_ar.grid(row=1, column=2)
    bt_4_ar.grid(row=2, column=0)
    bt_5_ar.grid(row=2, column=1)
    bt_6_ar.grid(row=2, column=2)

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

    letreiro_kr = Label(root_kr, image=lb_titulo_kr,
                        font=('Arial', 16, 'bold'))

    bt_1_kr = ttk.Button(root_kr,
                         text='Hello\n안녕',
                         image=bt_img_play,
                         command=play_1_kr,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_2_kr = ttk.Button(root_kr,
                         text='How are you?\n어떻게 지내?',
                         image=bt_img_play,
                         command=play_2_kr,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_3_kr = ttk.Button(root_kr,
                         text='I\'m fine!\n괜찮아요',
                         image=bt_img_play,
                         command=play_3_kr,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_4_kr = ttk.Button(root_kr,
                         text='Good morning\n좋은 아침입니다',
                         image=bt_img_play,
                         command=play_4_kr,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_5_kr = ttk.Button(root_kr,
                         text='Good afternoon\n좋은 오후입니다',
                         image=bt_img_play,
                         command=play_5_kr,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_6_kr = ttk.Button(root_kr,
                         text='Good night\n     잘 자',
                         image=bt_img_play,
                         command=play_6_kr,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    # GRIDS
    letreiro_kr.grid(row=0, columnspan=4)
    bt_1_kr.grid(row=1, column=0)
    bt_2_kr.grid(row=1, column=1)
    bt_3_kr.grid(row=1, column=2)
    bt_4_kr.grid(row=2, column=0)
    bt_5_kr.grid(row=2, column=1)
    bt_6_kr.grid(row=2, column=2)

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

    letreiro_es = Label(root_es, image=lb_titulo_es,
                        font=('Arial', 16, 'bold'))

    bt_1_es = ttk.Button(root_es,
                         text='Hello\nHola',
                         image=bt_img_play,
                         command=play_1_es,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_2_es = ttk.Button(root_es,
                         text='How are you?\nComo estás?',
                         image=bt_img_play,
                         command=play_2_es,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_3_es = ttk.Button(root_es,
                         text='I\'m fine!\nEstoy muy bién!',
                         image=bt_img_play,
                         command=play_3_es,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_4_es = ttk.Button(root_es,
                         text='Good morning\nBuenos días',
                         image=bt_img_play,
                         command=play_4_es,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_5_es = ttk.Button(root_es,
                         text='Good afternoon\nBuenas tardes',
                         image=bt_img_play,
                         command=play_5_es,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_6_es = ttk.Button(root_es,
                         text='Good night\nBuenas noches',
                         image=bt_img_play,
                         command=play_6_es,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    # GRIDS
    letreiro_es.grid(row=0, columnspan=4)
    bt_1_es.grid(row=1, column=0)
    bt_2_es.grid(row=1, column=1)
    bt_3_es.grid(row=1, column=2)
    bt_4_es.grid(row=2, column=0)
    bt_5_es.grid(row=2, column=1)
    bt_6_es.grid(row=2, column=2)

    root_es.mainloop()


def chama_ru():
    root_ru = Toplevel()

    def play_1_ru():
        pygame.init()
        pygame.mixer.music.load('audios/russo/1.mp3')
        pygame.mixer.music.play()

    def play_2_ru():
        pygame.init()
        pygame.mixer.music.load('audios/russo/2.mp3')
        pygame.mixer.music.play()

    def play_3_ru():
        pygame.init()
        pygame.mixer.music.load('audios/russo/3.mp3')
        pygame.mixer.music.play()

    def play_4_ru():
        pygame.init()
        pygame.mixer.music.load('audios/russo/4.mp3')
        pygame.mixer.music.play()

    def play_5_ru():
        pygame.init()
        pygame.mixer.music.load('audios/russo/5.mp3')
        pygame.mixer.music.play()

    def play_6_ru():
        pygame.init()
        pygame.mixer.music.load('audios/russo/6.mp3')
        pygame.mixer.music.play()

    letreiro_ru = Label(root_ru, image=lb_titulo_ru,
                        font=('Arial', 16, 'bold'))

    bt_1_ru = ttk.Button(root_ru,
                         text='Hello\nПривет',
                         image=bt_img_play,
                         command=play_1_ru,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_2_ru = ttk.Button(root_ru,
                         text='How are you?\nКак поживаете?',
                         image=bt_img_play,
                         command=play_2_ru,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_3_ru = ttk.Button(root_ru,
                         text='I\'m fine!\nСпасибо!',
                         image=bt_img_play,
                         command=play_3_ru,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_4_ru = ttk.Button(root_ru,
                         text='Good morning\nДоброе утро',
                         image=bt_img_play,
                         command=play_4_ru,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_5_ru = ttk.Button(root_ru,
                         text='Good afternoon\nДобрый день',
                         image=bt_img_play,
                         command=play_5_ru,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_6_ru = ttk.Button(root_ru,
                         text='Good night\nСпокойной ночи',
                         image=bt_img_play,
                         command=play_6_ru,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    # GRIDS
    letreiro_ru.grid(row=0, columnspan=4)
    bt_1_ru.grid(row=1, column=0)
    bt_2_ru.grid(row=1, column=1)
    bt_3_ru.grid(row=1, column=2)
    bt_4_ru.grid(row=2, column=0)
    bt_5_ru.grid(row=2, column=1)
    bt_6_ru.grid(row=2, column=2)

    root_ru.mainloop()


def chama_cn():
    root_cn = Toplevel()


    def play_1_cn():
        pygame.init()
        pygame.mixer.music.load('audios/mandarim/1.mp3')
        pygame.mixer.music.play()

    def play_2_cn():
        pygame.init()
        pygame.mixer.music.load('audios/mandarim/2.mp3')
        pygame.mixer.music.play()

    def play_3_cn():
        pygame.init()
        pygame.mixer.music.load('audios/mandarim/3.mp3')
        pygame.mixer.music.play()

    def play_4_cn():
        pygame.init()
        pygame.mixer.music.load('audios/mandarim/4.mp3')
        pygame.mixer.music.play()

    def play_5_cn():
        pygame.init()
        pygame.mixer.music.load('audios/mandarim/5.mp3')
        pygame.mixer.music.play()

    def play_6_cn():
        pygame.init()
        pygame.mixer.music.load('audios/mandarim/6.mp3')
        pygame.mixer.music.play()

    letreiro_cn = Label(root_cn, image = lb_titulo_ch, font=('Arial', 16, 'bold'))

    bt_1_cn = ttk.Button(root_cn, 
                        text = 'Hello\n你好', 
                        image=bt_img_play, 
                        command = play_1_cn, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_2_cn = ttk.Button(root_cn, 
                        text='How are you?\n你好吗?', 
                        image=bt_img_play, 
                        command = play_2_cn, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)


    bt_3_cn = ttk.Button(root_cn, 
                        text='I\'m fine!\n很好!', 
                        image=bt_img_play, 
                        command = play_3_cn, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_4_cn = ttk.Button(root_cn, 
                        text='Good morning\n早上好', 
                        image=bt_img_play, 
                        command = play_4_cn, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_5_cn = ttk.Button(root_cn, 
                        text='Good afternoon\n下午好', 
                        image=bt_img_play, 
                        command = play_5_cn, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_6_cn = ttk.Button(root_cn, 
                        text='Good night\n晚安', 
                        image=bt_img_play, 
                        command = play_6_cn, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    # GRIDS
    letreiro_cn.grid(row = 0, columnspan = 4)
    bt_1_cn.grid(row = 1, column = 0)
    bt_2_cn.grid(row = 1, column = 1)   
    bt_3_cn.grid(row = 1, column = 2)
    bt_4_cn.grid(row = 2, column = 0)
    bt_5_cn.grid(row = 2, column = 1)
    bt_6_cn.grid(row = 2, column = 2)

    root_cn.mainloop()


def chama_he():
    root_he = Toplevel()


    def play_1_he():
        pygame.init()
        pygame.mixer.music.load('audios/hebraico/1.mp3')
        pygame.mixer.music.play()

    def play_2_he():
        pygame.init()
        pygame.mixer.music.load('audios/hebraico/2.mp3')
        pygame.mixer.music.play()

    def play_3_he():
        pygame.init()
        pygame.mixer.music.load('audios/hebraico/3.mp3')
        pygame.mixer.music.play()

    def play_4_he():
        pygame.init()
        pygame.mixer.music.load('audios/hebraico/4.mp3')
        pygame.mixer.music.play()

    def play_5_he():
        pygame.init()
        pygame.mixer.music.load('audios/hebraico/5.mp3')
        pygame.mixer.music.play()

    def play_6_he():
        pygame.init()
        pygame.mixer.music.load('audios/hebraico/6.mp3')
        pygame.mixer.music.play()

    letreiro_he = Label(root_he, image = lb_titulo_he, font=('Arial', 16, 'bold'))

    bt_1_he = ttk.Button(root_he, 
                        text = 'Hello\nשלום', 
                        image=bt_img_play, 
                        command = play_1_he, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_2_he = ttk.Button(root_he, 
                        text='How are you?\n?מה שלומך', 
                        image=bt_img_play, 
                        command = play_2_he, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)


    bt_3_he = ttk.Button(root_he, 
                        text='I\'m fine!\n!אני בסדר', 
                        image=bt_img_play, 
                        command = play_3_he, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_4_he = ttk.Button(root_he, 
                        text='Good morning\nבוקר טוב', 
                        image=bt_img_play, 
                        command = play_4_he, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_5_he = ttk.Button(root_he, 
                        text='Good afternoon\nאחר הצהריים טובים', 
                        image=bt_img_play, 
                        command = play_5_he, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    bt_6_he = ttk.Button(root_he, 
                        text='Good night\nלילה טוב', 
                        image=bt_img_play, 
                        command = play_6_he, 
                        style='estilo_bt.TButton', 
                        compound="top", 
                        width=25)

    # GRIDS
    letreiro_he.grid(row = 0, columnspan = 4)
    bt_1_he.grid(row = 1, column = 0)
    bt_2_he.grid(row = 1, column = 1)   
    bt_3_he.grid(row = 1, column = 2)
    bt_4_he.grid(row = 2, column = 0)
    bt_5_he.grid(row = 2, column = 1)
    bt_6_he.grid(row = 2, column = 2)

    root_he.mainloop()


def chama_pt():
    root_pt = Toplevel()

    def play_1_pt():
        pygame.init()
        pygame.mixer.music.load('audios/portugues/1.mp3')
        pygame.mixer.music.play()

    def play_2_pt():
        pygame.init()
        pygame.mixer.music.load('audios/portugues/2.mp3')
        pygame.mixer.music.play()

    def play_3_pt():
        pygame.init()
        pygame.mixer.music.load('audios/portugues/3.mp3')
        pygame.mixer.music.play()

    def play_4_pt():
        pygame.init()
        pygame.mixer.music.load('audios/portugues/4.mp3')
        pygame.mixer.music.play()

    def play_5_pt():
        pygame.init()
        pygame.mixer.music.load('audios/portugues/5.mp3')
        pygame.mixer.music.play()

    def play_6_pt():
        pygame.init()
        pygame.mixer.music.load('audios/portugues/6.mp3')
        pygame.mixer.music.play()

    letreiro_pt = Label(root_pt, image=lb_titulo_pt,
                        font=('Arial', 16, 'bold'))

    bt_1_pt = ttk.Button(root_pt,
                         text='Hello\nOlá',
                         image=bt_img_play,
                         command=play_1_pt,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_2_pt = ttk.Button(root_pt,
                         text='How are you?\nComo está?',
                         image=bt_img_play,
                         command=play_2_pt,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_3_pt = ttk.Button(root_pt,
                         text='I\'m fine!\nEstou bem!',
                         image=bt_img_play,
                         command=play_3_pt,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_4_pt = ttk.Button(root_pt,
                         text='Good morning\nBom dia',
                         image=bt_img_play,
                         command=play_4_pt,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_5_pt = ttk.Button(root_pt,
                         text='Good afternoon\nBoa tarde',
                         image=bt_img_play,
                         command=play_5_pt,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    bt_6_pt = ttk.Button(root_pt,
                         text='Good night\nBoa noite',
                         image=bt_img_play,
                         command=play_6_pt,
                         style='estilo_bt.TButton',
                         compound="top",
                         width=25)

    # GRIDS
    letreiro_pt.grid(row=0, columnspan=4)
    bt_1_pt.grid(row=1, column=0)
    bt_2_pt.grid(row=1, column=1)
    bt_3_pt.grid(row=1, column=2)
    bt_4_pt.grid(row=2, column=0)
    bt_5_pt.grid(row=2, column=1)
    bt_6_pt.grid(row=2, column=2)

    root_pt.mainloop()


root = Tk()
root.title('LanGlot')

style = ThemedStyle(root)
style.set_theme('breeze')

bt_style = ttk.Style()
bt_style.configure('estilo_bt.TButton',
                   font=('Arial', 16, 'bold'),
                   ANCHOR=CENTER)

# IMAGENS BANDEIRAS
bt_img_de = PhotoImage(file="IMGS/bandeiras_paises/alemao.png")
bt_img_ar = PhotoImage(file="IMGS/bandeiras_paises/arabia-saudita.png")
bt_img_kr = PhotoImage(file="IMGS/bandeiras_paises/coreano.png")
bt_img_es = PhotoImage(file="IMGS/bandeiras_paises/espanhol.png")
bt_img_fr = PhotoImage(file="IMGS/bandeiras_paises/frances.png")
bt_img_en = PhotoImage(file="IMGS/bandeiras_paises/ingles.png")
bt_img_it = PhotoImage(file="IMGS/bandeiras_paises/italiano.png")
bt_img_jp = PhotoImage(file="IMGS/bandeiras_paises/japones.png")
bt_img_pt = PhotoImage(file="IMGS/bandeiras_paises/portugal.png")
bt_img_ch = PhotoImage(file="IMGS/bandeiras_paises/china.png")
bt_img_ru = PhotoImage(file="IMGS/bandeiras_paises/russia.png")
bt_img_he = PhotoImage(file="IMGS/bandeiras_paises/israel.png")
bt_img_play = PhotoImage(file="IMGS/icones/play.png")

# IMAGENS TÍTULOS
lb_titulo_de = PhotoImage(file="IMGS/titulos/alemao.png")
lb_titulo_ar = PhotoImage(file="IMGS/titulos/arabe.png")
lb_titulo_kr = PhotoImage(file="IMGS/titulos/coreano.png")
lb_titulo_es = PhotoImage(file="IMGS/titulos/espanhol.png")
lb_titulo_fr = PhotoImage(file="IMGS/titulos/frances.png")
lb_titulo_en = PhotoImage(file="IMGS/titulos/ingles.png")
lb_titulo_it = PhotoImage(file="IMGS/titulos/italiano.png")
lb_titulo_jp = PhotoImage(file="IMGS/titulos/japones.png")
lb_titulo_pt = PhotoImage(file="IMGS/titulos/portugues_portugal.png")
lb_titulo_ch = PhotoImage(file="IMGS/titulos/mandarim.png")
lb_titulo_ru = PhotoImage(file="IMGS/titulos/russo.png")
lb_titulo_he = PhotoImage(file="IMGS/titulos/hebraico.png")

# BOTÕES
botao_de = ttk.Button(root,
                      text='Deutsche',
                      # command=chama_de,
                      image=bt_img_de,
                      compound="top",
                      style='estilo_bt.TButton',
                      width=20)

botao_en = ttk.Button(root,
                      text='English',
                      # command=chama_en,
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
                      # command=chama_fr,
                      image=bt_img_fr,
                      compound="top",
                      style='estilo_bt.TButton',
                      width=20)

botao_it = ttk.Button(root,
                      text='Italiano',
                      # command=chama_it,
                      image=bt_img_it,
                      compound="top",
                      style='estilo_bt.TButton',
                      width=20)

botao_ru = ttk.Button(root,
                      text='Русский',
                      command=chama_ru,
                      image=bt_img_ru,
                      compound="top",
                      style='estilo_bt.TButton',
                      width=20)

botao_he = ttk.Button(root,
                      text='עברית',
                      command=chama_he,
                      image=bt_img_he,
                      compound="top",
                      style='estilo_bt.TButton',
                      width=20)

botao_pt = ttk.Button(root,
                         text='Português Europeu',
                         command=chama_pt,
                         image=bt_img_pt,
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
                      command=chama_cn,
                      image=bt_img_ch,
                      compound="top",
                      style='estilo_bt.TButton',
                      width=20)

botao_jp = ttk.Button(root,
                      text='日本語',
                      # command=chama_jp,
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
botao_pt.grid(row=2, column=1)
botao_ar.grid(row=2, column=2)
botao_kr.grid(row=3, column=0)
botao_ch.grid(row=3, column=1)
botao_jp.grid(row=3, column=2)

root.mainloop()
