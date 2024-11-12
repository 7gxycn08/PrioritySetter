import os.path
import threading
import winreg
import customtkinter
from tkinter import messagebox, filedialog
import ctypes
from PIL import Image

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except AttributeError:
    ctypes.windll.user32.SetProcessDPIAware(True)


def add_exe_to_reg():
    cpu_priority_levels = {
        "Idle": 1,
        "Normal": 2,
        "High": 3,
        "RealTime": 4
    }
    io_priority_levels = {
        "Very Low": 0,
        "Low": 1,
        "Normal": 2,
        "High": 3,
        "Critical": 4
    }
    memory_priority_levels = {
        "Very Low": 1,
        "Low": 2,
        "Medium": 3,
        "Below Normal": 4,
        "Normal": 5
    }

    selected_cpu_priority = cpu_option.get()
    selected_io_priority = io_option.get()
    selected_memory_priority = memory_option.get()
    cpu_value = cpu_priority_levels[selected_cpu_priority]
    io_value = io_priority_levels[selected_io_priority]
    memory_value = memory_priority_levels[selected_memory_priority]

    exe_path = filedialog.askopenfilename(title="Select EXE", filetypes=[("Executable files", "*.exe")])
    exe_name = os.path.basename(exe_path)
    if exe_name == "":
        return
    base_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
    key_name = exe_name
    registry_path = fr"{base_path}\{key_name}"
    key = None
    try:
        key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, fr"{registry_path}\PerfOptions",
                                 0, winreg.KEY_SET_VALUE)

        value_name_str = "CpuPriorityClass"
        winreg.SetValueEx(key, value_name_str, 0, winreg.REG_DWORD, cpu_value)

        value_name_str = "IoPriority"
        winreg.SetValueEx(key, value_name_str, 0, winreg.REG_DWORD, io_value)

        value_name_str = "PagePriority"
        winreg.SetValueEx(key, value_name_str, 0, winreg.REG_DWORD, memory_value)

        messagebox.showinfo(title="Done.", message="EXE Priority Settings Added to Registry.")

    except OSError as e:
        messagebox.showerror(title="Error", message=f"Error creating registry key: {e}")
        if e.winerror == 87:
            messagebox.showerror(title="Error",
                                 message="The parameter might be incorrect. "
                                 "Check if the registry path follows the expected format.")
            messagebox.showerror(title="Error", message=f"Registry Path: {registry_path}")
        else:
            messagebox.showerror(title="Error", message="Unexpected error.")
    finally:
        if key is not None:
            winreg.CloseKey(key)

def remove_game():
    exe_path = filedialog.askopenfilename(title="Select EXE", filetypes=[("Executable files", "*.exe")])
    exe_name = os.path.basename(exe_path)
    if exe_name == "":
        messagebox.showerror(title="Error.", message="Select EXE to Uninstall Priority Settings.")
        return
    base_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
    key_name = exe_name
    registry_path = fr"{base_path}\{key_name}"
    try:
        # Try to open the key to check if it exists
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.CloseKey(key)
        # If it opens successfully, close it and delete it
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, fr"{registry_path}\PerfOptions")
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, fr"{base_path}\{key_name}")
        messagebox.showinfo(title="Done.", message=f"Priority Settings Uninstalled Successfully: {registry_path}")
    except FileNotFoundError:
        messagebox.showinfo(title="Done.", message=f"Registry key does not exist: {registry_path}")
    except PermissionError:
        messagebox.showinfo(title="Done.", message="Permission denied: Unable to delete the registry key.")


customtkinter.set_appearance_mode("dark")  # Modes: Computer (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry("400x440")
app.title("PrioritySetter v1.0")
app.iconbitmap(r"Resources\boost.ico")
blank_image = Image.new('RGB', (1, 1))

cpu_label = customtkinter.CTkLabel(master=app, text=" CPU Priority")
cpu_label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
cpu_option = customtkinter.CTkOptionMenu(master=app, values=["Idle","Normal","High","RealTime"])
cpu_option.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

io_label = customtkinter.CTkLabel(master=app, text=" IO Priority")
io_label.place(relx=0.5, rely=0.30, anchor=customtkinter.CENTER)
io_option = customtkinter.CTkOptionMenu(master=app, values=["Very Low","Low","Normal","High","Critical"])
io_option.place(relx=0.5, rely=0.40, anchor=customtkinter.CENTER)

memory_label = customtkinter.CTkLabel(master=app, text=" Memory Priority")
memory_label.place(relx=0.5, rely=0.50, anchor=customtkinter.CENTER)
memory_option = customtkinter.CTkOptionMenu(master=app, values=["Very Low","Low","Medium","Below Normal","Normal"])
memory_option.place(relx=0.5, rely=0.60, anchor=customtkinter.CENTER)

add_button = customtkinter.CTkButton(master=app, text="Set EXE Priority",
                                     command=lambda: threading.Thread(target=lambda: add_exe_to_reg(),
                                                                      daemon=True).start())
add_button.place(relx=0.5, rely=0.80, anchor=customtkinter.CENTER)
remove_button = customtkinter.CTkButton(master=app, text="Remove EXE Priority",
                                     command=lambda: threading.Thread(target=lambda: remove_game(),
                                                                      daemon=True).start())
remove_button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)
app.mainloop()
