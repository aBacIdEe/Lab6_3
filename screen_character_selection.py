import tkinter

class Screen_CharacterSelection (tkinter.Frame):
    def __init__ (self, master, roster, callback_on_selected):
        super().__init__(master)
        # Save the CharacterRoster  
        self.roster = roster
        # Save the method reference to which we return control after the player hits "Character Selected"
        self.callback_on_selected = callback_on_selected

        self.grid()
        self.create_widgets()
        
    def create_widgets (self):
        '''
        This method creates all of the widgets character selector page.
        The information about each character should be derived from self.roster, 
        which is a CharacterRoster loaded from battle_characters.txt. 
        The layout should NOT be hard-coded: if you re-order, alter, or remove entries 
        in battle_characters.txt, the layout should automatically reflect those changes. 
        
        ########
        
        The radio buttons on this page should all use the variable "self.character_index_index".  
        The values of the radio buttons must be a number equally the position of the character in the list. 
        For example, if the characters listed are Troll, Elf, Human, and Dwarf.  self.character_index would equal 0 
        for the Troll, 1 for the Elf, and so forth.  
        
        The variable self.character_index has been instantiated for your convenience below.
        
        ########

        Here is some sample code for including an image on a page:   (char is a Character object)
            
            imageSmall = tkinter.PhotoImage(file="images/" + char.small_image);
            w= tkinter.Label (self,
                        image = imageSmall, 
                         )
            w.photo = imageSmall # saving the image as a property is required for "saving" the image. It's odd.

            w.grid (ADD PARAMETERS HERE)
        '''
        self.character_index = tkinter.StringVar()
        self.character_index.set(None)
        counter = 0
        for character in self.roster.character_list:
            character = str(character).split("; ")
            button = tkinter.Radiobutton(self, text = f"{character[0]}" , variable = self.character_index, value = counter)
            button.grid(row = counter, column = 0)

            self.smallImage = character[0].lower() + "_100.gif"
            imageFile = tkinter.PhotoImage(file = "images/" + self.smallImage)
            image = tkinter.Label(self, image = imageFile)
            image.photo = imageFile
            image.grid(row = counter, column = 1)

            for i in range(1, 4):
                detail = tkinter.Label(self, text = f"{character[i]}")
                detail.grid(row = counter, column = i + 1)
            
            counter += 1
        
        self.confirm = tkinter.Button(self, text = "Confirm", command = self.selected_clicked)
        self.confirm.grid(row = counter, column = 2)
       
 
    def selected_clicked(self):
        ''' This method is to be called when the "Character Selected!" button is clicked. 
            Notice that it passes self.character_index back to the callback method. '''         
        self.callback_on_selected(self.character_index.get())