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


root = tk.Tk()
root.title("Spark Calculator")
root.geometry("340x360")
root.resizable(False, False)

padding = tk.Label(root, height=2)
padding.pack()

single_draw_label = tk.Label(root, text="Single Draw Tickets:")
single_draw_label.pack()
single_draw_entry = tk.Entry(root, justify="center")
single_draw_entry.insert(0, "0")
single_draw_entry.pack()

ten_draw_label = tk.Label(root, text="Ten Draw Tickets:")
ten_draw_label.pack()
ten_draw_entry = tk.Entry(root, justify="center")
ten_draw_entry.insert(0, "0")
ten_draw_entry.pack()

crystals_label = tk.Label(root, text="Crystals:")
crystals_label.pack()
crystals_entry = tk.Entry(root, justify="center")
crystals_entry.insert(0, "0")
crystals_entry.pack()

padding = tk.Label(root, height=2)
padding.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_spark)
calculate_button.pack()

padding = tk.Label(root, height=2)
padding.pack()

rolls_label = tk.Label(root, text="Total Rolls: ")
rolls_label.pack()
sparks_label = tk.Label(root, text="Sparks: ")
sparks_label.pack()
percentage_label = tk.Label(root, text="Percentage: ")
percentage_label.pack()

padding = tk.Label(root, height=2)
padding.pack()

root.mainloop()
