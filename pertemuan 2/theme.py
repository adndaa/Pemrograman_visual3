import PySimpleGUI as sg
sg.theme("DarkGrey5")
sg.theme_text_color("#E3CF57")
window = sg.Window(title="Profile",
                        layout=[{sg.Text("SELAMAT DATANG DIKELAS",
                                font=("times",20,"italic","bold","underline"))},
                                {sg.Text("NPM   : 2210010353")},
                                {sg.Text("Nama  : ADINDA SYAH PUTRI")},
                                {sg.Text("Kelas : 5M Regular Banjarmasin")},
                                ],
                        size=(400,200),
                        font=("times", 15))
window()
window.close()