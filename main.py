import tkinter as tk

import requests


### obtener palabras aleatorias en ingles
def get_words():

    api_key = 'YOUR API KEY'

    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        #print(response.text)
        return (response.json()['word'].lower())
    else:
        #print("Error:", response.status_code, response.text)
        return 'Error reading word'




timer_int = 59 # Initital value of counter
def my_time():

    global timer_int
    global end_game
    global btn
    global btn_restart
    
    timer_int = timer_int - 1 # decrease value by 1 
    if timer_int < 0:
        end_game = True
        btn['state'] = 'disabled'
        btn_restart['state'] = 'active'
        
        window.unbind("<Return>")

        window.unbind("<KP_Enter>")

        # answer = messagebox.askyesno(title='Jugar de nuevo?', message='Jugar de nuevo?')
        # print(answer)
        return
    
    if timer_int > 9:
        timer.config(text='00:' + str(timer_int)) # Update the label text using string
    else:
        timer.config(text='00:0' + str(timer_int)) # Update the label text using string
    timer.after(1000, my_time) # time delay of 1000 milliseconds 






playing = False
end_game = False
counter_var = 0
def enter_next(*args, **kwargs):
    global playing
    global label
    global type_entry
    global counter_var
    global counter
    global text_var

    if playing == False:
        playing = True
        my_time()
        btn['text'] = 'Enter' 
        label['text'] = get_words()

        
        # print(type_entry.get())


    if label['text']  == type_entry.get():
        label['text'] = get_words()
        counter_var += 1
        counter.config(text=str(counter_var))
        #type_entry.config(textvariable='')
        text_var.set('')
        



    #### 


window = tk.Tk()
##### titulo solamente
window.title = 'Speed Typing Test'
label_title = tk.Label(window, 
                    text="Start typing the word and press \n" + "Enter to change it", 
                    justify='center',
                    padx=20,
                    pady=20,
                    font=('Arial', 20, 'bold'),
                    #fg='white',
                    #bg='red')
                    )   
label_title.grid(row=0, column=0, columnspan=2)

#### cuadro para mostrar la palabra a digitar
label = tk.Label(window, 
                    #text='Are you ready?', 
                    justify='center',
                    padx=15,
                    pady=20,
                    font=('Arial', 30, 'bold'),
                    fg='white',
                    bg='green')
label.grid(row=1, column=0, pady=15, columnspan=2)


#### Entry para tomar la palabra digitada
text_var = tk.StringVar()
type_entry = tk.Entry(width=20,
                        borderwidth=2,
                        justify='center',
                        bg='gray',
                        textvariable=text_var,
                        
                        )

type_entry.focus()
type_entry.grid(row=2, column=0, pady=15, columnspan=2
                    # sticky="EW"
                    )



##### boton inicio

btn = tk.Button(window,
                    #text='Start',
                    command=enter_next,
                    padx=25,
                    pady=15,
                    justify='center',
                    borderwidth=2,
                    width=15,
                    # bg='green',
                    fg='green',
                    font=('Arial', '12', 'bold')
                    )
   
btn.grid(row=3, column=0, pady=10, padx=25)



##### contador de aciertos

# counter_var = tk.IntVar()
# counter_var = 0
counter = tk.Label(window,
                    font=('Arial', 30, 'bold'),
                    #bg='gray',
                    width=10,
                    padx=30,
                
                    )
# counter.config(text='0')
counter.grid(row=3, column=1, pady=10, padx=20) 



##### temporizador
timer = tk.Label(window,
                font=('Arial', 30, 'bold'),
                bg='gray',
                width=10
                )
timer.config(text='00:59')
timer.grid(row=4, column=0, pady=10, columnspan=2)

#### en esta funcion dejo lo que va a 
#### cambiar cuando se reinicie el juego

def main():
    global label
    global btn
    global playing
    global end_game
    global timer_int
    global text_var
    global counter_var
    global counter

    timer_int = 59
    counter_var = 0
    counter.config(text='0')

    btn['text'] = 'Start' 
    btn['state'] = 'active'

    label['text'] = 'Are you ready?'

            ## para que una tecla haga una funcion
    ## en este caso el enter
    window.bind("<Return>", enter_next)

    ### esta línea es para que tome el enter
    # del numeric pad. la de arriba solo
    ## toma el enter normal del teclado alfabetico
    window.bind("<KP_Enter>", enter_next)

    text_var.set('')

    playing = False
    end_game = False
    


##### boton restart

btn_restart = tk.Button(window,
                    text='Restart',
                    command=main,
                    padx=25,
                    pady=15,
                    justify='center',
                    borderwidth=2,
                    width=15,
                    bg='red',
                    fg='red',
                    state='disable'
                    )
   
btn_restart.grid(row=5, column=0, columnspan=2, pady=10, padx=25)




main()
window.mainloop()
