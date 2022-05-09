# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:06:48 2021

@author: Haitham 
"""
# Import modules
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Default values for min and max
min_val=-5
max_val=5

# for converting from string to mathematical expression
replacements = {
    'sin':  'np.sin',
    'cos':  'np.cos',
    'tan':  'np.tan',
    'exp':  'np.exp',
    'sqrt': 'np.sqrt',
    '^':    '**',
    'X':    'x',
    
}

# Start the Tkinter GUI
root = Tk()
# Make the title name
root.title("Equation ploting GUI")
# Make an icon 
root.iconbitmap("Master.ico")
# Choose the size
root.geometry("800x700")
# doesn't make it reizable 
root.resizable(0, 0)

# call function when we click on min_box
def clickMin(*args):
    min_box.delete(0, 'end')

# call function when we click on max_box  
def clickMax(*args):
    max_box.delete(0, 'end')


# call function when we leave on min or max box
def leave(*args):
    # We can write only when we are focusing on it 
    root.focus()
  
  
def plot():
    '''
     This function is used to plot the equation that we have written in 
     equation_box, the min value of x and max value of x are given from user
    '''
    # Make them global to use them in the funciton
    global min_val, max_val
    
    
    # Chech if the user entered valid min
    if min_box.get()!="" and min_box.get()!="Min value":
        # If the user doesn't enter valid min number pop up an error message
        try:
            min_val=eval(min_box.get())
        except:
             messagebox.showerror(title="Error",
                message="Enter valid min")
    
    # Chech if the user entered valid min    
    if max_box.get()!="" and max_box.get()!="Max value":
        # If the user doesn't enter valid max number pop up an error message 
        try:
            max_val=eval(max_box.get())
        except:
             messagebox.showerror(title="Error",
                message="Enter valid max")
             
    # If max value of x is greater then min value of x pop up a warning message
    if max_val< min_val:
        messagebox.showwarning(title="Warning",
                message="Max should be greater than min")
    
    # Choose points from min value to max value to plot the equation
    x = np.linspace(min_val,max_val,100)
    
    # Get the value from the equation_box entry to the equation variable 
    equation=equation_box.get()
    
    # Replace any string value with it's mathematical expression
    for old, new in replacements.items():
        equation = equation.replace(old, new)
    
    try:
        # Evaluate function
        y = eval(equation)
    except SyntaxError:
        # If we have  syntax error raise an error message 
        messagebox.showerror(title="SyntaxError",
                message="Make sure to enter *, /, +, - or ^ between numbers")
        raise SyntaxError("Make sure to enter *, /, +, - or ^ between numbers")
    except:
        # If we have  any error raise an error message 
        messagebox.showerror(title="Error",
                             message="The only variable should be x or X")
        raise Exception("The only variable should be x or X")
        
    
    
    # setting the axes at the centre
    fig = plt.figure()
    
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    # Change the background color 
    ax.set_facecolor('#efefef')
    ax.set_xlabel("x")
                     
                    

    # plot the function
    plt.plot(x,y, 'r')
    
    # Draw the equation at Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(relx=0.25, rely=0.5)
    canvas.draw()
    # show the plot
    #plt.show()


# Make a label to ask the user to enter the equation
label = Label(root, text="Please Enter the eqution", font=('Helvetica',15),
              fg='#065478')      
# Make a box to make the user to write the equation in it
equation_box = Entry(root,font=('Helvetica',13), border=4 )

# Make a box to make the user to write the min and max values in it
min_box = Entry(root,font=('Helvetica',10), border=4 ,textvariable="min", width=10)
max_box = Entry(root,font=('Helvetica',10), border=4, width=10)

# Write a default values in them
min_box.insert(0, 'Min value')
max_box.insert(0, 'Max value')

# Make a button to plot the equation
plot_btn = Button(root, text="Plot the equation", command=plot,
                  font=('Helvetica'))

# Put the Label in the window
label.place(relx=0.35, rely=0.1)

# Put the equation_box in the window
equation_box.place(relx=0.35, rely=0.2)

# Put the min and max box in the window
min_box.place(relx=0.36, rely=0.3)
max_box.place(relx=0.48, rely=0.3)

# Put the plot_btn in the window
plot_btn.place(relx=0.39, rely=0.4)

# Use bind method
# when we click on the box clear the placeholder
min_box.bind("<Button-1>", clickMin)

# when we click on the box clear the placeholder
min_box.bind("<Leave>", leave)

# Use bind method
# when we click on the box clear the placeholder
max_box.bind("<Button-1>", clickMax)

# when we leave the box clear the placeholder
max_box.bind("<Leave>", leave)

# Loop the GUI
root.mainloop()


'''
https://www.kindacode.com/article/examples-of-numpy-linspace-in-python/#:~:text=The%20numpy.linspace%20%28%29%20function%20returns%20an%20ndarray%20with,using%20the%20numpy.linspace%20%28%29%20function%20in%20Python%20programs.
https://stackoverflow.com/questions/31440167/placing-plot-on-tkinter-main-window-in-python
https://docs.python.org/3/library/tkinter.messagebox.html#:~:text=The%20tkinter.messagebox%20module%20provides%20a%20template%20base%20class,and%20layouts%20include%20but%20are%20not%20limited%20to%3A

'''