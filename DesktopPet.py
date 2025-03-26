import random
import tkinter as tk

# Global vars
x = 700        # Start near middle of screen (adjust as needed)
cycle = 0
check = 0      # Start in idle
event_number = random.randrange(1, 10)
impath = '/Users/williamparker/Desktop/Luna Gift (Desktop Code)/Gifs/'

# Categories of event numbers
idle_nums = [1, 2, 3, 4, 5]
walk_left_nums = [6, 7]
walk_right_nums = [8, 9]

def event(cycle, check, event_number, x):
    """Decide which animation state to enter based on event_number."""
    print(f"[EVENT] cycle={cycle}, check={check}, event_number={event_number}, x={x}")

    if event_number in idle_nums:
        check = 0
        print(" -> Switching to IDLE")
        window.after(400, update, cycle, check, event_number, x)

    elif event_number in walk_left_nums:
        check = 1
        print(" -> Walking LEFT")
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in walk_right_nums:
        check = 2
        print(" -> Walking RIGHT")
        window.after(100, update, cycle, check, event_number, x)

def gif_cycle(cycle, frames, event_number, first_num, last_num):
    """Advance to next frame in the animation. If at end, reset & pick new event_number."""
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1)
    return cycle, event_number

def update(cycle, check, event_number, x):
    """Pick the right frame based on check (animation state), then re-schedule event()."""
    print(f"[UPDATE] cycle={cycle}, check={check}, event_number={event_number}, x={x}")

    if check == 0:
        # Idle
        frame = idle_frames[cycle]
        cycle, event_number = gif_cycle(cycle, idle_frames, event_number, 1, 9)

    elif check == 1:
        # Walk left
        frame = walk_left_frames[cycle]
        cycle, event_number = gif_cycle(cycle, walk_left_frames, event_number, 1, 9)
        x -= 5  # Move left a bit

    elif check == 2:
        # Walk right
        frame = walk_right_frames[cycle]
        cycle, event_number = gif_cycle(cycle, walk_right_frames, event_number, 1, 9)
        x += 5  # Move right a bit

    # Update window geometry — ensure we use a plus sign for both x & y
    window.geometry(f'100x100+{x}+400')

    # Update the label
    label.configure(image=frame)
    label.image = frame  # keep a reference
    # Schedule the next event
    window.after(100, event, cycle, check, event_number, x)

# Create window
window = tk.Tk()
window.title("Desktop Pet")
# If you prefer a normal window for debugging, comment out the next line:
# window.overrideredirect(True)

label = tk.Label(window, bd=0)
label.pack()

# Load your GIF frames
# Make sure the '24' and '8' below match the actual number of frames in each GIF
idle_frames = [tk.PhotoImage(file=impath+'Johnny_idle.gif', format='gif -index %i' % i) for i in range(24)]
walk_left_frames = [tk.PhotoImage(file=impath+'Johnny_walk_left.gif', format='gif -index %i' % i) for i in range(8)]
walk_right_frames = [tk.PhotoImage(file=impath+'Johnny_walk_right.gif', format='gif -index %i' % i) for i in range(8)]

# Debug: print how many frames we loaded
print(f"Idle frames loaded: {len(idle_frames)}")
print(f"Walk left frames loaded: {len(walk_left_frames)}")
print(f"Walk right frames loaded: {len(walk_right_frames)}")

# Start the animation
window.after(1, update, cycle, check, event_number, x)
window.mainloop()
