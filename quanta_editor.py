import tkinter,os,sys,time,random
from tkinter import *
from tkinter import font
from datetime import datetime
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

os.system("cls") #Windows -default

global selected
global linenumber
global open_status_name

open_status_name = False
linenumber = 0
selected = False

def uhrzeit():
    t = datetime.now()
    uhrzeit = "(%s_%sUhr)"%(t.hour,t.minute)
    return uhrzeit

def datum():
    t = datetime.now()
    datum = "%s.%s.%s"%(t.day,t.month,t.year)
    return datum

def x_datum():
    t = datetime.now()
    datum = "(%s-%s-%s)"%(t.day,t.month,t.year)
    return datum

def textfeld_width():
    return daten['fenster']['textfeld_element']['width']

def textfeld_height():
    return daten['fenster']['textfeld_element']['height']

def __tab_function(*args):
    position = Textfeld.index(INSERT)
    Textfeld.insert(position, "     ")

def speichern(*args):
    root.title("Datei wird gespeichert..")
    status = True
    try:
        root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Datei auswählen",filetypes = (("Python Dateien","*.py"),("Alle Dateitypen","*.*")))
    except Exception as FEHLER:
        print(FEHLER)
        status = False
    if (status != False):
        dateiname = root.filename
        name = dateiname
        __status_bar.config(text=f'{name}   Gespeichert')
        __inhalt_textfeld = Textfeld.get("1.0","end")
        root.title("Quanta>%s"%(dateiname))
        if (__inhalt_textfeld == ""):
            __inhalt_textfeld = " "
        try:
            file = open(dateiname,"w")
            file.write(__inhalt_textfeld)
            file.close()
        except Exception as F:
            if (dateiname == "" or dateiname == " "):
                pass
            else:
                print(" Fehler! => %s"%(F))

def __open_datei():
    status = True
    try:
        __dateiname__ = filedialog.askopenfilename(initialdir = "/",title = "Datei öffnen",filetypes = (("Python Dateien","*.py"),("Alle Dateitypen","*.tag")))
        global open_status_name
        open_status_name = __dateiname__
    except Exception as e:
        status = False
    if (status != False):
        try:
            datei = open(__dateiname__,"r")
            name = __dateiname__
            __status_bar.config(text=f'{name}   ')
            Textfeld.delete("1.0","end")
            root.title("Quanta>Datei geöffnet>%s"%(__dateiname__))
            content = datei.read()
            Textfeld.insert(END,"%s"%(content))
            datei.close()
        except Exception as F:
            if (__dateiname__ == "" or __dateiname__ == " "):
                pass
            else:
                print(" Fehler! => %s"%(F))


def neue_datei():
    Textfeld.delete("1.0","end")
    root.title("Quanta>Neue Datei>")
    global open_status_name
    open_status_name = False

#Text ausschneiden
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if Textfeld.selection_get():
            selected = Textfeld.selection_get()
            Textfeld.delete("sel.first", "sel.last")

#Text kopieren
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    if Textfeld.selection_get():
        selected = Textfeld.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

#Text einfügen
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = Textfeld.index(INSERT)
            Textfeld.insert(position, selected)

def jetzt():
    t = datetime.now()
    jetzt = "%s.%s.%s-%s:%s:%s Uhr"%(t.day,t.month,t.year,t.hour,t.minute,t.second)
    return jetzt

def __speichern__vorh(*args):
    global open_status_name
    if open_status_name:
        try:
            file = open(open_status_name, "w")
            file.write(Textfeld.get(1.0, END))
            file.close()
        except Exception as F:
            print(" Fehler! => %s"%(F))
        __status_bar.config(text=f'%s-Gespeichert: {open_status_name} '%(jetzt()))
    else:
        speichern()

def configure__(COLOR,__FONT,keyword):
    Textfeld.tag_config(keyword,font=__FONT,foreground = COLOR)

def text_changed(*args):
    global linenumber
    linenumber += 1
    #Textfeld.tag_remove('', '1.0', END)
    keywords = [
        "html",
        "/html",
        "head",
        "/head",
        "body",
        "/body",
        "import",
        "class",
        "if",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        "def",
        "__",
        "print",
        "dict",
        "=",
        ",",
        ":",
        "False",
        "True",
        "#",
        "from",
        "!",
        "%",
        "len",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "append",
        "clear",
        "remove",
        "delete",
        "try",
        "except",
        "cls",
        "clear",
        "datetime",
        "socket",
        "os",
        "time",
        "random",
        "cryptography",
        "*",
        "_",
        "pass",
        "else",
        "return",
        "while",
        "not in",
    ]
    for s in keywords:
        __FONT = "Consolas 24"
        if s:
            idx = '1.0'
            while 1:
                # searches for desried string from index 1
                idx = Textfeld.search(s, idx, nocase = 1,
                                stopindex = END)
                if not idx: break
                lastidx = '% s+% dc' % (idx, len(s))
                Textfeld.tag_add(s, idx, lastidx)
                idx = lastidx
                if (s == "html" or s == "/html" or s == "head" or s == "/head" or s == "body" or s == "/body"):
                    color = "orangered"
                if (s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8" or s == "9" or s == "0"):
                    color = "light salmon"
                if (s == "os" or s == "time" or s == "random" or s == "socket" or s == "datetime"):
                    color = "MediumPurple2"
                if (s == "cryptography"):
                    color = "PaleVioletRed3"
                    __FONT = "Courier 25 bold"
                if (s == "*"):
                    color = "lightgreen"
                if (s == "_" or s == "not in"):
                    color = "dark orange"
                if (s == "import" or s == "from"):
                    color = "cornflowerblue"
                    __FONT = "Consolas 25 bold"
                if (s == "class"):
                    color = "orange"
                    __FONT = "Consolas 24 italic"
                if (s == "try" or s == "except" or s == "pass" or s == "return" or s == "while"):
                    color = "HotPink2"
                    __FONT = "Consolas 24 bold"
                if (s == "append"):
                    color = "cornflowerblue"
                    __FONT = "Consolas 24 bold"
                if (s == "clear" or s == "cls"):
                    color = "powder blue"
                    __FONT = "Consolas 24 bold"
                if (s == "remove" or s == "delete"):
                    color = "DarkGoldenrod3"
                    __FONT = "Consolas 24 bold"
                if (s == "if" or s == "else"):
                    color = "deep pink"
                    __FONT = "Consolas 24 bold"
                if (s == "(" or s == ")"):
                    color = "white"
                    __FONT = "Courier 25 bold"
                if (s == "[" or s == "]"):
                    color = "snow"
                    __FONT = "Consolas 24"
                if (s == "{" or s == "}"):
                    color = "gold"
                if (s == "def"):
                    color = "DarkSlateGray2"
                    __FONT = "Consolas 24 italic"
                if (s == "__"):
                    color = "dark orange"
                if (s == "''" or s == "'"):
                    color = "yellow"
                if (s == '""' or s == '"'):
                    color = "DarkSeaGreen2"
                if (s == "print"):
                    color = "tomato"
                if (s == "dict"):
                    color = "cornflowerblue"
                    __FONT = "Consolas 24 italic"
                if (s == "=" or s == "%"):
                    color = "pink"
                if (s == "," or s == ";"):
                    color = "whitesmoke"
                    __FONT = "Consolas 24 bold"
                if (s == ":"):
                    color = "goldenrod"
                    __FONT = "Consolas 24 bold"
                if (s == "False" or s == "True"):
                    color = "blue violet"
                if (s == "#"):
                    color = "LemonChiffon4"
                if (s == "!"):
                    color = "DarkGoldenrod2"
                if (s == "len"):
                    color = "SkyBlue2"
                    __FONT = "Consolas 24 bold"
                configure__(color, __FONT, s)

daten = {
    'fenster':{
        'textfeld_element':{
            'width':82,
            'height':25.4,
            'hintergrundfarbe':"gray15",
        },
        'hintergrundfarbe':"white",
        'width':"1500",
        'height':"800",
        'standard_font_titel':"Helvetica 22 bold",
        'standard_font_text':"Helvetica 15 bold",
        'standard_bg':"white",
        'monospace_font':"Consolas 24",
        'nachrichten':{
            'Titel':"Quanta-Editor",
        },
    },
}


def __quotedbl_add(evt):
    Textfeld.insert(INSERT, '"')

def __quoteright_add(evt):
    Textfeld.insert(INSERT, "'")

def __parenleft_add(evt):
    Textfeld.insert(INSERT, ")")

def key_press(evt):
    print(evt)

standard_font_titel = daten['fenster']['standard_font_titel']
standard_font_text = daten['fenster']['standard_font_text']
standard_bg = daten['fenster']['hintergrundfarbe']
monospace_font = daten['fenster']['monospace_font']
textfeld_bg = daten['fenster']['textfeld_element']['hintergrundfarbe']

root = tkinter.Tk()
root.title(daten['fenster']['nachrichten']['Titel'])
root.configure(bg=daten['fenster']['hintergrundfarbe'])
root.minsize(daten['fenster']['width'],daten['fenster']['height'])
root.maxsize(daten['fenster']['width'],daten['fenster']['height'])

Textfeld = tkinter.Text(root)
Textfeld.configure(bg=textfeld_bg,font=monospace_font,fg="whitesmoke")
Textfeld.configure(width=textfeld_width(),height=textfeld_height())
Textfeld.configure(insertbackground="whitesmoke",padx=5,pady=5)
__Scrollbar = tkinter.Scrollbar(root, command=Textfeld.yview)
ss_x = tkinter.Scrollbar(root, orient='horizontal', command=Textfeld.xview)
Textfeld.configure(yscrollcommand=__Scrollbar.set)
Textfeld.configure(xscrollcommand=ss_x.set)
__Scrollbar.pack(side=RIGHT, fill=Y)
ss_x.pack(side=BOTTOM, fill=X)
Textfeld.place(x=0,y=1)
ss_x.config(command=Textfeld.xview)

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar,tearoff=False)
filemenu.add_command(label="Neue Datei",command=neue_datei)
filemenu.add_command(label="Öffnen",command=__open_datei)
filemenu.add_command(label="Ausschneiden        (Ctrl+x)",command=lambda:cut_text(False))
filemenu.add_command(label="Kopieren        (Ctrl+c)",command=lambda:copy_text(False))
filemenu.add_command(label="Einfügen        (Ctrl+v)",command=lambda:paste_text(False))
filemenu.add_command(label="Speichern als        (Ctrl+s)", command=speichern)
filemenu.add_command(label="Speichern        (Ctrl+s)", command=__speichern__vorh)
filemenu.add_command(label="Beenden",command=root.quit)
menubar.add_cascade(label="Optionen", menu=filemenu)
root.config(menu=menubar)

__status_bar = tkinter.Label(root,text="Ready", anchor=E)
__status_bar.configure(bg="cornflowerblue", fg="white", font="Consolas 12 bold")
__status_bar.pack(fill=X,side=BOTTOM, ipady=2)

toolbar_frame = tkinter.Frame(root)
toolbar_frame.pack()

root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-s>', __speichern__vorh)
root.bind('<Control-Key-f>', __tab_function)
root.bind('<quotedbl>', __quotedbl_add)
root.bind('<quoteright>', __quoteright_add)
root.bind('<parenleft>', __parenleft_add)
#root.bind('<Key>', key_press)
Textfeld.bind('<KeyRelease>', text_changed)



root.mainloop()
