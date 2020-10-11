from dearpygui.core import  *
add_additional_font("arial.ttf", 20, )
add_text("Vokabel trainer")
def start_clicked(sender, data):
    print("clicked: "+sender )
add_button("start" , callback = start_clicked)

start_dearpygui()
