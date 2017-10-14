from tkinter import*
import random
import time;

WINDOW_TITLE = "Restaurant managment system"
WINDOW_GEOMETRY = "1300x700+0+0"
    
class Window(Tk):

    def __init__( self, parent = None ):
        Tk.__init__( self, parent )
        self.my_time = StringVar()
        self.calculator_input = StringVar()       

        self.initUI()
        self.update_time()
        
    def initUI(self):
        self.geometry(WINDOW_GEOMETRY)
        self.title(WINDOW_TITLE)
        self.vcmd = (self.register(self.validate_input), '%S', '%P')
        self.Top = Frame(self, width=1300, height = 70, bg="powder blue")
        self.Top.pack(side=TOP)

        self.left_frame = Frame(self, width = 880, height = 600, bd = 5,
                               bg = "light green", relief=SUNKEN)
        self.left_frame.pack(side=LEFT)

        self.right_frame = Frame(self, width = 400, height = 600, bd = 5,
                                bg = "powder blue", relief=SUNKEN)
        self.right_frame.pack(side=RIGHT)
        
        self.lblInfo = Label(self.Top, font=('Arial', 50, 'bold'),
                             text="Restaurant managment system",
                             fg="dark red", bd = 10, anchor='w')
        self.lblInfo.grid(row=0, column=0)

        #=============================Time=======================================#
        self.lblTime = Label(self.Top, font=('Tahoma', 30, 'bold'),
                             textvariable=self.my_time,fg="dark green",
                             bd = 10, anchor='w')
        self.lblTime.grid(row=1, column=0)
        
        #=============================Calculator==================================#
        self.txtDisplay = Entry(self.right_frame, font=('Arial', 14, 'bold'),
                                textvariable=self.calculator_input, bd=10,
                                insertwidth=4, bg="powder blue", justify='right',
                                validate = 'key', validatecommand = self.vcmd)
        self.txtDisplay.grid(columnspan=4)
        
        self.btn7 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="7", bg="Powder blue",
                           command=lambda:self.btn_click(7)).grid(row=2,column=0)

        self.btn8 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="8", bg="Powder blue",
                           command=lambda:self.btn_click(8)).grid(row=2,column=1)

        self.btn9 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="9", bg="Powder blue",
                           command=lambda:self.btn_click(9)).grid(row=2,column=2)
        
        self.btn_addition = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="+", bg="Powder blue",
                           command=lambda:self.btn_click("+")).grid(row=2,column=3)

        self.btn4 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="4", bg="Powder blue",
                           command=lambda:self.btn_click(4)).grid(row=3,column=0)

        self.btn5 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="5", bg="Powder blue",
                           command=lambda:self.btn_click(5)).grid(row=3,column=1)

        self.btn6 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="6", bg="Powder blue",
                           command=lambda:self.btn_click(6)).grid(row=3,column=2)
        
        self.btn_subtraction = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="-", bg="Powder blue",
                           command=lambda:self.btn_click("-")).grid(row=3,column=3)

        self.btn1 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="1", bg="Powder blue",
                           command=lambda:self.btn_click(1)).grid(row=4,column=0)

        self.btn2 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="2", bg="Powder blue",
                           command=lambda:self.btn_click(2)).grid(row=4,column=1)

        self.btn3 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="3", bg="Powder blue",
                           command=lambda:self.btn_click(3)).grid(row=4,column=2)
        
        self.btn_multiply = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="*", bg="Powder blue",
                           command=lambda:self.btn_click("*")).grid(row=4,column=3)

        self.btn0 = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="0", bg="Powder blue",
                           command=lambda:self.btn_click(0)).grid(row=5,column=0)

        self.btn_dot = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text=".", bg="Powder blue",
                           command=lambda:self.btn_click(".")).grid(row=5,column=1)

        self.btn_equals = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="=", bg="Powder blue",
                           command=lambda:self.on_btn_equals()).grid(row=5,column=2)
        
        self.btn_divide = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="/", bg="Powder blue",
                           command=lambda:self.btn_click("/")).grid(row=5,column=3)

        self.btn_left_p = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="(", bg="Powder blue",
                           command=lambda:self.btn_click("(")).grid(row=6,column=0)

        self.btn_right_p = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text=")", bg="Powder blue",
                           command=lambda:self.btn_click(")")).grid(row=6,column=1)

        self.btn_clear = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="C", bg="Powder blue",
                           command=lambda:self.on_btn_clear()).grid(row=6,column=2)
        
        self.btn_clear_all = Button(self.right_frame, padx=16, pady=16, bd=5, fg='black',
                           font=('Tahoma', 14, 'bold'), text="CA", bg="Powder blue",
                           command=lambda:self.on_btn_clear_all()).grid(row=6,column=3)
        
        
    def update_time(self):
        self.my_time.set(time.asctime(time.localtime(time.time())))
        #print(self.my_time.get())
        self.update_idletasks()
        self.after(1000, self.update_time)

        
    def btn_click(self,input):
        self.calculator_input.set(self.calculator_input.get() + str(input))


    def on_btn_clear(self):
        val = self.calculator_input.get();
        val = val[:len(val)-1]
        self.calculator_input.set(val)


    def on_btn_clear_all(self):
        self.calculator_input.set("")


    def on_btn_equals(self):
        self.calculator_input.set("{0:.3f}".format(eval(self.calculator_input.get())))


    def validate_input(self, char, entry_value):
        if char in '0123456789.-+*/()':
            return True
        else:
            return False

main_window = Window()
main_window.update()
