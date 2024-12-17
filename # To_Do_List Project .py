# To_Do_List Project
# Three Classes at least and one of them one of them is(Abstract Base Class(ABC)).
# Using of External  Libraries of Python (Tkinter).

# Abeer Yahya & Aisha Hussein .


#_____________________________________________________________________________________________

import tkinter as tk                        # importing the tkinter module as tk 
from tkinter import ttk                     # importing the ttk module from the tkinter library , ttk: Provides themed widgets for better aesthetics (like Label, Button
from tkinter import messagebox              # importing the messagebox module from the tkinter library , messagebox: Used for displaying dialog boxes (e.g., error messages, warning ,confirmation prompts).
from abc import ABC, abstractmethod         # Imports the Abstract Base Class (ABC) module, used to define abstract methods.

#_____________________________________________________________________________________________

class AbstractToDoList(ABC):                     #This is a base class that defines the structure of the To-Do List operations using abstract methods.
    
    @abstractmethod                              # Abstract methods: Methods that must be implemented in a subclass.
    def add_task(self):                          # To add a task.
        pass

    @abstractmethod
    def delete_task(self):                       # To delete a specific task.
        pass

    @abstractmethod
    def delete_all_tasks(self):                  # To delete all tasks.
        pass
         
    @abstractmethod
    def update_task_list(self):                  # To refresh the task list.
        pass

#_______________________________________________________________________________________________


class User_Functions (AbstractToDoList):                      # This class implements the methods defined in the AbstractToDoList

    def add_task(self):                         
        task_string = self.task_field.get()                   # Gets the text from the input field (self.task_field). The get() method in Python is used to retrieve a value or data from an object. Its exact behavior depends on the type of object it is called on.
        if len(task_string) == 0:                             # If the field is empty, displays an error using messagebox.showinfo.
            messagebox.showinfo("Error", "Field is Empty.") 

            """ messagebox.showinfo(title, message) : The showinfo() function is a method provided by the messagebox module in the tkinter library. It is used to display an informational message to the user in a pop-up dialog box.
                When called, it opens a modal window (a pop-up) with the specified title and message.
                The user must close the window (by clicking "OK") to proceed with the program. """ 
                                                                                                                                                        
        else:                                                 # If valid, adds the task to the list (self.tasks) .
            self.tasks.append(task_string)                     
            self.update_task_list()                           # refreshes the display using self.update_task_list.
            self.task_field.delete(0, "end")                  # Clears the input field after adding the task

    #---------------------------------------------------------


    def delete_task(self):                                                                    
        try:                                                                              # Attempts to delete the selected task from the list.
            selected_task = self.task_listbox.get(self.task_listbox.curselection())       # self.task_listbox.curselection() returns the index of the currently selected item in the Listbox.
                                                                                          # self.task_listbox.get(index) is used to fetch the task string at the index returned by curselection().
                                                                                          # If the Listbox contains ["Task1", "Task2", "Task3"] and the second item ("Task2") is selected, curselection() returns (1,), and get(1) retrieves "Task2".


            if selected_task in self.tasks:                                               # Checks if the task is in self.tasks and removes it.
                self.tasks.remove(selected_task)                                          
                self.update_task_list()
        except tk.TclError:                                                               # Displays an error if no task is selected.
            messagebox.showinfo("Error", "No Task Selected. Cannot Delete.")


   #----------------------------------------------------------------

    def delete_all_tasks(self):

        confirm = messagebox.askyesno("Delete All", "Are you sure?")        # Displays a confirmation dialog using messagebox.askyesno.

        """ messagebox.askyesno(title, message) : The askyesno() function is part of the messagebox module in tkinter. It displays a confirmation dialog box to the user with "Yes" and "No" buttons, allowing the user to confirm or reject an action.
            Returns True if the user clicks Yes.
            Returns False if the user clicks No.     """ 
   
        if confirm:                                                         # If confirmed, clears all tasks from self.tasks and updates the display.
            self.tasks.clear()                      
            self.update_task_list()
 

   #------------------------------------------------------------------


    def update_task_list(self):
        self.clear_task_list()        # Step 1: Clear the existing items from the Listbox.Removes all items in the Listbox between the first index (0) and the last index (end). After this operation, the Listbox is empty.
        
        """ When update_task_list() refreshes the Listbox, the old data must first be removed.
            If this step were skipped, the Listbox would keep appending the new data on top of the old data, resulting in duplicate entries.
        """

        for task in self.tasks:                                  # Step 2: Iterate over the tasks list.
            self.task_listbox.insert("end", task)                # Step 3: Adds each task to the end of the Listbox.        # listbox.insert(index, item) : insert() method is used to add items to a Tkinter Listbox widget


    #------------------------------------------------------------------

    def clear_task_list(self):
         self.task_listbox.delete(0, "end")          #Deletes all entries from the Listbox.

   
    #------------------------------------------------------------------

    def close_app(self):
        self.root.destroy()       # using the destroy() method to close the application  
        
        """ The .destroy() method is a built-in function in Tkinter that destroys the specified widget and all of its children. Once a widget is destroyed, it is permanently removed from the GUI, and you cannot interact with it anymore.
            root.destroy() :When you call .destroy() on the root window (root), it terminates the entire Tkinter application and closes the window.  
        """                         
#_______________________________________________________________________________________________


class ToDoListWidget(User_Functions):



    def __init__(self, root):            #__init__: The constructor initializes the main window (self.root), the tasks list, and calls methods to set up the GUI and update the task list.

        self.tasks = []                  #The self parameter refers to the current instance of the class.     # Initialize  tasks list.

        self.root = root                 #The root object represents the main application window created by Tkinter. Using self.root makes root accessible as an attribute of the class, allowing it to be used throughout the class for customization and control of the main window.


        self.root.title("To-Do List")                  # The title() method is used to set the string displayed in the title bar of the window.
        self.root.geometry("500x450+750+250")          # "500x450": Sets the width to 500 pixels and the height to 450 pixels , 750 is the number of pixels from the left edge of the screen , 250 is the number of pixels from the top edge of the screen.
     
        self.root.resizable( True , 0)                    # Disables resizing of the application window. The resizable(width, height) method allows control over whether the window can be resized horizontally (width) and vertically (height). Setting both parameters to 0 means the window size is fixed, and the user cannot resize it.

        self.root.configure(bg="#0000FF")              #  Sets the background color of the application window.bg="#0000FF": Sets the background color  (#0000FF : Hex color code ).

           
        # Create GUI layout:
        self.create_widgets()                          
        self.update_task_list()
        
#=====================================================



    def create_widgets(self):    # The create_widgets function is responsible for setting up the graphical components (widgets) of the To-Do List application. This includes frames, labels, input fields, buttons, and the listbox used to display tasks.

        
        # Frames :                                                       # Frames are container widgets used to organize other widgets. They help in grouping related widgets visually.
        header_frame = tk.Frame(self.root, bg="#0000FF")                 # header_frame: Holds the title of the application.      
        functions_frame = tk.Frame(self.root, bg="#0000FF")              # functions_frame: Contains input fields and buttons.
        listbox_frame = tk.Frame(self.root, bg="#0000FF")                # listbox_frame: Displays the tasks in a listbox.

        header_frame.pack(fill="both")                                   # fill="both": Ensures the widget fully stretches in both width and height to fill the space it occupies.
        functions_frame.pack(side="left", expand=True, fill="both")      # side="left": Places the widget along the left edge of the parent.
        listbox_frame.pack(side="right", expand=True, fill="both")       # expand=True: Allows the widget to claim extra space if available, ensuring it dynamically adjusts as the parent resizes.

        #--------------------------------------------------------------------

        #Header:

        header_label = ttk.Label(
            header_frame,                                       # Creates a header label inside header_frame.                              
            width=10 ,                                              
            text="  ToDo List",
            font=("Times New Roman Greek", 38 , "italic"),      # font=("FontName", FontSize, "Style")
            background="#FFFFFF",                               # Background is wight.
            foreground="#000000"                                # text is black. 
        )
        header_label.pack( pady=20)                     #The pack() method organizes widgets by "packing" them into the parent widget.
                                                                # The arguments padx and pady are used with the pack() method to add external padding (space around the widget).
                                                 


        #--------------------------------------------------------------------


        # Task input:
        
        #Task Label:
        task_label = ttk.Label(                              # Creates a label with the text "Enter the Task:" in the functions_frame.
            functions_frame,              
            text="Enter the Task:",
            font=("Times New Roman Greek", 11, "bold"),      #font=("FontName", FontSize, "Style")
            background="#FAEBD7",                            #Background is light beige (#FAEBD7).
            foreground="#000000"                             #text is black.
        )
        task_label.place(x=30, y=40)

        #==========================
       
        #Task Field:
        self.task_field = ttk.Entry(                         # Creates an entry field (ttk.Entry) for user input.
            functions_frame,
            font=("Consolas", 12),                           #font=("FontName", FontSize)
            width=18,
            background="#FFF8DC",                             
            foreground="#000000"                              #text is black.
        )
        self.task_field.place(x=30, y=80)            # place() Method: Allows precise control of widget placement. ,x increases as you move right , y increases as you move down.

        #--------------------------------------------------------------------


        # Buttons:                                                                            #Buttons are interactive elements for performing actions.           

        add_button = ttk.Button(                                                              #Creates a button labeled "Add Task".                                
            functions_frame, text="Add Task", width=24, command=self.add_task                 # command is used with Button widgets to trigger actions on click.command specifies what happens when an item is selected.
        )
        del_button = ttk.Button(
            functions_frame, text="Delete Task", width=24, command=self.delete_task           #command=self.add_task: Binds the add_task method to this button. Clicking it triggers the method.
        )
        del_all_button = ttk.Button(
            functions_frame, text="Delete All Tasks", width=24, command=self.delete_all_tasks       
        )
        exit_button = ttk.Button(
            functions_frame, text="Exit", width=24, command=self.close_app
        )
       

        # Places the buttons vertically below each other in functions_frame:

        add_button.place(x=30, y=120)            # place() Method: Allows precise control of widget placement. ,x increases as you move right , y increases as you move down.
        del_button.place(x=30, y=160)             
        del_all_button.place(x=30, y=200)
        exit_button.place(x=30, y=240)
 
        #----------------------------------------------------------------------


        # Task Listbox
        self.task_listbox = tk.Listbox(
            listbox_frame,                          #Creates a listbox inside listbox_frame.
            width=26,                               #Dimensions: 26 characters wide and 13 rows high.
            height=13,
            selectmode="SINGLE",                    # Selection Mode: SINGLE allows only one task to be selected at a time.
            background="#FFFFFF",                   # Background: White.
            foreground="#000000",                   # Text: Black.
            selectbackground="#CD853F",             #Selected Item: Background becomes golden brown (#CD853F) .
            selectforeground="#FFFFFF"              # text becomes white.
        )
        self.task_listbox.place(x=70, y=20)           # place() Method: Allows precise control of widget placement. ,x increases as you move right , y increases as you move down.

#_______________________________________________________________________________________________


if __name__ == "__main__":
    root = tk.Tk()                                    # tk.Tk(): Creates the main application window.
    app = ToDoListWidget(root)                        # Creating an instance of the ToDoListWidget Class.
    user_functions = User_Functions()                 # Creating an instance of the  User_Functions Class.
    user_functions.root = root                         
    user_functions.task_field = app.task_field        
    user_functions.task_listbox = app.task_listbox    
    user_functions.tasks = app.tasks                  # Links task_field, task_listbox, and tasks from ToDoListWidget to User_Functions.
    root.mainloop()                                  # : Keeps the application running in an event loop.
