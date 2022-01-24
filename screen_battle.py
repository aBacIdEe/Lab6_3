import tkinter

from characters import Character

class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        self.p1 = tkinter.Label(self, text = str(self.player1))
        self.p1.grid(row = 0, column = 0)
        self.p2 = tkinter.Label(self, text = str(self.player2))
        self.p2.grid(row = 1, column = 0)

        self.attackBtn = tkinter.Button(self, text = "Attack", command = self.attack_clicked)
        self.attackBtn.grid(row = 0, column = 1)
        

        self.result1 = tkinter.Button(self, text = " ")
        self.result1.grid(row = 2, column = 0, columnspan = 2)
        self.result2 = tkinter.Button(self, text = " ")
        self.result2.grid(row = 3, column = 0, columnspan = 2)
        self.result3 = tkinter.Button(self, text = " ")
        self.result3.grid(row = 4, column = 0, columnspan = 2)
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''        
        self.result1["text"] = self.player1.attack(self.player2)
        self.p2["text"] = str(self.player2)
        if self.player2.hit_points <= 0:
            self.result3["text"] = self.player2.get_death_message()
            self.create_exit()


        self.result2["text"] = self.player2.attack(self.player2)
        self.p1["text"] = str(self.player1)
        if self.player1.hit_points <= 0:
            self.result3["text"] = self.player1.get_death_message()
            self.create_exit()
        
    def create_exit(self):
        self.attackBtn.destroy()
        exit = tkinter.Button(self, text = "Exit", command = self.exit_clicked)
        exit.grid(row = 1, column = 1)
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()
  
            
            
            
            