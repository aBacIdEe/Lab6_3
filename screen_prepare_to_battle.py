import tkinter

class Screen_PrepareToBattle (tkinter.Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        player1 = tkinter.Label(self, text = str(self.player1))
        player1.grid(row = 0, column = 0)
        player2 = tkinter.Label(self, text = str(self.player2))
        player2.grid(row = 1, column = 0)

        battle = tkinter.Button(self, text = "Battle", command = self.commence_battle_clicked)
        battle.grid(row = 1, column = 1)
        
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        