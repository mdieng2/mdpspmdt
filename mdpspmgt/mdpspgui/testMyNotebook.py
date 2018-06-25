import Tkinter as Tk
import ttk as Ttk
#import Tkinter.font as tkFont
import Tkconstants, tkFileDialog
import mdzipmgt.mdzipmgt as Zip


class AppUI(Tk.Frame):

    def __init__(self, master=None):
        self.master_frame = Tk.Frame.__init__(self, master, relief=Tk.SUNKEN, bd=2)
        master.title("MD-PSPMGT")
        menubar = Tk.Menu(master)

        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="Load package", accelerator='Ctrl+O', command=self._load_package)
        menu.add_command(label="Save as", accelerator='Ctrl+S', command=self._save_as)
        menu.add_command(label="Quit", accelerator='Ctrl+Q', command=master.quit)

        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Select All", accelerator='Ctrl+A', command=self._select_all)
        menu.add_command(label="Copy", accelerator='Ctrl+C', command=self._copy_selection)
        menu.add_command(label="Bufferize", accelerator='Ctrl+B', command=self._copy_in_clipboard)

        menu = Tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=menu)
        menu.add_command(label="About", accelerator='Ctrl+H', command=self._app_credentials)

        try:
            master.config(menu=menubar)
        except AttributeError:
            # master is a toplevel window (Python 1.4/Tkinter 1.63)
            master.tk.call(master, "config", "-menu", menubar)

        self.canvas = Tk.Canvas(self, bg="blue", width=910, height=5, bd=0, highlightthickness=0)
        self.canvas.pack()

        # master.bind("<Any-KeyPress>", self._app_credentials)
        master.bind('<Control-O>', self._load_package)
        master.bind('<Control-o>', self._load_package)
        master.bind('<Control-S>', self._save_as)
        master.bind('<Control-s>', self._save_as)
        master.bind('<Control-A>', self._app_credentials)
        master.bind('<Control-a>', self._app_credentials)
        master.bind('<Control-C>', self._select_all)
        master.bind('<Control-c>', self._select_all)
        master.bind('<Control-B>', self._copy_selection)
        master.bind('<Control-b>', self._copy_selection)
        master.bind('<Control-H>', self._copy_in_clipboard)
        master.bind('<Control-h>', self._copy_in_clipboard)
        master.bind('<Control-Q>', self._exit_app)
        master.bind('<Control-q>', self._exit_app)

        # create notebook
        # ###########################################################
        #demoPanel = Tk.Frame(master, name='notebookpanel')  # create a new frame slaved to master
        #pspPanel = Tk.Frame(self.master_frame, name='notebookpanel')  # create a new frame slaved to master
        #pspPanel.pack(fill = "both")  # pack the Frame into root expand = True,
        #pspPanel_canvas = Tk.Canvas(pspPanel, bg="white", width=910, height=0, bd=2, highlightthickness=0)
        #pspPanel_canvas.pack()
        # ###########################################################

        # create (notebook) demo panel
        nb = Ttk.Notebook(master, name='notebook')  # create the ttk.Notebook widget
        #nb_canvas = Tk.Canvas(nb, bg="green", width=0, height=0, bd=2, highlightthickness=0)
        #nb_canvas.pack()

        #canvas = Tk.Canvas(self, bg="green", width=0, height=0, bd=0, highlightthickness=0)
        #canvas.pack()

        # extend bindings to top level window allowing
        #   CTRL+TAB - cycles thru tabs
        #   SHIFT+CTRL+TAB - previous tab
        #   ALT+K - select tab using mnemonic (K = underlined letter)
        nb.enable_traversal()
        # self.canvas = Tk.Canvas(master, bg="white", width=800, height=480, bd=0, highlightthickness=0)
        # nb.pack(fill=Tkconstants.BOTH, expand=Tkconstants.TRUE, padx=2, pady=3)  # add margin
        # self.canvas = Tk.Canvas(nb, bg="white", width=800, height=480, bd=0, highlightthickness=0)
        # self.canvas.pack()

        # create description tab
        # frame to hold (tab) content
        frame = Tk.Frame(nb, name='descrip')

        # widgets to be displayed on 'Description' tab
        msg = [
            "Ttk is the new Tk themed widget set. One of the widgets ",
            "it includes is the notebook widget, which provides a set ",
            "of tabs that allow the selection of a group of panels, ",
            "each with distinct content. They are a feature of many ",
            "modern user interfaces. Not only can the tabs be selected ",
            "with the mouse, but they can also be switched between ",
            "using Ctrl+Tab when the notebook page heading itself is ",
            "selected. Note that the second tab is disabled, and cannot "
            "be selected."]

        lbl = Tk.Label(frame, wraplength='4i', justify=Tkconstants.LEFT, anchor=Tkconstants.N,
                    text=''.join(msg))
        neatVar = Tk.StringVar()
        btn = Tk.Button(frame, text='Neat!', underline=0,
                     command=lambda v=neatVar: self._say_neat(master, v))
                    #command = lambda v=neatVar: self._say_neat(self.master_frame, v))
        neat = Tk.Label(frame, textvariable=neatVar, name='neat')

        # position and set resize behavior
        lbl.grid(row=0, column=0, columnspan=2, sticky='new', pady=5)
        btn.grid(row=1, column=0, pady=(2, 4))
        neat.grid(row=1, column=1, pady=(2, 4))
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure((0, 1), weight=1, uniform=1)

        # bind for button short-cut key
        # (must be bound to toplevel window)
        master.winfo_toplevel().bind('<Alt-n>', lambda e, v=neatVar: self._say_neat(v))

        # add to notebook (underline = index for short-cut character)
        nb.add(frame, text='Description', underline=0, padding=2)

        # create disabled tab
        # Populate the second pane. Note that the content doesn't really matter
        disabled_frame = Tk.Frame(nb)
        nb.add(disabled_frame, text='Disabled', state='disabled')

        # create text tab
        # populate the third frame with a text widget
        txt_frame = Tk.Frame(nb)

        txt = Tk.Text(txt_frame, wrap=Tkconstants.WORD, width=40, height=10)
        vscroll = Ttk.Scrollbar(txt_frame, orient=Tkconstants.VERTICAL, command=txt.yview)
        txt['yscroll'] = vscroll.set
        vscroll.pack(side=Tkconstants.RIGHT, fill=Tkconstants.Y)
        txt.pack(fill=Tkconstants.BOTH, expand=Tkconstants.Y)

        # add to notebook (underline = index for short-cut character)
        nb.add(txt_frame, text='Text Editor', underline=0)

        # Create Frames for the mdpspmgt
        general_frame = Tk.Frame(nb, width=910, height=600, name='general')
        app_frame = Tk.Frame(nb, width=910, height=600,  name='application')
        #app_frame.grid(row=0, column=0, padx=10, pady=2, sticky=Tkconstants.NSEW)
        system_frame = Tk.Frame(nb, width=910, height=600,  name='system')
        manager_frame = Tk.Frame(nb, width=910, height=600,  name='manager')

        # Make all frames scrollable
        gf_scbVDirSel = Tk.Scrollbar(general_frame, orient=Tkconstants.VERTICAL)  # , command=app_frame.yview
        gf_scbVDirSel.pack(side=Tkconstants.RIGHT, fill=Tkconstants.Y)
        #af_scbVDirSel = Tk.Scrollbar(app_frame, orient=Tkconstants.VERTICAL) # , command=app_frame.yview
        #af_scbVDirSel.pack(side=Tkconstants.RIGHT, fill=Tkconstants.Y)
        sf_scbVDirSel = Tk.Scrollbar(system_frame, orient=Tkconstants.VERTICAL)
        sf_scbVDirSel.pack(side=Tkconstants.RIGHT, fill=Tkconstants.Y)
        mf_scbVDirSel = Tk.Scrollbar(manager_frame, orient=Tkconstants.VERTICAL)
        mf_scbVDirSel.pack(side=Tkconstants.RIGHT, fill=Tkconstants.Y)

        # Add the frames to the NoteBook
        nb.add(general_frame, text='General', underline=0, padding=2)
        nb.add(app_frame, text='Application', underline=0, padding=2)
        nb.add(system_frame, text='System', underline=0, padding=2)
        nb.add(manager_frame, text='Manager', underline=0, padding=2)

        #Sample data
        data = [["asd1", "asd2", "asd3", "asd4"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"],
                ["asd1", "asd2", "asd3", "asd3"],
                ["bbb1", "bbb3", "bbb4", "bbb4"],
                ["ccc1", "ccc3", "ccc4", "ccc4"],
                ["ddd1", "ddd3", "ddd4", "ddd4"],
                ["eee1", "eee3", "eee4", "eee4"]]

        tree = Ttk.Treeview(app_frame, columns=(1, 2, 3, 4), height=len(data),
                            selectmode = "extended", show="headings")
        #app_frame.rowconfigure(0, weight=0)
        tree.pack()

        tree.heading(1, text="Number")
        tree.heading(2, text="Trigram")
        tree.heading(3, text="Name")
        tree.heading(4, text="Type")
        tree.column(1, width=150, anchor=Tkconstants.CENTER)
        tree.column(2, width=150, anchor=Tkconstants.CENTER)
        tree.column(3, width=400, anchor=Tkconstants.W)
        tree.column(4, width=200, anchor=Tkconstants.W)

        scroll = Ttk.Scrollbar(nb, orient="vertical", command=tree.yview)
        scroll.pack(side='right', fill='y')

        tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1], val[2], val[3]))

    def _say_neat(self, master, v):
        v.set('Yeah, I know...')
        master.update()
        master.after(500, v.set(''))

    def _exit_app(self, root=None):
        print "exit_app"
        self.master.quit()

    def _load_package(self, root=None):
        print "Enter load_package"
        root.filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("zip files", "*.zip"), ("all files", "*.zip")))
        print (root.filename)
        self._display_package_content(root)
        print "Exit load_package"

    def _save_as(self, root=None):
        print "Save_as"

    def _app_credentials(self, root=None):
        print "app_credentials"

    def _select_all(self, root=None):
        print "select_all"

    def _copy_selection(self, root=None):
        print "copy_selection"

    def _copy_in_clipboard(self, root=None):
        print "copy_in_clipboard"

    def _display_package_content(self, root=None):
        print "Enter _display_package_content"
        print root.filename
        #################
        #Tk.__init__(self)
        t = SimpleTable(self.AppUI_ui_frame.master, 10, 2)
        #t.__init__(root, 10, 2) #self._initFrame(root, 10, 2)
        #root.uiFrame.hide()
        t.pack(side="top", fill="x")
        t.set(0, 0, "Hello")
        t.set(0, 1, "Moussa")
        #################
        file_list = Zip.read_zipfile(root.filename)
        for f in file_list:
            print(f)
        """ print "======================================================================================="
            print "|{:.^6}|{:.^6}|{:.^50}|{:.^20}|".format('Name', 'Number', 'File Name', 'Full Name')
            print "======================================================================================="
            for f in file_list:
                cpnent = Cpnent.component_present(f)
                print "|{:.<6}|{:.<6}|{:.<50}|{:.<20}|".format(cpnent[1], cpnent[0], f, cpnent[2])
            """
        print "Exit _display_package_content"

    def _initFrame(self, parent, rows=10, columns=4):
        # use black background so it "peeks through" to
        # form grid lines
        #Tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Tk.Label(self, text="%s/%s" % (row, column),
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


class SimpleTable(Tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to
        # form grid lines
        Tk.Frame.__init__(self, parent, background="black")
        Tk.Frame.grid_configure(self, row=0, column=0, sticky='nsew')
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Tk.Label(self, text="%s/%s" % (row, column),
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


def runAppUI(self):
    root = Tk.Tk()
    app = AppUI(root)
    app.pack()
    root.mainloop()


def testAppUI(self):
    runAppUI(self=None)


if __name__ == "__main__":
    testAppUI(self=None)