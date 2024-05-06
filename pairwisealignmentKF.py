import re
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from Bio import Align
from tkinter.messagebox import *

class PairwiseAlign:

    def __init__(self,master):
        self.master=master
        #title bar
        master.title("Pairwise Sequence Alignment by Kalungi")
        #make the window not resizable
        master.resizable(False,False)
        #first label for sequence one
        self.label1=Label(master,text="Enter sequence one")
        self.label1.grid(row=0,column=0)
        #scrolled text box for sequence one 
        self.text1=ScrolledText(master,font=('Verdana', 16), height=6, width=40)
        self.text1.grid(row=0,column=1)
        #second label for sequence two
        self.label2=Label(master, text="Enter Sequence two")
        self.label2.grid(row=1,column=0)
        #scrolled textbox for sequence two
        self.text2=ScrolledText(master,font=('Verdana', 16), height=6, width=40)
        self.text2.grid(row=1,column=1)
        #button for align
        self.button1=Button(master,text="Align",command=self.pairwisealign)
        self.button1.grid(row=2,column=0, columnspan="2")
        #label for results
        self.results1=Label(master,text="Results")
        self.results1.grid(row=3,column=0)
        #scrolled textbox for results
        self.results2=ScrolledText(master,font=('Verdana', 16), height=6, width=40)
        self.results2.grid(row=3,column=1)
            
        
    def pairwisealign(self):
        seq1=self.text1.get(1.0,END)
        seq2=self.text2.get(1.0,END)
        # checks for valid DNA sequences
        assert self.validate_dna(seq1,seq2)
        # initiates the Pairwise Aligner method
        aligner=Align.PairwiseAligner()
        alignments=aligner.align(seq1,seq2)
        # changes the text in the results label to alignment score
        self.results1.configure(text=f"Score: {alignments.score}\n\n")
        # writes the alignment in the text box
        for alignment in alignments:
            self.results2.insert(END,alignment.format("fasta"))
        #displays a congragulations message
        showinfo(title="Congragulations",message="Your alignment is finished")

    

    def validate_dna(self, seq1, seq2):
        # Convert sequences to uppercase
        seq1 = seq1.upper()
        seq2 = seq2.upper()

        # Check if sequences contain only DNA characters (A, G, T, C)
        if re.match("^[AGTC]+$", seq1) and re.match("^[AGTC]+$", seq2):
            print("Sequences are valid DNA sequences.")
            return True
        else:
            print("Sequences contain non-DNA characters or are empty.")
            return False

if __name__=="__main__":
    root=Tk()
    app=PairwiseAlign(root)
    root.mainloop()
    



