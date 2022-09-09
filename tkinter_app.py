import tkinter as tk
from tkinter import *
from tkinter import ttk
import re
from PIL import ImageTk, Image


LARGEFONT = ("Verdana", 10)
data = []
users = []
groups = []
user = ""
counter = 0


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}
        files = open("part2\\social_network.txt", "r")
        lines = files.readlines()
        line1 = []
        global data
        for line in lines:
            a = re.split("<|>|,|:|\n|#| ", line)
            y = []
            for x in a:
                if x != "":
                    y.append(x)
            line1.append(y)
        data = line1
        files.close()

        for x in line1:
            a = x[0]
            if a != "users":
                if a == "groups":
                    break
                else:
                    users.append(a)
        global user
        user = users[0]
        for ui in users:
            filename = "part2\\" + str(ui) + ".txt"
            f = open(filename, "a+")
            f.close()

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2,  Page4, Page5):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        global counter
        frame = self.frames[cont]
        d = counter + 1
        counter = d
        frame.tkraise()


# first window frame startpage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')
        # parent.geometry("1000*1000")

        # label of frame Layout 2
        label = ttk.Label(self, text="Chose the user:", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, padx=0, pady=10)

        button1 = ttk.Button(
            self, text="Contact List", command=lambda: controller.show_frame(Page1),
        )
        usr = StringVar(self)
        usr.set(users[0])
        popupMenu = OptionMenu(self, usr, *users)
        popupMenu.grid(row=0, column=1, padx=10, pady=10)

        def choose_users(*args):
            global user
            user = usr.get()
            # print(str(user))

        usr.trace("w", choose_users)

        # putting the button in its place by
        # using grid
        button1.grid(row=0, column=1, padx=20, pady=10)
        exitbutton = ttk.Button(self, text="Exit", command=exit )
        exitbutton.grid(row=0, column=18,padx=20, pady=10)
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(
            self,
            text="Click to get the groups whish user is a member of",
            command=lambda: controller.show_frame(Page2),
        )

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=5, padx=20, pady=10)
        button3 = ttk.Button(
            self, text="Messages", command=lambda: controller.show_frame(Page5)
        )

        # putting the button in its place by
        # using grid
        button3.grid(row=0, column=9, padx=20, pady=10)
        button4 = ttk.Button(
            self, text="Post Messages", command=lambda: controller.show_frame(Page4)
        )

        # putting the button in its place by
        # using grid
        button4.grid(row=0, column=13, padx=20, pady=10)


# second window frame page1
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        l_counter = 0
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')

        self.label = ttk.Label(self, text="Existing contacts:", font=LARGEFONT)
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.label1 = ttk.Label(self, text="", font=LARGEFONT)
        self.label1.grid(row=1, column=0, padx=10, pady=10)
        self.label1.configure(background='light blue')
        self.label1.after(2000, self.pcontacts)
        exitbutton = ttk.Button(self, text="Exit", command=exit )
        exitbutton.grid(row=0, column=18,padx=20, pady=10)
        button1 = ttk.Button(
            self,
            text="Select the user",
            command=lambda: controller.show_frame(StartPage),
        )
        button1.grid(row=0, column=10, padx=10, pady=10)
        button2 = ttk.Button(
            self,
            text="Click to get the groups whish user is a member of",
            command=lambda: controller.show_frame(Page2),
        )
        button2.grid(row=0, column=11, padx=10, pady=10)
        button3 = ttk.Button(
            self, text="Messages", command=lambda: controller.show_frame(Page5)
        )

        # putting the button in its place by
        # using grid
        button3.grid(row=0, column=12, padx=10, pady=10)

        button4 = ttk.Button(
            self, text="Post Messages", command=lambda: controller.show_frame(Page4)
        )

        # putting the button in its place by
        # using grid
        button4.grid(row=0, column=13, padx=10, pady=10)

    def pcontacts(self):
        self.la = ttk.Label(self, text="Current User:" + str(user), font=LARGEFONT)
        self.la.grid(row=10, column=0, padx=10, pady=10, sticky="sw")
        self.la.configure(background='light blue')
        # self.label1.configure(background='light blue')
        contacts = []
        lists = " "
        for line in data:
            if line[0] == "groups":
                break
            if line[0] == user:
                for word in line:
                    if word != user:
                        contacts.append(word)
        usrt = StringVar(self)
        for i in contacts:
            lists = lists + "   " + str(i)
        usrt.set(lists)
        self.label1.configure(text=lists)
        self.label1.after(1000, self.pcontacts)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')

        self.label = ttk.Label(
            self, text="Groups the user is member of:", font=LARGEFONT
        )
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.label1 = ttk.Label(self, text="", font=LARGEFONT)
        self.label1.grid(row=1, column=0, padx=10, pady=10)
        self.label1.after(2000, self.pgroups)
        self.label1.configure(background='light blue')
        exitbutton = ttk.Button(self, text="Exit", command=exit )
        exitbutton.grid(row=0, column=18,padx=20, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="Contact List", command=lambda: controller.show_frame(Page1)
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=0, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(
            self,
            text="Select the user",
            command=lambda: controller.show_frame(StartPage),
        )

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=5, padx=10, pady=10)
        button3 = ttk.Button(
            self, text="Messages", command=lambda: controller.show_frame(Page5)
        )

        # putting the button in its place by
        # using grid
        button3.grid(row=0, column=9, padx=10, pady=10)

        button4 = ttk.Button(
            self, text="Post Messages", command=lambda: controller.show_frame(Page4)
        )

        # putting the button in its place by
        # using grid
        button4.grid(row=0, column=13, padx=10, pady=10)

    def pgroups(self):
        self.la = ttk.Label(self, text="Current User:" + str(user), font=LARGEFONT)
        self.la.grid(row=10, column=0, padx=10, pady=10, sticky="sw")
        self.la.configure(background='light blue')
        flag = 0
        sd = 0
        groupss = []
        lists = " "
        for line in data:
            sd = 0
            if line[0] == "groups":
                flag = 1
            if flag != 1:
                continue
            grp_name = line[0]
            groups.append(grp_name)
            for i in line:
                if i == user:
                    sd = 1
            if sd == 1:
                groupss.append(grp_name)

        for i in groupss:
            lists = lists + "   " + str(i)

        self.label1.configure(text=lists)
        self.label1.after(1000, self.pgroups)


poi = 2
n = -1


class Page3(tk.Frame):
    def clean(self):
        for widget in self.winfo_children():
            a = str(widget)
            if (
                a != ".!frame.!page3.!label"
                and a != ".!frame.!page3.!label2"
                and a != ".!frame.!page3.!button"
                and a != ".!frame.!page3.!button2"
                and a != ".!frame.!page3.!button3"
            ):
                if self.currentuser != user:
                    widget["text"] = ""
                    global poi
                    poi = 2
                    self.currentuser = user

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')

        self.label = ttk.Label(self, text="Messages:", font=LARGEFONT)
        self.label.grid(row=0, column=0, padx=0, pady=10)
        self.label1 = ttk.Label(self, text="", font=LARGEFONT)
        self.label1.grid(row=1, column=0, padx=10, pady=10)
        self.label1.after(2000, self.pm1)
        self.postedi = []
        self.postedm = []
        self.currentuser = user

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="Contact List", command=lambda: controller.show_frame(Page1)
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=0, column=8, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(
            self,
            text="Select the user",
            command=lambda: controller.show_frame(StartPage),
        )

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=14, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="Click to get the groups whish user is a member of",
            command=lambda: controller.show_frame(Page2),
        )

        # putting the button in its place by
        # using grid

        button3.grid(row=0, column=20, padx=10, pady=10)
        button4 = ttk.Button(
            self, text="Post Messages", command=lambda: controller.show_frame(Page4)
        )

        # putting the button in its place by
        # using grid
        button4.grid(row=0, column=25, padx=10, pady=10)

        # scroll=ttk.Scrollbar(self,orient=VERTICAL)
        # scroll.grid(row=100,column=100,sticky=NSEW)

    # img=[]
    # labe=[]
    def pm1(self):
        self.la = ttk.Label(self, text="Current User:" + str(user), font=LARGEFONT)
        self.la.grid(row=10, column=0, padx=10, pady=10, sticky="sw")
        global poi
        self.clean()
        if self.currentuser != user:
            self.clean()
            self.currentuser = user
            # global poi
            poi = 2
        # self.some_frame = tk.Frame(self.parent)

        # global poi
        poi = poi + 1
        lists = ""
        filepath = "part2\\" + str(user) + ".txt"
        f = open(filepath, "r")
        lines = f.readlines()
        for line in lines:
            poi = poi + 1
            line = line.rstrip()
            if " " not in line:
                if line[-4:] == ".png" or line[-4:] == ".jpg" or line[-5:] == ".jpeg":
                    filepath = "part2\\" + str(line)
                    if filepath not in self.postedi:
                        if Image.open(filepath):
                            load = Image.open(filepath)
                            render = ImageTk.PhotoImage(load)
                            img = Label(self, image=render)
                            img.image = render
                            img.grid(row=poi, column=1, padx=10, pady=20)
                            self.postedi.append(filepath)
                        else:
                            continue
            if " " not in line or " " in line:
                if (
                    line not in self.postedm
                    and line not in self.postedi
                    and line[-4:] != ".png"
                    and line[-4:] != ".jpg"
                    and line[-5:] != ".jpeg"
                ):
                    self.labe = ttk.Label(self, text=str(line), font=LARGEFONT)
                    self.labe.grid(row=poi, column=1, padx=10, pady=0)
                    self.postedm.append(line)

        self.label1.configure(text="")
        self.label1.after(1000, self.pm1)


class Page4(tk.Frame):
    def submit_i(self):
        self.image = self.entry_i.get()
        self.i = 1
        self.m = 0
        self.pm()

    def submit_m(self):
        self.message = self.entry_m.get()
        self.i = 0
        self.m = 1
        self.pm()

    def submit_u(self):
        self.usg = self.entry_u.get()
        self.m = 0
        self.i = 0
        # self.pm()

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')

        self.label = ttk.Label(self, text="Post Messages:", font=LARGEFONT)
        self.label.grid(row=0, column=0, padx=10, pady=10)
        # self.label1 = ttk.Label(self, text="", font=LARGEFONT)
        # self.label1.grid(row=1, column=0, padx=10, pady=10)
        exitbutton = ttk.Button(self, text="Exit", command=exit )
        exitbutton.grid(row=0, column=18,padx=20, pady=10)
        # self.label1.after(1000, self.pm)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="Contact List", command=lambda: controller.show_frame(Page1)
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=0, column=5, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(
            self,
            text="Select the user",
            command=lambda: controller.show_frame(StartPage),
        )

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=6, padx=10, pady=10)

        button3 = ttk.Button(
            self,
            text="Click to get the groups whish user is a member of",
            command=lambda: controller.show_frame(Page2),
        )

        # putting the button in its place by
        # using grid
        button3.grid(row=0, column=7, padx=10, pady=10)

        button4 = ttk.Button(
            self,
            text="Get Messages",
            command=lambda: controller.show_frame(Page5),
        )

        # putting the button in its place by
        # using grid
        button4.grid(row=0, column=8, padx=10, pady=10)
        # Entry
        self.entry_i = Entry(self)
        self.entry_u = Entry(self)
        self.entry_m = Entry(self)
        # Label
        self.label_u = ttk.Label(
            self, text="Enter id to send(user or group):", font=LARGEFONT
        )
        self.label_m = ttk.Label(self, text="Messages:", font=LARGEFONT)
        self.label_i = ttk.Label(
            self,
            text="Images( Enter name of image file with proper ext):",
            font=LARGEFONT,
        )
        # Label
        self.label_u.grid(row=2, column=0, padx=0, pady=10)
        self.label_m.grid(row=3, column=0, padx=0, pady=10)
        self.label_i.grid(row=4, column=0, padx=0, pady=10)
        # Entry
        self.entry_u.grid(row=2, column=1, padx=10, pady=10)
        self.entry_m.grid(row=3, column=1, padx=10, pady=10)
        self.entry_i.grid(row=4, column=1, padx=10, pady=10)
        # Buttons
        self.but_u = Button(self, text="Submit", command=self.submit_u)
        self.but_u.grid(row=2, column=2, padx=10, pady=10)
        self.but_m = Button(self, text="Submit", command=self.submit_m)
        self.but_m.grid(row=3, column=2, padx=10, pady=10)
        self.but_i = Button(self, text="Submit", command=self.submit_i)
        self.but_i.grid(row=4, column=2, padx=10, pady=10)

        self.messages = []
        self.images = []
        self.usg = ""
        self.message = ""
        self.image = ""
        self.m = 0
        self.i = 0

    def pm(self):
        self.la = ttk.Label(self, text="Current User:" + str(user), font=LARGEFONT)
        self.la.grid(row=10, column=0, padx=10, pady=10, sticky="sw")
        self.la.configure(background='light blue')
        # filepath="part2\\"+str(user)+".txt"
        # entry_m=ttk.Entry(self)
        # entry_i=ttk.Entry(self)
        u = 0
        g = 0
        if self.usg in users:
            u = 1
        if self.usg in groups:
            g = 1

        if u == 1:
            filepath = "part2\\" + str(self.usg) + ".txt"
            try:
                f = open(filepath, "a+")
            except:
                print("wrong user")
            if self.m == 1:
                f.write("\n")
                f.write(str(self.message))
                self.messages.append(self.message)
            if self.i == 1:
                f.write("\n")
                f.write(str(self.image))
                self.images.append(self.image)
            f.close()

        if g == 1:
            for line in data:
                if line[0] == self.usg:
                    for usr in line:
                        if usr != self.usg:
                            filepath = "part2\\" + str(usr) + ".txt"
                            try:
                                f = open(filepath, "a+")
                            except:
                                print("wrong user")
                            if self.m == 1:
                                f.write("\n")
                                f.write(str(self.message))
                                self.messages.append(self.message)
                            if self.i == 1:
                                f.write("\n")
                                f.write(str(self.image))
                                self.images.append(self.image)
                            f.close()

        if u == 0 and g == 0:
            print("wrong user and group")

        # self.label1.configure(text="")
        # self.label1.after(1000, self.pm)


class Page5(tk.Frame):
    def delete(self):
        self.lst.delete(0, tk.END)
        self.messages = []

    def pop_window(self, event):
        data = self.lst.get(self.lst.curselection()[0])
        top = tk.Toplevel(self)
        tk.Label(top, text="Message : \n"+str(data)).grid(
            row=0, column=1, padx=10, pady=10
        )
        a = str(data)
        if a[-4:] == ".jpg" or a[-4:] == ".png" or a[-5:] == ".jpeg":
            impath = "part2\\" + a
            load = Image.open(impath)
            render = ImageTk.PhotoImage(load)
            img = Label(top, image=render)
            img.image = render
            img.grid(row=1, column=1, padx=10, pady=10)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='light blue')

        exitbutton = ttk.Button(self, text="Exit", command=exit )
        exitbutton.grid(row=0, column=18,padx=20, pady=10)

        self.currenuser = user

        self.label = ttk.Label(
            self,
            text="Messages(Double click on message heading to see the entire message):",
            font=LARGEFONT,
        )
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.label1 = ttk.Label(self, font=LARGEFONT)
        self.label1.grid(row=1, column=0, padx=10, pady=10)
        self.label1.configure(background='light blue')
        self.label1.after(1000, self.mes)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(
            self, text="Contact List", command=lambda: controller.show_frame(Page1)
        )

        # putting the button in its place by
        # using grid
        button1.grid(row=0, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(
            self,
            text="Select the user",
            command=lambda: controller.show_frame(StartPage),
        )

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=5, padx=10, pady=10)
        button3 = ttk.Button(
            self,
            text="Groups the user has joined",
            command=lambda: controller.show_frame(Page2),
        )

        # putting the button in its place by
        # using grid
        button3.grid(row=0, column=9, padx=10, pady=10)

        button4 = ttk.Button(
            self, text="Post Messages", command=lambda: controller.show_frame(Page4)
        )

        # putting the button in its place by
        # using grid
        button4.grid(row=0, column=13, padx=10, pady=10)
        self.messages = []
        self.lv = tk.Variable()
        self.lst = tk.Listbox(self, listvariable=self.lv)
        self.lst.bind("<Double-Button-1>", self.pop_window)
        self.lst.grid(row=2, column=1, padx=10, pady=10)
        self.lines = []

    def mes(self):
        self.la = ttk.Label(self, text="Current User:" + str(user), font=LARGEFONT)
        self.la.grid(row=10, column=0, padx=10, pady=10, sticky="sw")
        self.la.configure(background='light blue')
        # print(self.currenuser)
        # print(user)
        if self.currenuser != user:
            self.delete()
            self.currenuser = user
        self.filepath = "part2\\" + str(user) + ".txt"
        with open(self.filepath, "r+") as fo:
            self.lines = fo.readlines()
        # fi=open(filepath)
        # self.lines=fi.getlines()
        for line in self.lines:
            if line not in self.messages:
                self.lst.insert(tk.END, line.strip())
                self.lst.insert(tk.END, "\n")

                self.messages.append(line)

        # self.label1.configure(text="")
        self.label1.after(1000, self.mes)

        self.filepth="part2\\messages.txt" 
        with open(self.filepth, "w+") as fo:
            for line in self.messages:
                fo.write(str(line))


# Driver Code
app = tkinterApp()
app.mainloop()
