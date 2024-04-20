from tkinter import *
from tkinter.font import BOLD

BG = "#01010d"
FG = "#b8fffa"
PADX="14px"
PADY="2px"

bgWind = Tk()
bgWind.attributes('-fullscreen', True)
bgWind.config(bg=BG)

def newWind():
    window = Tk()
    window.title("Command Prompt")
    window.geometry("650x730+600+15")
    window.resizable(0,0)
    window.config(bg=BG)
    window.after(1, lambda: window.focus_force())
    menufrm = Frame(window, bg=FG, borderwidth="0")
    menufrm.pack(anchor="nw", fill=X)

    sbar = Scrollbar(window)
    sbar.pack(side="right",fill="y")

    bodyCanvas = Canvas(window, bg=BG, borderwidth="0", yscrollcommand=sbar.set)
    bodyCanvas.pack(side=TOP, fill=BOTH)

    sbar.config(command=bodyCanvas.yview)

    Label(menufrm, fg=BG, bg=FG, text="File", font=("Terminal",11, BOLD), padx=PADX, pady=PADY).pack(side=LEFT)
    Label(menufrm, fg=BG, bg=FG, text="Edit", font=("Terminal",11, BOLD), padx=PADX, pady=PADY).pack(side=LEFT)
    Label(menufrm, fg=BG, bg=FG, text="View", font=("Terminal",11, BOLD), padx=PADX, pady=PADY).pack(side=LEFT)
    Label(menufrm, fg=BG, bg=FG, text="Terminal", font=("Terminal",11, BOLD), padx=PADX, pady=PADY).pack(side=LEFT)
    Label(menufrm, fg=BG, bg=FG, text="Tabs", font=("Terminal",11, BOLD), padx=PADX, pady=PADY).pack(side=LEFT)
    Label(menufrm, fg=BG, bg=FG, text="Help", font=("Terminal",11, BOLD), padx=PADX, pady=PADY).pack(side=LEFT)

    def mostrar():
        def textRes():
            text = "Login incorrect"
            txtArr = [
                "login:backdoor",
                "No home directory specified in password file!",
                "Logging in with home=/"
            ]
            for i in txtArr:
                text = text + "\n" + i
            return text
        def handler(e):
            entr.config(state="disabled",disabledbackground=BG,disabledforeground=FG)
            resframe = Frame(bodyCanvas, bg=BG, borderwidth="0")
            resframe.pack(anchor="nw", fill=X)
            if entr.get() == "whoami":
                lbl = Label(resframe, fg=FG, bg=BG, text="kotaru", font=("Terminal",12))
                lbl.pack(side=LEFT)
                mostrar()
            elif entr.get() == "uname -a":
                lbl = Label(resframe, fg=FG, bg=BG, text="SolarOS 4.0.1 Generic_50203-02 sun4am i386\nUnknown.Unknown", font=("Terminal",12),justify=LEFT)
                lbl.pack(side=LEFT)
                mostrar()
            elif entr.get() == "login -n root":
                lbl = Label(resframe, fg=FG, bg=BG, text=textRes(), font=("Terminal",12),justify=LEFT)
                lbl.pack(side=LEFT)
                login()
            #More conditionals and commands
            elif entr.get() == "exit":
                window.destroy()
                return
            else:
                lbl = Label(resframe, fg=FG, bg=BG, text="Unknown command", font=("Terminal",12))
                lbl.pack(side=LEFT)
                mostrar()
        frame = Frame(bodyCanvas, bg=BG, borderwidth="0")
        frame.pack(anchor="nw", fill=X)
        Label(frame, fg=FG, bg=BG, text="$", font=("Terminal",12)).pack(side=LEFT)
        entr = Entry(frame, fg=FG, bg=BG, borderwidth="0", font=("Terminal",12))
        entr.pack(side=LEFT)
        entr.after(1, lambda:entr.focus_force())

        entr.bind('<Return>',handler)
        return

    def login():
        def handlerLog(e):
            entr.config(state="disabled",disabledbackground=BG,disabledforeground=FG)
            if entr.get() == "bin/history":
                dictHist = {
                    488: "cd/opt/LLL/controller/laser/",
                    489: "vi LLLSDLaserControl.c",
                    490: "make",
                    491: "make install",
                    492: "./sanity_check",
                    493: "./configure -o test.cfg",
                    494: "vi test.cfg",
                    495: "vi ~/last_will_and_testament.txt",
                    496: "cat/Proc/meminfo",
                    497: "ps -a -x -u",
                    498: "kill -9 2207",
                    499: "kill 2208",
                    500: "ps -a -x -u",
                    501: "touch/opt/LLL/run/ok",
                    502: "LLLSDLaserControl -ok 1"
                }

                for i in range(488,503):
                    resframe = Frame(bodyCanvas, bg=BG, borderwidth="0")
                    resframe.pack(anchor="nw", fill=X)
                    lbl = Label(resframe, fg=FG, bg=BG, text=str(i), font=("Terminal",12), padx="10px")
                    lbl.pack(side=LEFT)
                    lbl = Label(resframe, fg=FG, bg=BG, text=dictHist[i], font=("Terminal",12))
                    lbl.pack(side=LEFT)
                login()
            elif entr.get() == "bin/LLLSDLaserControl -ok 1":
                comms = [
                    "Starting up...",
                    "PSU online",
                    "HV online",
                    "Analog core memory... OK!",
                    "Booting pattern recognition systems",
                    "Merging current data model",
                    "Starting laser emitter",
                    "Particle traps test OK!",
                    "Entangling laser with particles traps"
                ]

                for i in range(9):
                    resframe = Frame(bodyCanvas, bg=BG, borderwidth="0")
                    resframe.pack(anchor="nw", fill=X)
                    lbl = Label(resframe, fg=FG, bg=BG, text="*", font=("Terminal",12), padx="10px")
                    lbl.pack(side=LEFT)
                    lbl = Label(resframe, fg=FG, bg=BG, text=comms[i], font=("Terminal",12))
                    lbl.pack(side=LEFT)
                entryWindow()
            #More conditionals and commands
            elif entr.get() == "exit":
                window.destroy()
                return
            else:
                resframe = Frame(bodyCanvas, bg=BG, borderwidth="0")
                resframe.pack(anchor="nw", fill=X)
                lbl = Label(resframe, fg=FG, bg=BG, text="Unknown command", font=("Terminal",12))
                lbl.pack(side=LEFT)
                login()
        frame = Frame(bodyCanvas, bg=BG, borderwidth="0")
        frame.pack(anchor="nw", fill=X)
        Label(frame, fg=FG, bg=BG, text="#", font=("Terminal",12)).pack(side=LEFT)
        entr = Entry(frame, fg=FG, bg=BG, borderwidth="0", width=80, font=("Terminal",12))
        entr.pack(side=LEFT)
        entr.focus()

        entr.bind('<Return>',handlerLog)
        return

    def entryWindow():
        qWind = Tk()
        qWind.title("Warning")
        qWind.geometry("450x100+500+350")
        qWind.resizable(0,0)
        qWind.config(bg="#fffc9a")
        qWind.after(1, lambda:qWind.focus_force())

        Label(qWind, bg="#fffc9a", text="Aperture Clear?", font=("Terminal",12, BOLD), pady="10px").pack()
        optFrame = Frame(qWind, bg="#fffc9a", borderwidth="0")
        optFrame.pack(anchor="nw", fill=X)

        def destroyAll():
            qWind.destroy()
            window.destroy()
            bgWind.destroy()

        def focusbtn():
            btnYes.config(bg="#318fff", fg="white")
            qWind.bind('<Return>', lambda e: btnYes.invoke())

        def focusLeft(e):
            btnYes.config(bg="#318fff", fg="white")
            btnNo.config(bg="#fffc9a", fg="black")
            qWind.bind('<Return>', lambda e: btnYes.invoke())

        def focusRight(e):
            btnYes.config(bg="#fffc9a", fg="black")
            btnNo.config(bg="#318fff", fg="white")
            qWind.bind('<Return>', lambda e: btnNo.invoke())

        yOF = Frame(optFrame, bg="#fffc9a", borderwidth="0")
        yOF.pack(side=LEFT, padx="30px")
        Label(yOF, text="< ", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0").pack(side=LEFT)
        btnYes = Button(yOF, text="Yes", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0", activebackground="#318fff", activeforeground="white", command=destroyAll)
        btnYes.pack(side=LEFT)
        btnYes.after(1, focusbtn)
        Label(yOF, text=" >", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0").pack(side=LEFT)

        nOF = Frame(optFrame, bg="#fffc9a", borderwidth="0")
        nOF.pack(side=RIGHT, padx="30px")
        Label(nOF, text="< ", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0").pack(side=LEFT)
        btnNo = Button(nOF, text="No", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0", activebackground="#318fff", activeforeground="white", command=lambda: qWind.destroy())
        btnNo.pack(side=LEFT)
        Label(nOF, text=" >", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0").pack(side=LEFT)

        qWind.bind('<Left>', focusLeft)
        qWind.bind('<Right>', focusRight)
        #Button(optFrame, text="< Yes >", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0").pack(side=LEFT, padx="30px")
        #Button(optFrame, text="< No >", bg="#fffc9a", font=("Terminal",12, BOLD), borderwidth="0").pack(side=RIGHT, padx="30px")
        #menufrm = Frame(window, bg=FG, borderwidth="0")
        #menufrm.pack(anchor="nw", fill=X)
    mostrar()
    window.mainloop()

#def dropWindow():
#    bgWind.destroy()

menufrm = Frame(bgWind, bg=BG, borderwidth="0")
menufrm.pack(anchor="nw", fill=X)
Button(menufrm, text="Open Console", command=newWind, bg=FG, width=20, height=5, font=("Terminal",11, BOLD)).pack(side=LEFT, padx="5px")
Button(menufrm, text="Close", command=lambda: bgWind.destroy(), bg=FG, width=20, height=5, font=("Terminal",11, BOLD)).pack(side=LEFT, padx="5px")
Label (menufrm, text="> Crated by: Kotaru196 <", bg=BG, fg=FG, font=("Terminal", 12, BOLD)).pack(side=LEFT, padx="30px")

bgWind.mainloop()