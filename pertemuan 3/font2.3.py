import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                        layout=[{sg.Text("FTI UNISKA",
                                        font=("helvetica",24),text_color="#FFFFFF")},
                                {sg.Text("FAKULTAS TEKNOLOGI INFORMASI",
                                        font=("courier",18,"italic","bold","underline"))},
                                {sg.Text("UNISKA MAB BANJARMASIN")}],
                        size=(430,200),
                        font=("times", 18))
window()
window.close()