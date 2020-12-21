from tkinter import *
class Place():
     def __init__(self):
          top = Tk()
          top.title("Padronizador de item 1")
          top.geometry("250x350")
          self.labelText = "Area de transferencia"
          menu = Menu(top)
          top.config(menu=menu)
          new_item = Menu(tearoff=False)
          new_item.add_command(label='Sobre',command=self.sobre)
          menu.add_cascade(label='Ajuda', menu=new_item)          
          def Iniciar():
               label5.config(text = "IP--> "+entrada1.get()+"\n"+"SERIAL--> "+entrada2.get()+"\n"+"CTO--> "+entrada3.get()+"\n"+ "SINAL--> -"+entrada4.get()+"dBm")
               top.clipboard_clear()
               top.clipboard_append("IP--> "+entrada1.get()+"\n"+"SERIAL--> "+entrada2.get()+"\n"+"CTO--> "+entrada3.get()+"\n"+ "SINAL--> -"+entrada4.get()+"dBm")
          # Label DO IP
          label1 = Label(top, text = "IP")
          label1.place(x = 10,y = 10)
          entrada1 = Entry(top, bd = 5)
          entrada1.place(x = 60,y = 10)
          # Label DO SERIAL
          label2 = Label(top,text = "SERIAL")
          label2.place(x = 10,y = 50)
          entrada2 = Entry(top,bd = 5)
          entrada2.place(x = 60,y = 50)
          # Label DA CTO
          label3 = Label(top,text = "CTO")
          label3.place(x = 10,y = 90)
          entrada3 = Entry(top,bd = 5)
          entrada3.place(x = 60,y = 90)
          # Label DO SINAL
          label4 = Label(top,text = "SINAL")
          label4.place(x = 10,y = 130)
          entrada4 = Entry(top,bd = 5)
          entrada4.place(x = 60,y = 130)
          # Area de transferencia
          label5 = Label(top, text = 'Pressione Gerar')
          label5.place(x = 60,y = 220)
          # Botão
          botao = Button(top, text = "Gerar", command=Iniciar)
          botao.place(x = 100, y = 170)
          top.mainloop()
          # Função "sobre"
     def sobre(self):
          top = Tk()
          top.geometry("240x110+70+70")
          top.title("Créditos")
            
          texto=("Criador e Desenvolvedor"+"\n"+"Guilherme Schieffelbein Patricio"+"\n"+"Criador do Padrão"+"\n"+" Allan Symmes Machado")
          textONlabel = Label(top, text=texto, font=('Helvetica', 10, 'bold'))
          textONlabel.pack()

          lb2 = Label(top, text="Versão 0.0.0.2")
          lb2.pack()                          
Place()
