import PySimpleGUI as sg
window = sg.Window(title="Profile",
                        layout=[{sg.Text("NPM   : 2210010353")},
                                {sg.Text("Nama  : ADINDA SYAH PUTRI")},
                                {sg.Text("Kelas : 5M Regular Banjarmasin")},
                                {sg.Text("Matkul: Pemrograman Visual 3")},
                                ],
                        size=(400,200))
window()
window.close()