import tkinter as tk


def calculate_spark() -> None:
    try:
        single_draw_tickets = int(single_draw_entry.get() or 0)
        ten_draw_tickets = int(ten_draw_entry.get() or 0)
        crystals = int(crystals_entry.get() or 0)
    except ValueError:
        pass
    else:
        total_rolls = single_draw_tickets + (ten_draw_tickets * 10) + (crystals // 300)
        sparks = total_rolls // 300
        percentage = (total_rolls / 300) * 100

        rolls_label.config(text=f"Total Rolls: {total_rolls}")
        sparks_label.config(text=f"Sparks: {sparks}")
        percentage_label.config(text=f"Percentage: {percentage:.2f}%")


bg_color = "white"

root = tk.Tk()
root.title("Spark Calculator")
root.geometry("340x360")
root.configure(background=bg_color)
root.resizable(False, False)

padding = tk.Label(root, height=2, bg=bg_color)
padding.pack()

single_draw_label = tk.Label(root, text="Single Draw Tickets:", bg=bg_color)
single_draw_label.pack()
single_draw_entry = tk.Entry(root, justify="center", bg=bg_color)
single_draw_entry.insert(0, "0")
single_draw_entry.pack()

ten_draw_label = tk.Label(root, text="Ten Draw Tickets:", bg=bg_color)
ten_draw_label.pack()
ten_draw_entry = tk.Entry(root, justify="center", bg=bg_color)
ten_draw_entry.insert(0, "0")
ten_draw_entry.pack()

crystals_label = tk.Label(root, text="Crystals:", bg=bg_color)
crystals_label.pack()
crystals_entry = tk.Entry(root, justify="center", bg=bg_color)
crystals_entry.insert(0, "0")
crystals_entry.pack()

padding = tk.Label(root, height=2, bg=bg_color)
padding.pack()

calculate_button = tk.Button(
    root, text="Calculate", command=calculate_spark, bg=bg_color
)
calculate_button.pack()

padding = tk.Label(root, height=2, bg=bg_color)
padding.pack()

rolls_label = tk.Label(root, text="Total Rolls: ", bg=bg_color)
rolls_label.pack()
sparks_label = tk.Label(root, text="Sparks: ", bg=bg_color)
sparks_label.pack()
percentage_label = tk.Label(root, text="Percentage: ", bg=bg_color)
percentage_label.pack()

padding = tk.Label(root, height=3, bg=bg_color)
padding.pack()

root.mainloop()
