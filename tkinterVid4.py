import tkinter as tk

LARGE_FONT = ('Verdana', 12)


class SeaofBTCapp(tk.Tk):#Tk is a class that represents the root window of a 
                        #tkinter GUI. This root window’s mainloop method 
                        #handles all the events for the GUI, so it’s important to
                        #create only one instance of Tk.
                        #we want to inherit everithing from tk.TK
    def __init__(self, *args, **kwargs):#Initialize class SeaofBTCapp
                                        #*args any number of variables, 
                                        #**kwargs Keyboard arguments, 
                                        #basicaly dictionaries
        tk.Tk.__init__(self, *args, **kwargs)  #Initialize the class root window
                                                #with the same name as the 
                                                #new object you create
        container = tk.Frame(self)  #always need a container that will contain everithing
                                    #Frame is what you think as a window
        #Pack or Grid are your 2 option to layout things
        #Pack is easy but litte control on location buy easy
        #Grid more control but take longer to set up
        container.pack(side = 'top', fill = 'both', expand = True)#locates the container into 
        #frame and defines how to fill and expand
        
        #now we create and initial paramentes the grid inside container
        container.grid_rowconfigure(0, weight=1)#minium size and priority
        container.grid_columnconfigure(0, weight=1)
        
        #specify the dictionary
        self.frames = {}#contains all the pages of you application
        
        for F in (StartPage, PageOne, PageTwo):
        
            frame = F(container, self)#not defined yet but it is the initial page
            
            self.frames[F] = frame # reference the page in frame
            
            #creates the first cell of the grid in row 0 column 0 and sticky to all 4 sides
            frame.grid(row=0, column=0, sticky='nsew')
        
        #show the frame
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()# method to bring the page to the front
        
#this was the most complicaded part but is just the baseline to all prigrams, adding pages is easy from now on.



#now adding pages
#start page that will link to other pages
class StartPage(tk.Frame):#we want to inherit everithing from tk.frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #add a button to navigate to a different page
        button1 = tk.Button(self, text='Visit Page 1', 
                            command=lambda: controller.show_frame(PageOne))
        #lambda creates a function on the fly so you can pass parameters
        button1.pack()
        
        #add a button to navigate to a different page
        button2 = tk.Button(self, text='Visit Page 2', 
                            command=lambda: controller.show_frame(PageTwo))
        #lambda creates a function on the fly so you can pass parameters
        button2.pack()        
        

#create all other pages       
class PageOne(tk.Frame):       
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Page One!!!', font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #add a button to navigate to a different page
        button1 = tk.Button(self, text='Back to Home', 
                            command=lambda: controller.show_frame(StartPage))
        #lambda creates a function on the fly so you can pass parameters
        button1.pack()

        #add a button to navigate to a different page
        button2 = tk.Button(self, text='Page Two', 
                            command=lambda: controller.show_frame(PageTwo))
        #lambda creates a function on the fly so you can pass parameters
        button2.pack()

    tk.Frame

class PageTwo(tk.Frame):#we want to inherit everithing from tk.frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text='Page Two!!!', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        #add a button to navigate to a different page
        button1 = tk.Button(self, text='Back to Home', 
                            command=lambda: controller.show_frame(StartPage))
        #lambda creates a function on the fly so you can pass parameters
        button1.pack()

        
        #add a button to navigate to a different page
        button2 = tk.Button(self, text='Visit Page 1', 
                            command=lambda: controller.show_frame(PageOne))
        #lambda creates a function on the fly so you can pass parameters
        button2.pack()
        



#run the code
app = SeaofBTCapp()
app.mainloop()



















