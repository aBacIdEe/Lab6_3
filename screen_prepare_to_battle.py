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
        tkinter.Label(self, text = "You").grid(row = 0, column = 0)
        tkinter.Label(self, text = "Computer").grid(row = 0, column = 1)
        player1 = tkinter.Label(self, text = self.player1.name)
        player1.grid(row = 1, column = 0)
        player2 = tkinter.Label(self, text = self.player2.name)
        player2.grid(row = 1, column = 1)

        imageSmall = tkinter.PhotoImage(file = "images/" + self.player1.small_image)
        w = tkinter.Label (self, image = imageSmall)
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid (row = 2, column = 0)
        imageSmall = tkinter.PhotoImage(file = "images/" + self.player2.small_image)
        w = tkinter.Label (self, image = imageSmall)
        w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.
        w.grid (row = 2, column = 1)

        tkinter.Label(self, text = f"HP: {self.player1.hit_points}").grid(row = 3, column = 0)
        tkinter.Label(self, text = f"HP: {self.player2.hit_points}").grid(row = 3, column = 1)
        tkinter.Label(self, text = f"ATK: {self.player1.strength}").grid(row = 4, column = 0)
        tkinter.Label(self, text = f"ATK: {self.player1.strength}").grid(row = 4, column = 1)
        tkinter.Label(self, text = f"DEX: {self.player1.dexterity}").grid(row = 5, column = 0)
        tkinter.Label(self, text = f"DEX: {self.player1.dexterity}").grid(row = 5, column = 1)


        battle = tkinter.Button(self, text = "Battle", command = self.commence_battle_clicked)
        battle.grid(row = 6, column = 1)
        
 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        