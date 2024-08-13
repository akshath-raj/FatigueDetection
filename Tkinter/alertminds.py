
from pathlib import Path
from tkinter import *
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time



#path for controle
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
#greets
def greet():
    greetings = ['Hola !', 'Hello :)', 'Sup '+("\U0001f60e"), 'Howdy '+ ("\U0001F607"), 'Greetings !',  'Ola !' , 'Allo !']
    return random.choice(greetings)
#Home page
def Home(parent):
    canvas = Canvas(
    parent,
    bg = "#FFFFFF",
    height = 405,
    width = 675,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")


    
    canvas.place(x = 230, y = 72)

#Time table page
def timetable(parent_window):
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480-100+32,
    width = 700-20,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

    canvas.place(x = 230, y = 72)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        350.0,
        240.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        620.0,
        68.0,
        700.0,
        69.0,
        fill="#B83737",
        outline="")

    canvas.create_rectangle(
        22.0,
        114.0,
        222.0,
        136.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        22.0,
        314.0,
        222.0,
        336.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        611.0,
        -1.0,
        612.0,
        59.0,
        fill="#B83737",
        outline="")

    canvas.create_rectangle(
        611.0,
        229.0,
        612.0,
        480.0,
        fill="#B83737",
        outline="")

    canvas.create_rectangle(
        -1.0,
        68.0,
        604.0,
        69.0,
        fill="#B83737",
        outline="")

    canvas.create_rectangle(
        22.0,
        214.0,
        222.0,
        236.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        585.0,
        225.0,
        anchor="nw",
        text="12/12/12",
        fill="#38b6ff",
        font=("Inter Bold", 44 * -1),
        angle=90
    )

    canvas.create_text(
        22.0,
        114.0,
        anchor="nw",
        text="time 1",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        22.0,
        214.0,
        anchor="nw",
        text="time 1",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        22.0,
        314.0,
        anchor="nw",
        text="time 1",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        38.0,
        166.0,
        anchor="nw",
        text="sample txt",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        38.0,
        266.0,
        anchor="nw",
        text="sample txt",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        38.0,
        366.0,
        anchor="nw",
        text="sample txt",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )
    
#reports page
def reports(parent):
    canvas = Canvas(
    parent,
    bg = "#FFFFFF",
    height = 405,
    width = 675,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")


    
    canvas.place(x = 230, y = 72)

    # Function to generate live concentration levels
    def generate_concentration():
        # Generate a random concentration level between 60 and 100
        return random.randint(60, 100)

    # Function to update the graph
    def update_graph():
        # Generate live concentration data
        concentration = generate_concentration()
        
        # Get current time
        current_time = time.strftime("%H:%M:%S")
        
        # Append data to lists
        x_data.append(current_time)
        y_data.append(concentration)
        
        # Limit data to show last 10 data points
        if len(x_data) > 10:
            x_data.pop(0)
            y_data.pop(0)
        
        # Clear previous plot
        ax.clear()
        
        # Plot data
        ax.plot(x_data, y_data, marker='o', linestyle='-')
        
        # Set labels and title
        ax.set_xlabel('Time')
        ax.set_ylabel('Concentration Level')
        ax.set_title('Live Concentration vs Time')
        
        # Update the graph
        canvas.draw()
        
        # Call update_graph function after 1 second (1000 milliseconds)
        parent.after(1000, update_graph)



    # Create matplotlib figure and canvas
    fig = Figure(figsize=(6.70, 4))
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=220,y=70)

    # Initialize lists to store data
    x_data = []
    y_data = []

    # Call the update_graph function to start updating the graph
    update_graph()


#quiz page
def quiz(parent):

    
    
    canvas = Canvas(
    parent,
    bg = "#FFFFFF",
    height = 480-68,
    width = 700-16,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

    canvas.place(x = 230, y = 72)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        350.0,
        240.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        620.0,
        69.0,
        700.0,
        70.0,
        fill="#B83737",
        outline="")



    canvas.create_rectangle(
        610.9999999507862,
        8.0,
        613.0,
        498.0000174619963,
        fill="#B83737",
        outline="")

    canvas.create_text(
        22.0,
        134.0,
        anchor="nw",
        text="Question 1",
        fill="#0000FF",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        80.0,
        91.0,
        anchor="nw",
        text="QUIZ ON BASIC AI AND ML",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_rectangle(
        -1.0,
        68.0,
        621.0,
        69.00000000000006,
        fill="#8C1818",
        outline="")

    canvas.create_text(
        30.0,
        212.0-30,
        anchor="nw",
        text="What is the fullform of RNN?",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        22.0,
        264.0-30,
        anchor="nw",
        text="Question 2",
        fill="#0000FF",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        30.0,
        312.0-30,
        anchor="nw",
        text="What is the fullform of CNN?",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        22.0,
        364.0-30,
        anchor="nw",
        text="Question 3",
        fill="#0000FF",
        font=("CreteRound Regular", 17 * -1)
    )

    canvas.create_text(
        30.0,
        412.0-30,
        anchor="nw",
        text="What is the fullform of FFNN?",
        fill="#000000",
        font=("CreteRound Regular", 17 * -1)
    )

#button check
def handle_button_press(btn_name):
    global current_window
    if btn_name == "home":
        current_window = Home(window)
        home_button_clicked()
        
    elif btn_name == "timetable":
        timetable_button_clicked()
        current_window = quiz(window)
    elif btn_name=="reports":
        reports_button_clicked()
        current_window = reports(window)
    elif btn_name == "quiz":
        print("jjiu........................................................")
        quiz_button_clicked()
        current_window=timetable(window)
    elif btn_name == "pauseresume":
        pass
# ~ FUNCTIONS FOR BUTTONS FOR CHANGING TABS ~
def home_button_clicked(): # (coordinates : x= 0 , y= 133)
    print("Home button clicked")
    canvas.itemconfig(page_navigator, text="Home")
    sidebar_navigator.place(x=0, y=133)    
def quiz_button_clicked(): # (coordinates : x= 0 , y= 184)
    print("quiz button clicked")
    canvas.itemconfig(page_navigator, text="Time Table")
    sidebar_navigator.place(x=0, y=184)
def reports_button_clicked():
    print("reports button clicked")
    canvas.itemconfig(page_navigator, text="Report")
    sidebar_navigator.place(x=0, y=232)
def timetable_button_clicked(): # (coordinates : x= 0 , y= 232)
    print("timetable button clicked")
    canvas.itemconfig(page_navigator, text="Quiz")
    sidebar_navigator.place(x=0, y=280)

#__main__
window = Tk()
window.title("Alert Minds")
window.geometry("930x506")
window.configure(bg = "#dbdbdb")
canvas = Canvas(
    window,
    bg = '#dbdbdb',
    height = 506,
    width = 930,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
background_image = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    566.0,
    253.0,
    image=background_image
)


current_window=Home(window)


####### HOME BUTTON #############
home_button_image = PhotoImage(
    file=relative_to_assets("HOME (6) (1).png"))
home_button = Button(
    image=home_button_image,
    bg="#dbdbdb",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("home"),
    relief="sunken",
    activebackground="#dbdbdb",
    activeforeground="#dbdbdb"
)
home_button.place(
    x=7.35,
    y=133.0,
    width=191.0,
    height=47.0
)
#################################
####### tt BUTTON #############
quiz_button_image = PhotoImage(
    file=relative_to_assets("HOME (5) (1).png"))
quiz_button = Button(
    image=quiz_button_image,
    borderwidth=0,
    bg="#dbdbdb",
    highlightthickness=0,
    command=lambda: handle_button_press("quiz"),
    relief="sunken",
    activebackground="#dbdbdb",
    activeforeground="#dbdbdb"
)
quiz_button.place(
    x=7.35,
    y=184.0,
    width=191,
    height=47.0
)
#####################################
####### reports BUTTON #############
reports_button_image = PhotoImage(
    file=relative_to_assets("rep (2).png"))
reports_button = Button(
    image=reports_button_image,
    borderwidth=0,
    bg="#dbdbdb",
    highlightthickness=0,
    command=lambda: handle_button_press("reports"),
    relief="sunken",
    activebackground="#dbdbdb",
    activeforeground="#dbdbdb"
)
reports_button.place(
    x=7.35,
    y=232.0,
    width=191.146240234375,
    height=47.0
)
####### timetable BUTTON ################
timetable_button_image = PhotoImage(
    file=relative_to_assets("quiz (1).png"))
timetable_button = Button(
    image=timetable_button_image,
    borderwidth=0,
    bg="#dbdbdb",
    highlightthickness=0,
    command=lambda: handle_button_press("timetable"),
    relief="sunken",
    activebackground="#dbdbdb",
    activeforeground="#dbdbdb"
)
timetable_button.place(
    x=7.351776123046875,
    y=280.0,
    width=191.146240234375,
    height=47.0
)
########################################
####### (i)  SIDEBAR NAVIGATOR #########
sidebar_navigator = Frame(background="#b83737")
sidebar_navigator.place(x=0, y=133, height=47, width=7)
########################################
####### (ii)  PAGE NAVIGATOR ###########
page_navigator = canvas.create_text(
    251.0,
    37.0,
    anchor="nw",
    text="Home",
    fill="#dbdbdb",
    font=("Montserrat Bold", 26 * -1))
########################################
########################################
#App name
img= PhotoImage(
    file=relative_to_assets("HOME (1) (3).png"))
canvas.create_image(20,0,anchor=NW,image=img)
"""canvas.create_text(             
    21.0,
    21.0,
    anchor="nw",
    text="Alerts Mind",
    fill="#000000",
    font=("MS Sans Serif", 32 * -1)
)"""
############## Greetings/Hello ################################ 
canvas.create_text(
    800.0,
    46.0,
    anchor="nw",
    text=greet(),
    fill="#808080",
    font=("Montserrat SemiBold", 16 * -1)
)
#################################################################

#Text-to-delete
canvas.create_text( #Background
    283.39056396484375,
    216.0,
    anchor="nw",
    text="(Starting the Magic",
    fill="#dbdbdb",
    font=("Montserrat Bold", 48 * -1)
)
canvas.create_text(
    311.3304748535156,
    275.0,
    anchor="nw",
    text="Loading Screens...)",
    fill="#dbdbdb",
    font=("Montserrat Bold", 48 * -1)
)


#################################################################

#window.after(1000, lambda: continous_playing_thread())

#################################################################
window.resizable(False, False)
window.mainloop()
###################################################################
