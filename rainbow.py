import tkinter as tk
import math

# Define rainbow colors
RAINBOW_COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_octagon(canvas, center_x, center_y, radius, color):
    """Draws a regular octagon centered at (center_x, center_y)."""
    points = []
    for i in range(8):
        angle_deg = 45 * i - 90  # Start from top
        angle_rad = math.radians(angle_deg)
        x = center_x + radius * math.cos(angle_rad)
        y = center_y + radius * math.sin(angle_rad)
        points.extend((x, y))
    canvas.create_polygon(points, outline="black", fill=color, width=2)

def draw_rainbow_octagons(canvas, center_x, center_y, start_radius, step):
    """Draws concentric rainbow octagons."""
    for i, color in enumerate(RAINBOW_COLORS):
        draw_octagon(canvas, center_x, center_y, start_radius + i * step, color)

def main():
    root = tk.Tk()
    root.title("Rainbow Octagons")

    canvas_size = 500
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack()

    # Draw rainbow octagons in the center
    draw_rainbow_octagons(canvas, canvas_size / 2, canvas_size / 2, 40, 15)

    root.mainloop()

if __name__ == "__main__":
    main()
