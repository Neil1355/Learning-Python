import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

lb1 = tk.Listbox(frame_a)
lb1.insert(1, "Gujarat")
lb1.insert(2, "Maharashtra")
lb1.insert(3, "Himachal Pradesh")
lb1.pack()

CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
C1 = tk.Checkbutton(frame_a, text="Music", variable=CheckVar1, onvalue=1, offvalue=0)
C2 = tk.Checkbutton(frame_a, text="Video", variable=CheckVar2, onvalue=1, offvalue=0)
C1.pack()
C2.pack()

frame_b = tk.Frame()
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

var = tk.IntVar()
R1 = tk.Radiobutton(frame_b, text="Option 1", variable=var, value=1)
R2 = tk.Radiobutton(frame_b, text="Option 2", variable=var, value=2)
R3 = tk.Radiobutton(frame_b, text="Option 3", variable=var, value=3)
R1.pack()
R2.pack()
R3.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
