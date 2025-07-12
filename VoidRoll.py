import customtkinter as ctk
import random
import time
from threading import Thread

# OG Unicode Dice Symbols ⚀–⚅
DICE_UNICODE = {
    1: '⚀', 2: '⚁', 3: '⚂',
    4: '⚃', 5: '⚄', 6: '⚅'
}

class VoidRoll(ctk.CTk):  # 🔥 Class renamed to VoidRoll
    def __init__(self):
        super().__init__()

        # 🖤 Window Config - AMOLED Ready
        self.title("🎲 VoidRoll")
        self.geometry("400x500")
        self.configure(bg="#000000")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # 💡 Full Black Frame for 100% AMOLED
        self.main_frame = ctk.CTkFrame(self, fg_color="#000000", bg_color="#000000")
        self.main_frame.pack(expand=True, fill="both")

        # 🧠 Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="VoidRoll 🎲",
            font=("Segoe UI", 28, "bold"),
            text_color="white",
            bg_color="#000000"
        )
        self.title_label.pack(pady=25)

        # 🎲 Dice Display
        self.dice_label = ctk.CTkLabel(
            self.main_frame,
            text="⚀",
            font=("Segoe UI Emoji", 120),
            text_color="white",
            bg_color="#000000"
        )
        self.dice_label.pack(pady=30)

        # 🔁 Roll Button
        self.roll_button = ctk.CTkButton(
            self.main_frame,
            text="🎲 Roll Dice",
            font=("Arial", 20, "bold"),
            fg_color="transparent",
            border_color="#ff0000",
            border_width=2,
            text_color="white",
            corner_radius=100,
            bg_color="#000000",
            command=self.animate_dice_roll
        )
        self.roll_button.pack(pady=20, ipadx=10, ipady=5)

        # ❌ Exit Button
        self.quit_button = ctk.CTkButton(
            self.main_frame,
            text="❌ Exit",
            font=("Arial", 16),
            fg_color="transparent",
            border_color="#ff0000",
            border_width=2,
            text_color="white",
            corner_radius=100,
            bg_color="#000000",
            command=self.quit
        )
        self.quit_button.pack(pady=10, ipadx=10, ipady=5)

        # 💗 Footer Branding
        self.footer = ctk.CTkLabel(
            self.main_frame,
            text="Powered by 💗 Y7X",
            font=("Arial", 12),
            text_color="gray",
            bg_color="#000000"
        )
        self.footer.pack(side="bottom", pady=20)

    def animate_dice_roll(self):
        Thread(target=self._roll_animation_thread).start()

    def _roll_animation_thread(self):
        for _ in range(15):
            rand = random.randint(1, 6)
            self.dice_label.configure(text=DICE_UNICODE[rand])
            time.sleep(0.05)

        final_result = random.randint(1, 6)
        self.dice_label.configure(text=DICE_UNICODE[final_result])

if __name__ == "__main__":
    app = VoidRoll()
    app.mainloop()