import PySimpleGUI as sg
susunan=[{sg.push(),
        sg.Text("UNISKA MAB",font=("helvetica",24)),
        sg.Push()},
        {sg.Push(),
        sg.Text("BANJARMASIN",font=("courier",18)),
        sg.Push}
        ]
window= sg.Window(title="element_text",
                layout=susunan,
                size=(430,200))

window()
window.close()