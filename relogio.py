from time import strftime
from tkinter import Label, Tk

# ======= Configuração da janela =========
window = Tk() # ======= Cria a janela grafica =========
window.title("Relógio") # ====== Titulo da janela =========
window.geometry("300x100") #======= Proporção da tela =========
window.configure(bg="Black")  # =======Tela de fundo(bg = backgroud)=====
window.resizable(False, False)  # =====Tamanho fixo da tela =======

clock_label = Label(window, bg="black", fg="Red", font=("Red", 30, "bold"), relief="flat")

clock_label.place(x=20, y=20)


def update_label():

#==========função para atualizar o relogio a cada 80milisegundos===========
    
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ") #tupla na forma do tempo atual 
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label) #tempo da atualização
    clock_label.pack(anchor="center")


update_label() #atualiza o programa
window.mainloop() #faz o programar rodar em looping
