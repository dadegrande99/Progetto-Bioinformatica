import customtkinter as ctk
import os
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from alignmentfreegraph import AlignmentFreeGraph

plt.rcParams['figure.figsize'] = [16, 9]
plt.rcParams['figure.dpi'] = 80

# Variables
afg = None
selected_file = None
hash_table = None

# Functions


def do_new_nothing():
    pass


def close_new_window():
    new_window.destroy()


def select_config_file():
    global selected_file
    selected_file = open_file_dialog_json()
    # controlla se il file scelta è nella stessa directory di interface.py, nel caso lo sia cancella il path e tieni solo il nominee

    file_label.configure(text=selected_file.split("/")[-1])


def open_file_dialog():
    # Use the global keyword to indicate that we want to use the global variable
    global selected_file
    selected_file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                               filetypes=[("json files", "*.json"), ("text files", "*.txt"), ("all files", "*.*")])
    # Do something with the filename
    return selected_file


def open_file_dialog_json():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                          filetypes=[("json files", "*.json")])
    return filename


def is_file_in_current_directory(filename):
    files_in_directory = os.listdir('.')
    return filename in files_in_directory


def login():
    print("Login")
    location = location_entry.get()
    if location == "":
        location = None
    db_name = db_name_entry.get()
    if db_name == "":
        db_name = None
    username = username_entry.get()
    if username == "":
        username = None
    password = password_entry.get()
    if password == "":
        password = None

    global afg
    global selected_file

    print(selected_file)
    new_window.destroy()
    try:
        afg = AlignmentFreeGraph(
            location, db_name, username, password, selected_file)
        print("Connected")
        selected_file = None

    except Exception as e:
        new_connection(error=e)


def plot_graph(graph: nx.DiGraph):
    fig = Figure(figsize=(10, 6), dpi=50)
    ax = fig.add_subplot(111)

    pos = nx.spring_layout(graph)

    nx.draw_networkx_nodes(graph, pos, node_size=1000,
                           node_color="skyblue", node_shape="o", alpha=0.8, ax=ax)
    nx.draw_networkx_labels(graph, pos, labels=nx.get_node_attributes(
        graph, "name"), font_weight="bold", font_size=14, font_color="black", font_family="arial", ax=ax)
    node_labels = {node: f"\n\n\n{node}" for node in graph.nodes}
    nx.draw_networkx_labels(
        graph, pos, labels=node_labels, font_color='black', ax=ax)
    for edge in graph.edges:
        rad = -0.2
        for color in graph.edges[edge]["label"].split("+"):
            nx.draw_networkx_edges(graph, pos, edgelist=[
                                   edge], connectionstyle=f"arc3,rad={rad}", arrows=True, arrowsize=20, width=2, edge_color=color, ax=ax)
            if rad < 0:
                rad *= -1
            else:
                rad += 0.2
                rad *= -1

    fig.tight_layout()
    ax.set_axis_off()
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side="left")


def new_connection(message: str = "Create a conection", error: str = None):

    global new_window
    new_window = ctk.CTkToplevel(master=root)
    new_window.title("New Connection")
    new_window.geometry("500x500")

    if afg is None:
        root.config(bg='gray')
        new_window.grab_set()
        # change the background color back to white when the new window is closed
        new_window.bind('<Destroy>', lambda e: root.config(bg=root_bg_color))
        new_window.protocol("WM_DELETE_WINDOW", do_new_nothing)
    else:
        new_window.protocol("WM_DELETE_WINDOW", close_new_window)

    message_label = ctk.CTkLabel(
        master=new_window, text=message, font=("Roboto", 16))
    message_label.pack()

    if error is not None:
        error_label = ctk.CTkLabel(
            master=new_window, text=error, text_color="red")
        error_label.pack()

    conn_bg_color = new_window.cget("bg")

    global file_label
    file_button = ctk.CTkButton(
        master=new_window, text="Connect by file", command=select_config_file, fg_color="#24a0ed", hover_color="#1183ca")
    file_button.pack(pady=10)

    file_label = ctk.CTkLabel(
        master=new_window, text="", font=("Consolas", 12))
    file_label.pack()

    global location_entry
    location_frame = ctk.CTkFrame(
        master=new_window, bg_color=conn_bg_color)
    location_label = ctk.CTkLabel(master=location_frame, text="Location")
    location_entry = ctk.CTkEntry(
        master=location_frame, placeholder_text="Location")

    global db_name_entry
    db_name_frame = ctk.CTkFrame(master=new_window, bg_color=conn_bg_color)
    db_name_label = ctk.CTkLabel(master=db_name_frame, text="DB Name")
    db_name_entry = ctk.CTkEntry(
        master=db_name_frame, placeholder_text="DB Name")

    global username_entry
    username_frame = ctk.CTkFrame(master=new_window, bg_color=conn_bg_color)
    username_label = ctk.CTkLabel(master=username_frame, text="Username")
    username_entry = ctk.CTkEntry(
        master=username_frame, placeholder_text="Username")

    global password_entry
    password_frame = ctk.CTkFrame(master=new_window, bg_color=conn_bg_color)
    password_label = ctk.CTkLabel(master=password_frame, text="Password")
    password_entry = ctk.CTkEntry(
        master=password_frame, show="*", placeholder_text="Password")

    location_label.pack(side="left", padx=5)
    location_entry.pack(side="left")
    location_frame.pack(pady=10)

    db_name_label.pack(side="left", padx=5)
    db_name_entry.pack(side="left")
    db_name_frame.pack(pady=10)

    username_label.pack(side="left", padx=5)
    username_entry.pack(side="left")
    username_frame.pack(pady=10)

    password_label.pack(side="left", padx=5)
    password_entry.pack(side="left")
    password_frame.pack(pady=10)

    login_button = ctk.CTkButton(
        master=new_window, text="Login", command=login,)
    login_button.pack(pady=30)


def show_hashtable():
    global afg

    # Create a treeview for the hashtable
    for widget in hash_table_frame.winfo_children():
        widget.destroy()
    tree = ttk.Treeview(
        hash_table_frame, selectmode='browse', show='headings')

    # Assuming hashtable is a dictionary
    hashtable = afg.get_hashtable()  # Replace with your method to get the hashtable

    # Create the columns
    tree["columns"] = ("Key", "Value")
    tree.column("#0", width=0, stretch=ctk.NO)
    tree.column("Key", anchor="w", width=30)
    tree.column("Value", anchor="w")

    # Create the headings
    tree.heading("#0", text="", anchor=ctk.W)
    tree.heading("Key", text="Key", anchor=ctk.W)
    tree.heading("Value", text="Value", anchor=ctk.W)

    # Add the data from the hashtable
    for key, value in hashtable.items():
        if value == {}:
            tree.insert(parent='', index='end', values=(key, "-"))
        else:
            for k in value:
                tree.insert(parent='', index='end',
                            values=(key, f"{k}: {value[k]}"))
                key = ""

    tree.pack()


def change_k(event):
    global afg
    global k_value_entry
    k = k_value_entry.get()
    if feasible_k():
        k = int(k)
        if k != afg.get_k():
            afg.set_k(k)
            show_hashtable()
            k_value_problem_label.configure(text="")
    k_value_entry.delete(0, tk.END)
    k_value_entry.insert(0, str(afg.get_k()))
    k_value_problem_label.configure(
        text=k + " not feasible")


def feasible_k():
    # controll k value is a number
    global k_value_entry
    k = k_value_entry.get()
    if is_int(k):
        k = int(k)
        if k > 1:
            return True
    return False


def is_int(string: str):
    return string.isdigit()

# Creating interface


# interface style
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# main window
root = ctk.CTk()
root.geometry("800x800")
root.minsize(500, 500)
root.maxsize(1000, 1000)
root_bg_color = root.cget("bg")

root.title("Alignment-Free Sequence to Graph")

open_window_button = ctk.CTkButton(
    master=root, text="New Connection", command=new_connection)
open_window_button.pack(anchor="ne", pady=5, padx=10)
# frame of the interface
frame = ctk.CTkFrame(master=root)
frame.pack(pady=10, padx=15, fill="both", expand=True)
# Project title
title = ctk.CTkLabel(
    master=frame, text="Alignment-Free Sequence to Graph", font=("Roboto", 24))
title.pack(pady=5, padx=10)

if afg is None and is_file_in_current_directory("credentials.json"):
    try:
        afg = AlignmentFreeGraph(configuration="credentials.json")
    except Exception as e:
        new_connection(error=e)

graph_frame = ctk.CTkFrame(master=frame)
graph_frame.pack(pady=10, padx=15, anchor="n", expand=True)

plot_graph(afg.get_networkx_di_graph())

k_value_frame = ctk.CTkFrame(master=graph_frame)
k_value_label = ctk.CTkLabel(master=k_value_frame, text="k = ")
k_value_entry = ctk.CTkEntry(master=k_value_frame, width=45)
k_value_entry.insert(0, str(afg.get_k()))
k_value_frame.pack(anchor="n", pady=10, padx=5, expand=True)
k_value_label.pack(side="left", anchor="n", pady=10, padx=5)
k_value_entry.pack(side="left", anchor="n", pady=10, padx=3)
k_value_entry.bind("<Return>", change_k)
k_value_problem_label = ctk.CTkLabel(
    master=k_value_frame, text="", text_color="red")
k_value_problem_label.pack(side="left", pady=0, padx=1, expand=True)

hash_table_frame = ctk.CTkFrame(master=graph_frame)
hash_table_frame.pack(side="right", pady=10, padx=15, expand=True)


show_hashtable()

show_hashtable_button = ctk.CTkButton(
    master=frame, text="Show Hashtable", command=show_hashtable, fg_color="#24a0ed", hover_color="#1183ca")
show_hashtable_button.pack(anchor="n", pady=20, padx=10)

# Create a button that will close the interface when clicked

exit_button = ctk.CTkButton(
    master=root, text="Exit", command=root.destroy, fg_color="#df2c14", hover_color="#c61a09")
exit_button.pack(side='bottom', pady=5, padx=10)


root.mainloop()