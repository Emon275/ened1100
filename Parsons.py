####################################################################
# Python Parsons Problem Program
# Dr. Greg Bucks
# Created: 8/4/2021
# Last Update: 10/26/2023
####################################################################
####################################################################
# import libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import *
import random
import os
import sys
import subprocess
####################################################################
####################################################################
# Button Functions
# Load code
def Btn5_click(*args):
  # clear out anything already in listboxes
  Lb1.delete(0,'end')
  Lb2.delete(0,'end')
  # ask user for file and read in contents
  File = filedialog.askopenfile(mode = "r")
  Lines = File.readlines()
  File.close()
  Lines[len(Lines)-1] = Lines[len(Lines)-1] + "\n"
  # randomly enter lines from file into listbox
  for x in range(len(Lines)):
    L = random.randint(0,len(Lines)-1)
    Lb1.insert(tk.END,Lines[L])
    del Lines[L]

# Move to code
def Btn1_click(*args):
  # check if a line is selected
  if len(Lb1.curselection())!=0:
    # if a line is selected, copy it over
    Ind = Lb1.curselection()
    Text = Lb1.get(Ind)
    Lb1.delete(Ind)
    Lb2.insert(tk.END,Text)

# Move to code options
def Btn8_click(*args):
  # check if a line is selected
  if len(Lb2.curselection())!=0:
    # if a line is selected, copy it over
    Ind = Lb2.curselection()
    Text = Lb2.get(Ind)
    Lb2.delete(Ind)
    Lb1.insert(tk.END,Text)

# Move line up
def Btn2_click(*args):
  # check if a line is selected
  if len(Lb2.curselection())!=0:
    Ind = Lb2.curselection()
    Text = Lb2.get(Ind)
    # check if the selected line is not at the top of the list
    if Ind[0] > 0:
      # switch selected line with the one above
      Text2 = Lb2.get(Ind[0]-1)
      Lb2.delete(Ind[0])
      Lb2.delete(Ind[0]-1)
      Lb2.insert(Ind[0]-1,Text)
      Lb2.insert(Ind[0],Text2)
      Lb2.selection_set(Ind[0]-1)

# Move line down
def Btn3_click(*args):
  # check if a line is selected
  if len(Lb2.curselection())!=0:
    Ind = Lb2.curselection()
    Text = Lb2.get(Ind)
    Last = Lb2.size()
    # check if the selected line is not at the bottom of the list
    if Ind[0] < Last-1:
      # switch selected line with the one below
      Text2 = Lb2.get(Ind[0]+1)
      Lb2.delete(Ind[0])
      Lb2.delete(Ind[0])
      Lb2.insert(Ind[0],Text2)
      Lb2.insert(Ind[0]+1,Text)
      Lb2.selection_set(Ind[0]+1)

# Indent selected line
def Btn6_click(*args):
  # check if a line is selected
  if len(Lb2.curselection())!=0:
    # if line is selected, add 2 spaces to front of line
    Ind = Lb2.curselection()
    Text = Lb2.get(Ind)
    Lb2.delete(Ind[0])
    Lb2.insert(Ind[0],"  " + Text)
    Lb2.selection_set(Ind[0])

# Unindent selected line
def Btn7_click(*args):
  # check if a line is selected
  if len(Lb2.curselection())!=0:
    Ind = Lb2.curselection()
    Text = Lb2.get(Ind)
    # if line is selected, check if first two characters are spaces
    if Text[0] == " " and Text[1] == " ":
      # if first two characters are spaces, remove them
      Lb2.delete(Ind[0])
      Lb2.insert(Ind[0],Text[2:])
      Lb2.selection_set(Ind[0])

# Export code
def Btn11_click(*args):
  F = filedialog.asksaveasfile(initialfile = 'Python_TaskXpX_UCusername.py',defaultextension='.txt',filetypes=[('All Files','*.*'),('Python Files','*.py')])
  if F:
    File = open(F.name,"w")
    for L in range(Lb2.size()):
      File.write(Lb2.get(L))
    File.close()
  
# Import code
def Btn9_click(*args):
  # clear out current contents
  Lb2.delete(0,'end')
  # ask user for file and read in contents
  File = filedialog.askopenfile(mode = "r")
  Lines = File.readlines()
  File.close()
  Lines[len(Lines)-1] = Lines[len(Lines)-1] + "\n"
  # enter lines from file into listbox
  for x in range(len(Lines)):
    Lb2.insert(tk.END,Lines[x])

# Test code
def Btn4_click(*args):
  # write lines from listbox to file
  File = open("Code.py","w")
  for L in range(Lb2.size()):
    File.write(Lb2.get(L))
  File.write("input('Press any key to continue.')")
  File.close()
  # minimize window
  top.iconify()
  exec(open("Code.py").read())
  if os.path.exists("Code.py"):
    os.remove("Code.py")
  # restore window
  top.deiconify()

# Exit program
def Btn10_click(*args):
  top.destroy()

####################################################################
####################################################################
# Generate User Interface
top = tk.Tk()
top.title("Python Parsons Problems")
# Create fonts
HFont = font.Font(family="Times New Roman",size=14,weight="bold")
BFont = font.Font(family="Times New Roman",size=12,weight="bold")
CFont = font.Font(family="Courier New",size=10)
TFont = font.Font(family="Times New Roman",size=12)
# Add frames
TopFrame = tk.Frame(top,borderwidth = 2, relief = "ridge")
LeftFrame = tk.Frame(top,borderwidth = 2, relief = "ridge")
RightFrame = tk.Frame(top,borderwidth = 2, relief = "ridge")
TopFrame.grid(column = 0, row = 0, columnspan = 3)
LeftFrame.grid(column = 0, row = 1,rowspan = 2)
RightFrame.grid(column = 2, row = 1, rowspan = 2)
# Add button for moving code segments to completed code
Btn1 = tk.Button(top, text = "→",command = Btn1_click,font=HFont)
Btn1.config(font=BFont)
Btn1.grid(column = 1, row = 1)
# Add button for moving code segments back to options
Btn8 = tk.Button(top, text = "←",command = Btn8_click,font=HFont)
Btn8.config(font=BFont)
Btn8.grid(column = 1, row = 2)
####################################################################
# Top Frame children
# Add header label
InstrHead = tk.Label(TopFrame,text="Instructions:",font=HFont,justify=LEFT)
InstrHead.grid(column = 0, row = 0)
# Add Instructions
Instructions = "In a Parsons Problem, you are presented with all the code needed to solve a problem, but it is given to you in a random order.\n\
Your job is to place the lines of code in the correct order to solve the problem.  Note that there may be some lines of code\n\
that you do not use.  Follow the instructions below to use this program to solve the problem you have been given.\n\n\
1) Load in the code for the problem using the Load Code button\n\
2) Select the line you wish to add to your code and click the right arrow button\n\
3) If you wish to remove a line from your cide, select the line you wish to remove and click the left arrow button\n\
4) You can reorder the code in your Final Code window by selecting the line and clicking the Move Up or Move Down buttons\n\
5) You can indent or unindent lines in your Final Code window by selecting the line and clicking the Indent or Unindent buttons\n\
6) Once you think your code is ready, click the Test it out! button to run your code in the Python Shell window"
InstrText = tk.Label(TopFrame,text=Instructions,font=TFont,justify=LEFT)
InstrText.grid(column = 0, row = 1)
####################################################################
# Left Frame children
# Add label
Lbl1 = tk.Label(LeftFrame,text="Available Code",font=HFont)
Lbl1.grid(column = 0, row = 0)
# Add list box with code segments
Lb1 = tk.Listbox(LeftFrame,height = 20, width = 65)
Lb1.config(font=CFont)
Lb1.grid(column = 0, row = 1,columnspan = 2)
# Add button for loading code segments
Btn5 = tk.Button(LeftFrame, text = "Load Code",command = Btn5_click)
Btn5.config(font=BFont)
Btn5.grid(column = 1, row = 3)
# Add button to exit
Btn10 = tk.Button(LeftFrame, text = "Exit",command = Btn10_click,font=HFont)
Btn10.config(font=HFont)
Btn10.grid(column = 0, row = 3)
####################################################################
# Right Frame children
# Add label
Lbl2 = tk.Label(RightFrame,text="Final Code",font=HFont)
Lbl2.grid(column = 0, row = 0, columnspan = 9)
# Add list box for completed code
Lb2 = tk.Listbox(RightFrame,height = 20, width = 65)
Lb2.config(font=CFont)
Lb2.grid(column = 0, row = 1, columnspan = 9)
# Add button for moving code segments up
Btn2 = tk.Button(RightFrame, text = "Move Up",command = Btn2_click)
Btn2.config(font=BFont)
Btn2.grid(column = 0, row = 3)
# Add button for moving code segments down
Btn3 = tk.Button(RightFrame, text = "Move Down",command = Btn3_click)
Btn3.config(font=BFont)
Btn3.grid(column = 1, row = 3)
# Add label for spacing
#Lbl3 = tk.Label(RightFrame,text=" ",font=HFont)
#Lbl3.grid(column = 2, row = 3)
# Add button for indenting
Btn6 = tk.Button(RightFrame, text = "Indent",command = Btn6_click)
Btn6.config(font=BFont)
Btn6.grid(column = 2, row = 3)
# Add button for unindenting
Btn7 = tk.Button(RightFrame, text = "Unindent",command = Btn7_click)
Btn7.config(font=BFont)
Btn7.grid(column = 3, row = 3)
# Add label for spacing
Lbl4 = tk.Label(RightFrame,text=" ",font=HFont)
Lbl4.grid(column = 4, row = 3)
# Add button to export
Btn11 = tk.Button(RightFrame, text = "Export",command = Btn11_click)
Btn11.config(font=BFont)
Btn11.grid(column = 6, row = 3)
# Add button to import
Btn9 = tk.Button(RightFrame, text = "Import",command = Btn9_click)
Btn9.config(font=BFont)
Btn9.grid(column = 5, row = 3)
# Add label for spacing
Lbl5 = tk.Label(RightFrame,text=" ",font=HFont)
Lbl5.grid(column = 7, row = 3)
# Add button for testing code
Btn4 = tk.Button(RightFrame, text = "Test it out!",command = Btn4_click)
Btn4.config(font=BFont)
Btn4.grid(column = 8, row = 3)
####################################################################
# Run the GUI
top.mainloop()
