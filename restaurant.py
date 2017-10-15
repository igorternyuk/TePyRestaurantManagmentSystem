from tkinter import*
import random
import time;

WINDOW_TITLE = "Restaurant managment system"
WINDOW_GEOMETRY = "1300x600+0+0"
    
class Window(Tk):

    def __init__( self, parent = None ):
        Tk.__init__( self, parent )
        self.my_time = StringVar()
        self.calculator_input = StringVar()       

        self.rand_ref = StringVar()
        self.fries = StringVar()
        self.burger = StringVar()
        self.filet = StringVar()
        self.chicken_burger = StringVar()
        self.cheese_burger = StringVar()
        self.subtotal = StringVar()
        self.total = StringVar()
        self.service_charge = StringVar()
        self.drinks = StringVar()
        self.tax = StringVar()
        self.cost = StringVar()

        self.prices = {}
        
        self.initUI()
        self.update_time()
        self.load_prices("prices.dat");
        
    def initUI(self):
        self.geometry(WINDOW_GEOMETRY)
        self.title(WINDOW_TITLE)
        self.vcmd = (self.register(self.validate_input), '%S', '%P')
        self.vncmd = (self.register(self.validate_numeric_input), '%S', '%P')
        self.Top = Frame(self, width=1300, height = 70)
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
        self.txtDisplay = Entry(self.right_frame,font=('Arial', 20, 'bold'),
                                textvariable=self.calculator_input, bd=10,
                                insertwidth=4, bg="powder blue", justify='right',
                                validate = 'key', validatecommand = self.vcmd)
        self.txtDisplay.grid(columnspan=4)
        
        self.btn7 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="7", bg="Powder blue",
                           command=lambda:self.btn_click(7)).grid(row=2,column=0)

        self.btn8 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="8", bg="Powder blue",
                           command=lambda:self.btn_click(8)).grid(row=2,column=1)

        self.btn9 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="9", bg="Powder blue",
                           command=lambda:self.btn_click(9)).grid(row=2,column=2)
        
        self.btn_addition = Button(self.right_frame, padx=16, pady=10, bd=5,
                                   fg='black', font=('Tahoma', 22, 'bold'),
                                   text="+", bg="Powder blue",
                                   command=lambda:self.btn_click("+"))
        self.btn_addition.grid(row=2,column=3)

        self.btn4 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="4", bg="Powder blue",
                           command=lambda:self.btn_click(4)).grid(row=3,column=0)

        self.btn5 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="5", bg="Powder blue",
                           command=lambda:self.btn_click(5)).grid(row=3,column=1)

        self.btn6 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="6", bg="Powder blue",
                           command=lambda:self.btn_click(6)).grid(row=3,column=2)
        
        self.btn_subtraction = Button(self.right_frame, padx=22, pady=10, bd=5,
                                      fg='black', font=('Tahoma', 22, 'bold'),
                                      text="-", bg="Powder blue",
                           command=lambda:self.btn_click("-"))
        self.btn_subtraction.grid(row=3,column=3)
        
        self.btn1 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="1", bg="Powder blue",
                           command=lambda:self.btn_click(1)).grid(row=4,column=0)

        self.btn2 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="2", bg="Powder blue",
                           command=lambda:self.btn_click(2)).grid(row=4,column=1)

        self.btn3 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="3", bg="Powder blue",
                           command=lambda:self.btn_click(3)).grid(row=4,column=2)
        
        self.btn_multiply = Button(self.right_frame, padx=20, pady=10, bd=5,
                                   fg='black', font=('Tahoma', 22, 'bold'),
                                   text="*", bg="Powder blue",
                                   command=lambda:self.btn_click("*"))
        self.btn_multiply.grid(row=4,column=3)
        
        self.btn0 = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="0", bg="Powder blue",
                           command=lambda:self.btn_click(0)).grid(row=5,column=0)

        self.btn_dot = Button(self.right_frame, padx=28, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text=".", bg="Powder blue",
                           command=lambda:self.btn_click(".")).grid(row=5,column=1)

        self.btn_equals = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="=", bg="Powder blue",
                           command=lambda:self.on_btn_equals()).grid(row=5,column=2)
        
        self.btn_divide = Button(self.right_frame, padx=20, pady=10, bd=5, fg='black',
                           font=('Tahoma', 22, 'bold'), text="/", bg="Powder blue",
                           command=lambda:self.btn_click("/")).grid(row=5,column=3)

        self.btn_left_p = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 18, 'bold'), text="(", bg="Powder blue",
                           command=lambda:self.btn_click("(")).grid(row=6,column=0)

        self.btn_right_p = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 18, 'bold'), text=")", bg="Powder blue",
                           command=lambda:self.btn_click(")")).grid(row=6,column=1)

        self.btn_clear = Button(self.right_frame, padx=24, pady=10, bd=5, fg='black',
                           font=('Tahoma', 18, 'bold'), text="C", bg="Powder blue",
                           command=lambda:self.on_btn_clear()).grid(row=6,column=2)
        
        self.btn_clear_all = Button(self.right_frame, padx=14, pady=10, bd=5,
                                    fg='black', font=('Tahoma', 18, 'bold'),
                                    text="CA", bg="Powder blue",
                                    command=lambda:self.on_btn_clear_all())
        self.btn_clear_all.grid(row=6,column=3)
        #=============================Restaurant left column=========================#

        self.lbl_reference = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                   text="Reference",bd = 8, bg = "light green",
                                   anchor='w')
        self.lbl_reference.grid(row = 0, column = 0)
        self.txt_reference = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                   textvariable=self.rand_ref,bd = 8, insertwidth=4,
                                   bg = "powder blue", justify='right',
                                   validate = 'key', validatecommand = self.vncmd)
        self.txt_reference.grid(row = 0, column = 1)

        self.lbl_fries = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                               text="Large fries",bd = 8, bg = "light green",
                               anchor='w')
        self.lbl_fries.grid(row = 1, column = 0)
        self.txt_fries = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                               textvariable=self.fries,bd = 8, insertwidth=4,
                               bg = "Goldenrod", justify='right',
                               validate = 'key', validatecommand = self.vncmd)
        self.txt_fries.grid(row = 1, column = 1)

        self.lbl_burger = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                text="Burger",bd = 8, bg = "light green",
                                anchor='w')
        self.lbl_burger.grid(row = 2, column = 0)
        self.txt_burger = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                textvariable=self.burger,bd = 8, insertwidth=4,
                                bg = "Khaki", justify='right',
                                validate = 'key', validatecommand = self.vncmd)
        self.txt_burger.grid(row = 2, column = 1)

        self.lbl_filet = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                               text="Filet",bd = 8, bg = "light green",
                               anchor='w')
        self.lbl_filet.grid(row = 3, column = 0)
        self.txt_filet = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                               textvariable=self.filet,bd = 8, insertwidth=4,
                               bg = "Burlywood", justify='right',
                               validate = 'key', validatecommand = self.vncmd)
        self.txt_filet.grid(row = 3, column = 1)

        self.lbl_chicken = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                 text="Chicken meal",bd = 8, bg = "light green",
                                 anchor='w')
        self.lbl_chicken.grid(row = 4, column = 0)
        self.txt_chicken = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                 textvariable=self.chicken_burger,bd = 8,
                                 insertwidth=4, bg = "Pale Goldenrod",
                                 justify='right', validate = 'key',
                                 validatecommand = self.vncmd)
        self.txt_chicken.grid(row = 4, column = 1)

        self.lbl_cheese = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                text="Cheese meal",bd = 8, bg = "light green",
                                anchor='w')
        self.lbl_cheese.grid(row = 5, column = 0)
        self.txt_cheese = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                textvariable=self.cheese_burger,bd = 8,
                                insertwidth=4,
                                bg = "Light Yellow", justify='right',
                                validate = 'key', validatecommand = self.vncmd)
        self.txt_cheese.grid(row = 5, column = 1)

       #=============================Restaurant right column=======================#

        self.lbl_drinks = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                   text="Drinks",bd = 8, bg = "light green",
                                   anchor='w')
        self.lbl_drinks.grid(row = 0, column = 2)
        self.txt_drinks = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                   textvariable=self.drinks,bd = 8, insertwidth=4,
                                   bg = "powder blue", justify='right')
        self.txt_drinks.grid(row = 0, column = 3)

        self.lbl_cost = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                               text="Cost of meal",bd = 8, bg = "light green",
                               anchor='w')
        self.lbl_cost.grid(row = 1, column = 2)
        self.txt_cost = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                   textvariable=self.cost,bd = 8, insertwidth=4,
                                   bg = "powder blue", justify='right')
        self.txt_cost.grid(row = 1, column = 3)

        self.lbl_service = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                text="Service charge",bd = 8, bg = "light green",
                                anchor='w')
        self.lbl_service.grid(row = 2, column = 2)
        self.txt_service = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                 textvariable=self.service_charge,bd = 8,
                                 insertwidth=4,bg = "powder blue",
                                 justify='right')
        self.txt_service.grid(row = 2, column = 3)

        self.lbl_state_tax = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                   text="State tax",bd = 8, bg = "light green",
                                   anchor='w')
        self.lbl_state_tax.grid(row = 3, column = 2)
        self.txt_state_tax = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                   textvariable=self.tax,bd = 8, insertwidth=4,
                                   bg = "powder blue", justify='right')
        self.txt_state_tax.grid(row = 3, column = 3)

        self.lbl_subtotal = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                                  text="Subtotal",bd = 8, bg = "light green",
                                  anchor='w')
        self.lbl_subtotal.grid(row = 4, column = 2)
        self.txt_subtotal = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                                  textvariable=self.subtotal,bd = 8,
                                  insertwidth=4, bg = "powder blue",
                                  justify='right')
        self.txt_subtotal.grid(row = 4, column = 3)

        self.lbl_total = Label(self.left_frame, font=('Tahoma', 20, 'bold'),
                               text="Total",bd = 8, bg = "light green",
                               anchor='w')
        self.lbl_total.grid(row = 5, column = 2)
        self.txt_total = Entry(self.left_frame, font=('Tahoma', 14, 'bold'),
                               textvariable=self.total,bd = 8, insertwidth=4,
                               bg = "powder blue", justify='right')
        self.txt_total.grid(row = 5, column = 3)
        
       #=====================================Buttons============================#

        self.btn_total = Button(self.left_frame, font=('Tahoma', 20, 'bold'),
                                fg = 'black', text="Total", padx=16, pady=8,
                                width = 5, bd=5)
        self.btn_total.grid(row=7,column=0)
        self.btn_total.bind("<Button-1>", self.calculate_all)
        self.btn_total.bind("<Return>", self.calculate_all)
        
        self.btn_reset = Button(self.left_frame, font=('Tahoma', 20, 'bold'),
                                fg = 'black', text="Reset", padx=16, pady=8,
                                width = 5, bd=5,command=lambda:self.reset())
        self.btn_reset.grid(row=7,column=1)
        self.btn_exit = Button(self.left_frame, font=('Tahoma', 20, 'bold'),
                               fg = 'black', text="Exit", padx=16, pady=8,
                               width = 5, bd=5, command=lambda:self.quit_app())
        self.btn_exit.grid(row=7,column=2)

    def update_time(self):
        self.my_time.set(time.asctime(time.localtime(time.time())))
        #print(self.my_time.get())
        self.update_idletasks()
        self.after(1000, self.update_time)


    def load_prices(self, pathToFile):
        fi = open(pathToFile, "r")
        lines = fi.readlines()
        N=len(lines)-1
        for i in range(0,12,2):
            key = lines[i]
            key = key[:len(key)-1]
            val = float(lines[i+1])
            self.prices[key] = val
        print(self.prices)
        fi.close()    

    def btn_click(self,input):
        self.calculator_input.set(self.calculator_input.get() + str(input))


    def on_btn_clear(self):
        val = self.calculator_input.get();
        val = val[:len(val)-1]
        self.calculator_input.set(val)


    def on_btn_clear_all(self):
        self.calculator_input.set("")


    def on_btn_equals(self):
        self.calculator_input.set(("{0:.3f}".
                                   format(eval(self.calculator_input.get()))))


    def validate_input(self, char, entry_value):
        if char in '0123456789.-+*/()':
            return True
        else:
            return False

    def validate_numeric_input(self, char, entry_value):
        if char in '0123456789':
            return True
        else:
            return False

    def calculate_all(self, event):
        self.rand_ref.set(str(random.randint(10000,1000000)))
        cost_of_fries = 0
        if self.fries.get() != "":
            cost_of_fries = float(self.fries.get()) * self.prices['Fries']
        cost_of_burger = 0
        if self.burger.get() != "":
            cost_of_burger = float(self.burger.get()) * self.prices['Burger']
        cost_of_filet = 0
        if self.filet.get() != "":
            cost_of_filet = float(self.filet.get()) * self.prices['Filet']
        cost_of_chicken_burger = 0
        if self.chicken_burger.get() != "":
            cost_of_chicken_burger = (float(self.chicken_burger.get()) *
            self.prices['Cnicken burger'])
        cost_of_cheese_burger = 0
        if self.cheese_burger.get() != "":
            cost_of_cheese_burger = (float(self.cheese_burger.get()) *
            self.prices['Cheese burger'])
        cost_of_drinks = 0
        if self.drinks.get() != "":
            cost_of_drinks = float(self.drinks.get()) * self.prices['Drinks']

        total_meal = (cost_of_fries + cost_of_burger + cost_of_filet +
                    cost_of_chicken_burger + cost_of_cheese_burger)
        subtotal = total_meal + cost_of_drinks
        service = subtotal * 0.05
        tax = subtotal * 0.2
        total = subtotal + service + tax

        self.cost.set(str('$%.3f' % (total_meal)))
        self.subtotal.set(str('$%.3f' % (subtotal)))
        self.total.set(str('$%.3f' % (total)))
        self.service_charge.set(str('$%.3f' % (service)) )       
        self.tax.set(str('$%.3f' % (tax)))



    def reset(self):
        self.rand_ref.set("")
        self.fries.set("")
        self.burger.set("")
        self.filet.set("")
        self.chicken_burger.set("")
        self.cheese_burger.set("")
        self.subtotal.set("")
        self.total.set("")
        self.service_charge.set("")
        self.drinks.set("")
        self.tax.set("")
        self.cost.set("")
                      
        
    def quit_app(self):
        self.destroy()

main_window = Window()
main_window.update()
