from tkinter import *

class App(Frame):
    def __init__(self, master):         
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
   
    def create_widgets(self):        
        Label(self, text="Enter information for a new MadLibsStory").grid(row=0, column=0, columnspan=1, sticky=W)
        Label(self, text="Person: ").grid(row=1, column=0, sticky=W)
        self.person_ent=Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)
        Label(self, text="Plural Noun: ").grid(row=2, column=0, sticky=W)
        self.noun_ent=Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)
        Label(self, text="Verb: ").grid(row=3, column=0, sticky=W)
        self.verb_ent=Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)
        Label(self, text="Adjective(s): ").grid(row=4, column=0, sticky=W)
        self.is_itchy=BooleanVar()
        Checkbutton(self, text="Itchy",
                    variable=self.is_itchy).grid(row=4, column=1, sticky=W)
        self.is_joyous=BooleanVar()
        Checkbutton(self, text="Joyous",
                    variable=self.is_joyous).grid(row=4, column=2, sticky=W)
        self.is_electric=BooleanVar()
        Checkbutton(self, text="Electric",
                    variable=self.is_electric).grid(row=4, column=3, sticky=W)
     
        Label(self, text="Body Part:").grid(row=10, column=1, sticky=W)
        self.body_part=StringVar()
        B=["Belly button", "Big toe", "Medulla oblongata"]
        self.listofbodyparts=Listbox(width=20, height=5, listvariable=self.body_part)
        self.listofbodyparts.grid(row=4)
        self.body_part.set(tuple(B))
        Button(self, text="Click for MadLibsStory",
               command=self.tell_MadLibsStory).grid(row=5, column=0, sticky=W)
        self.MadLibsStory_txt=Text(self, width=30, height=10,wrap=WORD)
        self.MadLibsStory_txt.grid(row=7, column=0, columnspan=4)

    def tell_MadLibsStory(self):         
        person=self.person_ent.get()
        noun=self.noun_ent.get()
        verb=self.verb_ent.get()
        adjective=""
        if self.is_itchy.get():
            adjective+="Itchy, "
        if self.is_joyous.get():
            adjective+="Joyous, "
        if self.is_electric.get():
            adjective+="Electric, "
        bodypart=self.listofbodyparts.get(self.listofbodyparts.curselection())
     
        MadLibsStory="The famous explorer "
        MadLibsStory+=person
        MadLibsStory+=" had nearly given up a life-long quest to find The Lost City of "
        MadLibsStory+=noun.title()
        MadLibsStory+=" when one day, the "
        MadLibsStory+=noun
        MadLibsStory+=" found "
        MadLibsStory+=person+". "
        MadLibsStory+="A strong, "
        MadLibsStory+=adjective
        MadLibsStory+=" peculiar feeling overwhelmed the explorer. "
        MadLibsStory+="After all this time, the quest was finally over. A tear came to "
        MadLibsStory+=person+"'s "
        MadLibsStory+=bodypart.lower()+". "
        MadLibsStory+="And then, the "
        MadLibsStory+=noun
        MadLibsStory+= " promptly devoured "
        MadLibsStory+=person.upper()+". "
        MadLibsStory+="The moral of the MadLibsStory? Be careful what you "
        MadLibsStory+=verb
        MadLibsStory+=" for."
        self.MadLibsStory_txt.delete(0.0, END)
        self.MadLibsStory_txt.insert(0.0, MadLibsStory)

window=Tk()
window.title("Mad Libs")
app=App(window)
window.mainloop()




