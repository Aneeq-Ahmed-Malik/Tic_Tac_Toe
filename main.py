import random
import customtkinter
from tkinter import font
from CTkMessagebox import CTkMessagebox

WIDTH = 650
HEIGHT = 500
OP_WID = 300
OP_HGT = 330
CANVAS_HEIGHT = HEIGHT - 80
CANVAS_WIDTH = WIDTH

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

DIRECTIONS = [
    [[CANVAS_WIDTH / 6, CANVAS_HEIGHT / 6], [CANVAS_WIDTH / 2, CANVAS_HEIGHT / 6],
     [CANVAS_WIDTH / 1.2, CANVAS_HEIGHT / 6]],
    [[CANVAS_WIDTH / 6, CANVAS_HEIGHT / 2], [CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2],
     [CANVAS_WIDTH / 1.2, CANVAS_HEIGHT / 2]],
    [[CANVAS_WIDTH / 6, CANVAS_HEIGHT / 1.2], [CANVAS_WIDTH / 2, CANVAS_HEIGHT / 1.2],
     [CANVAS_WIDTH / 1.2, CANVAS_HEIGHT / 1.2]],
]


class MainWindow(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.options = None
        self.maxsize(WIDTH, HEIGHT)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - WIDTH) // 2
        y = (screen_height - HEIGHT) // 2

        self.grid_columnconfigure(0, weight=1)

        fonts = list(font.families())
        fonts.sort()
        print(fonts)
        self.title("Tic Tac Toe")
        self.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

        self.heading = customtkinter.CTkLabel(self, text="Tic Tac Toe",
                                              font=customtkinter.CTkFont(family="Fixedsys", size=80, weight="bold"),
                                              text_color="VioletRed1")
        self.heading.grid(row=0, column=0, sticky="ew", pady=70)

        self.start = customtkinter.CTkButton(self, text="Start", width=250, text_color="gray10",
                                             font=customtkinter.CTkFont(family="Fixedsys", size=30, weight="bold"),
                                             hover_color="SpringGreen4", command=self.select_options)

        self.start.grid(row=1, column=0, sticky="s", pady=(20, 20))
        self.exit = customtkinter.CTkButton(self, text="Exit", width=180, text_color="gray20",
                                            font=customtkinter.CTkFont(family="Fixedsys", size=30,
                                                                       weight="bold"),
                                            hover_color="SpringGreen4", command=lambda: self.destroy())
        self.exit.grid(row=2, column=0, sticky="s", pady=(20, 20))

    def select_options(self):
        self.options = customtkinter.CTkToplevel()

        self.options.maxsize(OP_WID, OP_HGT)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - OP_WID) // 2
        y = (screen_height - OP_HGT) // 2

        self.ok = customtkinter.CTkButton(self.options, text="Start", command=self.begin)
        self.ok.grid(row=1, column=0, pady=10)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.options.title("Tic Tac Toe")
        self.options.geometry(f"{OP_WID}x{OP_HGT}+{x}+{y}")
        self.options.attributes('-topmost', 'true')
        self.options.focus_set()

        self.p1 = customtkinter.CTkFrame(self.options, height=140, width=300)
        self.p1.grid(row=0, column=0, sticky="n")
        self.p1.grid_propagate(0)

        self.p1.grid_columnconfigure(2, weight=1)
        self.p1.grid_columnconfigure(1, weight=1)

        self.lbl1 = customtkinter.CTkLabel(self.p1, text="Player 1",
                                           font=customtkinter.CTkFont(family="Fixedsys", size=30, weight="bold"),
                                           text_color="#fccb06")
        self.lbl1.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.name1 = customtkinter.CTkEntry(self.p1)
        self.name1.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew", padx=40)
        self.name1.insert("0", "Player 1")

        self.switch_var1 = customtkinter.StringVar(value=True)
        self.switch1 = customtkinter.CTkSwitch(self.p1, text="Bot",
                                               variable=self.switch_var1, onvalue=True, offvalue=False)

        self.switch1.grid(row=1, column=1, padx=50, sticky="w", pady=15)

        self.mark1 = customtkinter.CTkSegmentedButton(self.p1, values=["O", "X"], command=lambda _: self.mark1_set())
        self.mark1.set("X")
        self.mark1.grid(row=1, column=1, sticky="e", pady=15)

        self.p2 = customtkinter.CTkFrame(self.options, height=140, width=300)
        self.p2.grid(row=2, column=0, sticky="se")
        self.p2.grid_propagate(0)

        self.p2.grid_columnconfigure(2, weight=1)
        self.p2.grid_columnconfigure(1, weight=1)

        self.lbl2 = customtkinter.CTkLabel(self.p2, text="Player 2",
                                           font=customtkinter.CTkFont(family="Fixedsys", size=30, weight="bold"),
                                           text_color="#b1ddf1")
        self.lbl2.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.name2 = customtkinter.CTkEntry(self.p2)
        self.name2.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew", padx=40)
        self.name2.insert("0", "Player 2")

        self.switch_var2 = customtkinter.StringVar(value=True)
        self.switch2 = customtkinter.CTkSwitch(self.p2, text="Bot",
                                               variable=self.switch_var2, onvalue=True, offvalue=False)

        self.switch2.grid(row=1, column=1, padx=50, sticky="w", pady=15)

        self.mark2 = customtkinter.CTkSegmentedButton(self.p2, values=["O", "X"], width=10,
                                                      command=lambda _: self.mark2_set())
        self.mark2.set("O")
        self.mark2.grid(row=1, column=1, sticky="e", pady=15)

    def mark1_set(self):
        if self.mark1.get() == "X":
            self.mark2.set("O")
        elif self.mark1.get() == "O":
            self.mark2.set("X")

    def mark2_set(self):
        if self.mark2.get() == "X":
            self.mark1.set("O")
        elif self.mark2.get() == "X":
            self.mark1.set("X")

    def main_window(self):
        self.heading.grid(row=0, column=0, sticky="ew", pady=70)
        self.start.grid(row=1, column=0, sticky="s", pady=(20, 20))
        self.exit.grid(row=2, column=0, sticky="s", pady=(20, 20))

    def begin(self):
        player1 = {
            "name": self.name1.get(),
            "mark": self.mark1.get(),
            "bot": self.switch1.get(),
            "color": "#fccb06"
        }
        player2 = {
            "name": self.name2.get(),
            "mark": self.mark2.get(),
            "bot": self.switch2.get(),
            "color": "#b1ddf1"
        }

        self.options.destroy()

        self.heading.grid_forget()
        self.start.grid_forget()
        self.exit.grid_forget()

        self.frame = GameWindow(self, player1, player2)
        self.frame.pack(side="top", fill="both", expand=True)
        self.frame.tkraise()


class Game:
    def __init__(self, player1: dict, player2: dict):
        self.board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]
        self.player1 = Bot(player1.get("name"), player1.get("mark"), player1.get("color"), -100) if \
            player1["bot"] else Player(player1.get("name"), player1.get("mark"), player1.get("color"))
        self.player2 = Bot(player2.get("name"), player2.get("mark"), player2.get("color"), 100) if \
            player2["bot"] else Player(player2.get("name"), player2.get("mark"), player2.get("color"))
        self.player1.move = random.randint(0, 1)
        self.empty = True

    def moves_left(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    return True
        return False

    def is_game_over(self):
        won = ["", "", "", ""]
        dia = [(0, 2), (1, 1), (2, 0)]

        for i in range(3):
            flag = False
            won[3] += self.board[i][i]
            for way in won[:2]:
                if way.count("X") == 3 or way.count("O") == 3:
                    flag = True
            if flag:
                break

            won = ["" if won.index(way) < 2 else way for way in won]

            for j in range(3):
                won[0] += self.board[i][j]
                won[1] += self.board[j][i]
                won[2] += self.board[i][j] if (i, j) in dia else ""

        for way in won:
            if way.count(self.player1.mark) == 3:
                return 5
            elif way.count(self.player2.mark) == 3:
                return -5
        return 0


class GameWindow(customtkinter.CTkFrame):
    def __init__(self, master: MainWindow, player1, player2, **kwargs):
        super().__init__(master, **kwargs)

        self.active_player = None
        self.root = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.game_grid = customtkinter.CTkCanvas(self, width=WIDTH, height=CANVAS_HEIGHT, bg="gray20",
                                                 highlightthickness=0)
        self.game_grid.grid(row=2, column=0, columnspan=3, sticky="s", pady=30)

        self.game_grid.create_line(CANVAS_WIDTH / 3, 10, CANVAS_WIDTH / 3, CANVAS_HEIGHT - 20)
        self.game_grid.create_line(CANVAS_WIDTH / 3 * 2, 10, CANVAS_WIDTH / 3 * 2, CANVAS_HEIGHT - 20)
        self.game_grid.create_line(10, CANVAS_HEIGHT / 3, CANVAS_WIDTH - 10, CANVAS_HEIGHT / 3)
        self.game_grid.create_line(10, CANVAS_HEIGHT / 3 * 2, CANVAS_WIDTH - 10, CANVAS_HEIGHT / 3 * 2)

        self.game = Game(player1, player2)

        self.p1 = customtkinter.CTkLabel(self, text=self.game.player1.name,
                                         font=customtkinter.CTkFont(family="Fixedsys", size=30, weight="bold"),
                                         text_color=self.game.player1.color)
        self.p1.grid(row=0, column=0, sticky="w")

        self.score1 = customtkinter.CTkLabel(self, text=self.game.player1.score,
                                             font=customtkinter.CTkFont(family="Arial", size=30, weight="bold"),
                                             text_color=self.game.player1.color)
        self.score1.grid(row=1, column=0, sticky="ew")

        self.p2 = customtkinter.CTkLabel(self, text=self.game.player2.name,
                                         font=customtkinter.CTkFont(family="Fixedsys", size=30, weight="bold"),
                                         text_color=self.game.player2.color)
        self.p2.grid(row=0, column=2, sticky="e")

        self.score2 = customtkinter.CTkLabel(self, text=self.game.player2.score,
                                             font=customtkinter.CTkFont(family="Arial", size=30, weight="bold"),
                                             text_color=self.game.player2.color)
        self.score2.grid(row=1, column=2, sticky="ew")

        self.turn = customtkinter.CTkLabel(self, text="Game Started",
                                           font=customtkinter.CTkFont(family="Fixedsys", size=30, weight="bold"),
                                           text_color="#008080")
        self.turn.grid(row=0, column=1, sticky="ew")

        self.play_game()

    def play_game(self):

        self.game_grid.unbind("<Button-1>")
        if not self.game.is_game_over() and self.game.moves_left():
            if self.game.player1.move:
                self.active_player = self.game.player1
                self.turn.configure(text=f"{self.active_player.name}'s Turn", text_color=self.active_player.color)

            else:
                self.active_player = self.game.player2
                self.game.player1.move = True
                self.turn.configure(text=f"{self.active_player.name}'s Turn", text_color=self.active_player.color)
            self.active_player.make_move(self)
        else:

            if self.game.is_game_over() > 0:
                self.game.player1.score += 1
            elif self.game.is_game_over() < 0:
                self.game.player2.score += 1

            self.score1.configure(text=self.game.player1.score)
            self.score2.configure(text=self.game.player2.score)

            msg = CTkMessagebox(title="Play again?", message="Do you want to play again?",
                                icon="question", option_1="Cancel", option_2="No", option_3="Yes")
            response = msg.get()

            if response == "Yes":
                self.play_again()
            elif response == "No":
                self.destroy()
                self.root.main_window()
            else:
                self.root.destroy()

    def play_again(self):
        self.game.board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]
        self.game_grid.delete("text")
        self.game.empty = True
        self.play_game()

    def check_position(self, event):
        if CANVAS_WIDTH / 3 < event.x < CANVAS_WIDTH / 3 * 2:
            if CANVAS_HEIGHT / 3 < event.y < CANVAS_HEIGHT / 3 * 2:
                self.board_set(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, i=1, j=1)
            elif event.y > CANVAS_HEIGHT / 3 * 2:
                self.board_set(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 1.2, i=2, j=1)
            elif event.y < CANVAS_HEIGHT / 3:
                self.board_set(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 6, i=0, j=1)

        elif event.x < CANVAS_WIDTH / 3:
            if CANVAS_HEIGHT / 3 < event.y < CANVAS_HEIGHT / 3 * 2:
                self.board_set(CANVAS_WIDTH / 6, CANVAS_HEIGHT / 2, i=1, j=0)
            elif event.y > CANVAS_HEIGHT / 3 * 2:
                self.board_set(CANVAS_WIDTH / 6, CANVAS_HEIGHT / 1.2, i=2, j=0)
            elif event.y < CANVAS_HEIGHT / 3:
                self.board_set(CANVAS_WIDTH / 6, CANVAS_HEIGHT / 6, i=0, j=0)

        elif event.x > CANVAS_WIDTH / 3 * 2:
            if CANVAS_HEIGHT / 3 < event.y < CANVAS_HEIGHT / 3 * 2:
                self.board_set(CANVAS_WIDTH / 1.2, CANVAS_HEIGHT / 2, i=1, j=2)
            elif event.y > CANVAS_HEIGHT / 3 * 2:
                self.board_set(CANVAS_WIDTH / 1.2, CANVAS_HEIGHT / 1.2, i=2, j=2)
            elif event.y < CANVAS_HEIGHT / 3:
                self.board_set(CANVAS_WIDTH / 1.2, CANVAS_HEIGHT / 6, i=0, j=2)

    def board_set(self, x, y, i, j):
        if self.game.board[i][j] == "_":
            self.game.board[i][j] = self.active_player.mark

            self.game_grid.create_text(x, y, text=self.active_player.mark,
                                       font=customtkinter.CTkFont(family="Arial", size=80, weight="bold"), tags="text",
                                       fill=self.active_player.color)
            self.active_player.move = False
            self.game.empty = False
            self.game_grid.after(1000, self.play_game)


class Player:

    def __init__(self, name, mark, color):
        self.name = name
        self.mark = mark
        self.move = False
        self.score = 0
        self.color = color

    def make_move(self, window: GameWindow):
        window.game_grid.bind("<Button-1>", window.check_position)


class Bot(Player):
    def __init__(self, name, mark, color, max_min):
        super().__init__(name, mark, color)
        self.infinity = max_min

    def minimax(self, game: Game, max_turn, move):
        score = game.is_game_over()

        if score:
            if self.infinity < 0:
                return score - move
            else:
                return score + move

        if not game.moves_left():
            return 0

        if max_turn:
            best = -100

            for i in range(3):
                for j in range(3):

                    if game.board[i][j] == "_":
                        game.board[i][j] = game.player1.mark

                        best = max(best, self.minimax(game, False, move + 1))

                        game.board[i][j] = "_"
            return best
        else:
            best = 100

            for i in range(3):
                for j in range(3):

                    if game.board[i][j] == "_":
                        game.board[i][j] = game.player2.mark

                        best = min(best, self.minimax(game, True, move + 1))

                        game.board[i][j] = "_"

            return best

    def make_move(self, window: GameWindow):
        least = self.infinity
        cord = [-1, -1]

        if window.game.empty:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            window.board_set(DIRECTIONS[i][j][0], DIRECTIONS[i][j][1], i, j)
            return

        for i in range(3):
            for j in range(3):
                if window.game.board[i][j] == "_":
                    window.game.board[i][j] = self.mark

                    score = self.minimax(window.game, self.infinity > 0, 0)

                    if self.infinity < 0:
                        if score > least:
                            least = score
                            cord = [i, j]
                    else:
                        if score < least:

                            least = score
                            cord = [i, j]

                    window.game.board[i][j] = "_"

        window.board_set(DIRECTIONS[cord[0]][cord[1]][0], DIRECTIONS[cord[0]][cord[1]][1], cord[0], cord[1])


app = MainWindow()

app.mainloop()
