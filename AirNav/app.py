import tkinter as tk
from math import cos, sin, radians
import threading
import time
import os

class Ui:
    @staticmethod
    def create_menu():
        f = open("Ui/pos.txt", "w")
        f.write("")
        f.close()
        num_options = 10  # تعداد گزینه‌ها
        radius = 150  # شعاع منو
        window_width = 500  # عرض پنجره
        window_height = 500  # ارتفاع پنجره
        root = tk.Tk()
        root.title("Circular Menu")
        pg_loop = True

        # محاسبه مختصات مرکز پنجره بر اساس اندازه صفحه نمایش
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        # تنظیم مختصات پنجره بر اساس محاسبات قبلی
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        try:
            root.wm_attributes("-transparentcolor", "#f0f0f0")
        except:
            pass
        canvas = tk.Canvas(root, width=window_width, height=window_height)
        canvas.pack()
        root.overrideredirect(1)  # Remove border
        root.wm_attributes("-topmost", 1)

        def hide_window():
            root.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")

        def show_window():
            root.geometry(f"{window_width}x{window_height}+{x}+{y}")


        def loop():
            nonlocal pg_loop
            while pg_loop:
                with open("Ui/val.txt", "r") as f:
                    if f.read() == "True":
                        show_window()
                    else:
                        hide_window()

                with open("Ui/end.txt", "r") as f:
                    if f.read() == "True":
                        break
            exit()

        thread1 = threading.Thread(target=loop)
        thread1.start()

        def option_clicked(option):
            with open("setting/btn.txt", "r") as f:
                do = f.read()
            do = do.split("\n")
            for i in range(len(do)):
                if do[i] == "exit":
                    if option == i + 1:
                        with open("Ui/end.txt", "w") as f:
                            f.write("True")
                        time.sleep(1)
                        root.destroy()
                        exit()
                elif do[i] == "hide":
                    if option == i + 1:
                        with open("Ui/val.txt", "w") as f:
                            f.write("False")
                elif do[i] == "mouse":
                    if option == i + 1:
                        with open("Ui/val.txt", "w") as f:
                            f.write("False")
                        with open("Ui/mouse.txt", "w") as f:
                            f.write("True")
                else:
                    if option == i + 1:
                        os.system(f"start {do[i]}")

        def save_btn_pos(angle, x, y, option):
            with open("Ui/pos.txt", "a+") as f:
                if option == 10:
                    f.write(f"{angle};{x};{y};{option}")
                else:
                    f.write(f"{angle};{x};{y};{option}\n")

        def stay_on_top():
            root.lift()
            root.after(200, stay_on_top)

        # تابعی برای ایجاد گزینه‌ها
        def create_option(angle, option, real_angle):
            x = center_x + radius * sin(angle)
            y = center_y + radius * cos(angle)
            save_btn_pos(real_angle, x, y, option)
            option_button = canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="white")
            option_text = canvas.create_text(x, y, text=str(option), font=("Arial", 12), fill="black")

            def highlight(event):
                canvas.itemconfig(option_button, fill="black")
                canvas.itemconfig(option_text, fill="white")

            def unhighlight(event):
                canvas.itemconfig(option_button, fill="white")
                canvas.itemconfig(option_text, fill="black")

            canvas.tag_bind(option_button, "<Enter>", highlight)
            canvas.tag_bind(option_button, "<Leave>", unhighlight)
            canvas.tag_bind(option_text, "<Enter>", highlight)
            canvas.tag_bind(option_text, "<Leave>", unhighlight)
            canvas.tag_bind(option_button, "<Button-1>", lambda event, option=option: option_clicked(option))

        # محاسبه مختصات مرکز دایره بر اساس اندازه پنجره
        center_x = int(window_width / 2)
        center_y = int(window_height / 2)

        # ایجاد گزینه‌ها در دایره
        for i in range(num_options):
            angle = radians((360 / num_options) * i)
            create_option(angle, i + 1, ((360 / num_options) * i))

        stay_on_top()
        root.mainloop()


# Ui.create_menu()
