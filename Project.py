from tkinter import *
from tkinter import filedialog
import csv
import os
from csv import writer
from styles import *


root = Tk()
# Main window
root.configure(bg=a)
# Main window Title
root.title("Fake News Detection")
# Main window dimensions
root.geometry("400x200")
filename = ""
root.state('zoomed')


# Working of Click Me button on main window
def click():
    # Clear frame from main
    for widgets in frame.winfo_children():
        widgets.destroy()
    root.configure(bg='SystemButtonFace')
    frame.configure(bg='SystemButtonFace', fg='black')
    # r variable for tracking radio buttons
    r = IntVar()

    # Working of click button on second window
    def clicked(value):
        # 1 for single news; 2 for database news
        if value == 1:
            nw2 = Toplevel(root)
            nw2.title("Fake News Detection")
            nw2.geometry("400x200")
            nw2.state('zoomed')

            # noinspection PyTypeChecker
            def single_news():

                # Converting string received into 2D-array
                s1 = e2.get()
                s2 = e3.get()
                s3 = e4.get()
                arr = [[1, s1, s2, s3]]
                with open('newtest.csv', 'a') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(arr)
                # noinspection PyTypeChecker

                # Importing the final answer after uploading and testing dataset
                from FND_backend import X_test_prediction as Pred_list
                for i in nw2.winfo_children():
                    i.destroy()
                if Pred_list[-1] == 0:
                    l4 = Label(nw2, text="News is real",
                               width=100, height=4,
                               font=('Times New Roman', 25, "bold italic"),
                               fg='red')
                    l4.pack(pady=200, padx=10, anchor=CENTER)
                else:
                    l4 = Label(nw2, text="News is fake",
                               width=100, height=4,
                               font=('Times New Roman', 25, "bold italic"),
                               fg='red',
                               )
                    l4.pack(pady=200, padx=10, anchor=CENTER)

            l7 = Label(nw2,
                       text="Enter the news data",
                       width=100, height=4,
                       font=('Times New Roman', 30, "bold italic"),
                       fg="black")
            l7.pack()
            # Title label and entry widget
            l_title = Label(nw2,
                            text="Enter the news title",
                            width=100, height=4,
                            font=('TkDefaultFont', 10, 'bold'),
                            fg="black")
            l_title.pack()
            e2 = Entry(nw2, width=50)
            e2.pack()
            l_author = Label(nw2,
                             text="Enter the news author",
                             width=100, height=4,
                             font=('TkDefaultFont', 10, 'bold'),
                             fg="black")
            l_author.pack()
            e3 = Entry(nw2, width=50)
            e3.pack()
            l_news = Label(nw2,
                           text="Enter the news ",
                           width=100, height=4,
                           font=('TkDefaultFont', 10, 'bold'),
                           fg="black")
            l_news.pack()
            e4 = Entry(nw2, width=50)
            e4.pack()

            b3 = Button(nw2, text="Enter", command=single_news)
            b3.pack()

            pass
        if value == 2:
            nw2 = Toplevel(root)
            # nw2.attributes('-fullscreen', True)
            nw2.title("Fake News Detection")
            nw2.geometry("400x200")
            nw2.state('zoomed')

            def file_browse():
                global filename
                filename = filedialog.askopenfilename(initialdir="/Desktop",
                                                      title="Select a File",
                                                      filetypes=(("CSV Files", "*.csv"),
                                                                 ("all files",
                                                                  "*.*")))
                label_file_explorer.configure(text="File Opened: "+filename, fg='blue',
                                              font=('TkDefaultFont', 10, "normal"),)
                pass

            def upload():

                def click2():
                    serial_number = int(e1.get())
                    print(serial_number)
                    for j in frame1.winfo_children():
                        j.destroy()
                    if Pred_list[serial_number-1] == 0:
                        l4 = Label(frame1, text="News is real",
                                   width=100, height=4,
                                   font=('Times New Roman', 25, "bold italic"),
                                   fg='red')
                        l4.pack()
                    else:
                        l4 = Label(frame1, text="News is fake",
                                   width=100, height=4,
                                   font=('Times New Roman', 25, "bold italic"),
                                   fg='red'
                                   )
                        l4.pack()

                data = []
                with open(os.path.join(os.path.dirname(__file__), filename), 'r', encoding="utf-8") as f:
                    f_csv = csv.reader(f)
                    for row in f_csv:
                        data.append(row)
                with open('newtest.csv', 'w+', encoding="utf-8") as f:
                    writer2 = csv.writer(f)
                    for i in range(int(len(data) * 30 / 100)):
                        writer2.writerow(data[i])
                # Importing the final answer after uploading and testing dataset
                from FND_backend import X_test_prediction as Pred_list
                for i in frame1.winfo_children():
                    i.destroy()
                l3 = Label(frame1, text="Enter the serial number of news to be checked from database.",
                           width=100, height=4, fg="black")
                l3.pack()
                e1 = Entry(frame1, width=10)
                e1.pack()
                b5 = Button(frame1, text="Click to Continue",
                            padx=0, pady=0,
                            command=click2)
                b5.pack()

            frame1 = LabelFrame(nw2, padx=150, pady=10)
            frame1.pack(padx=150, pady=250, anchor=CENTER)

            label_file_explorer = Label(frame1,
                                        text="Choose database to upload",
                                        width=100, height=4,
                                        font=('Times New Roman', 15, "bold italic"),
                                        fg="black")
            label_file_explorer.pack()
            b3 = Button(frame1, text="Browse database", command=file_browse)
            b3.pack()
            b4 = Button(frame1, text="Upload database", command=upload)
            b4.pack()
            pass

    # New window label 1
    l2 = Label(frame, text="Choose type of news you want to check",
               font=('Times New Roman', 15, "bold italic"),)
    l2.pack(pady=5)
    # New window radio button 1
    r1 = Radiobutton(frame, text="Single News",
                     variable=r, value=1)
    r1.pack()
    # New window radio button 2
    r2 = Radiobutton(frame, text="News Database",
                     variable=r, value=2)
    r2.pack()
    # New window click me button
    b2 = Button(frame, text="Click to continue",
                command=lambda: clicked(r.get()), height=10)
    b2.pack()


# Main window frame
frame = LabelFrame(root, padx=100, pady=100, bg=a)
frame.pack(padx=10, pady=200, anchor=CENTER)
# Main window first label
l1 = Label(frame, text="Fake News Detection",
           font=('Times New Roman', 25, "bold italic"),
           bg=a, fg=b)
l1.grid(row=0, column=1, pady=20)
# Main window button
b1 = Button(frame, text="Click to Continue",
            padx=0, pady=0,
            command=click,
            font=('Comic Sans MS', 10, "bold italic"), bg=a, fg=b)
b1.grid(row=2, column=1)

root.mainloop()
