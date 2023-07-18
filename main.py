import random
import tkinter as tk


BACKGROUND_COLOR = "#1e1e1e"
WALL_COLOR = "#000000"
PATH_COLOR = "#ffffff"
TEXT_COLOR = "#ffffff"

def generate_maze(width, height):
    maze = [[1] * width for _ in range(height)]
    stack = []
    start_x, start_y = random.randint(0, width-1), random.randint(0, height-1)
    stack.append((start_x, start_y))
    maze[start_y][start_x] = 0

    while stack:
        current_x, current_y = stack[-1]
        neighbors = []


        if current_x > 1 and maze[current_y][current_x - 2] == 1:
            neighbors.append((current_x - 2, current_y))
        if current_x < width - 2 and maze[current_y][current_x + 2] == 1:
            neighbors.append((current_x + 2, current_y))
        if current_y > 1 and maze[current_y - 2][current_x] == 1:
            neighbors.append((current_x, current_y - 2))
        if current_y < height - 2 and maze[current_y + 2][current_x] == 1:
            neighbors.append((current_x, current_y + 2))

        if neighbors:
            next_x, next_y = random.choice(neighbors)
            stack.append((next_x, next_y))
            maze[next_y][next_x] = 0
            maze[current_y + (next_y - current_y) // 2][current_x + (next_x - current_x) // 2] = 0
        else:
            stack.pop()

    return maze


def draw_maze(canvas, maze, cell_size):
    canvas.delete("all")
    width = len(maze[0])
    height = len(maze)

    for row in range(height):
        for col in range(width):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            if maze[row][col] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill=WALL_COLOR)
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill=PATH_COLOR)


def generate_button_clicked():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())

        maze = generate_maze(width, height)
        draw_maze(canvas, maze, cell_size)
    except ValueError:
        pass


window = tk.Tk()
window.title("Maze Generator")
window.configure(bg=BACKGROUND_COLOR)

cell_size = 20
canvas_width = 600
canvas_height = 600
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack()

controls_frame = tk.Frame(window, bg=BACKGROUND_COLOR)
controls_frame.pack(pady=10)

width_label = tk.Label(controls_frame, text="Width:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
width_label.pack(side=tk.LEFT, padx=5, pady=5)
width_entry = tk.Entry(controls_frame)
width_entry.pack(side=tk.LEFT, padx=5, pady=5)

height_label = tk.Label(controls_frame, text="Height:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
height_label.pack(side=tk.LEFT, padx=5, pady=5)
height_entry = tk.Entry(controls_frame)
height_entry.pack(side=tk.LEFT, padx=5, pady=5)

generate_button = tk.Button(controls_frame, text="Generate Maze", command=generate_button_clicked,
                            bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
generate_button.pack(pady=10)

window.mainloop()
