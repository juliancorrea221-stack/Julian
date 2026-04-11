import flet as ft
import random

CARD_WIDTH = 70
CARD_HEIGHT = 100
CARD_OFFSET = 20
DROP_PROXIMITY = 30

# -------- SLOT --------
class Slot(ft.Container):
    def __init__(self, solitaire, top, left, border=None):
        super().__init__()
        self.solitaire = solitaire
        self.top = top
        self.left = left
        self.width = CARD_WIDTH
        self.height = CARD_HEIGHT
        self.border = border
        self.border_radius = ft.border_radius.all(6)
        self.pile = []
        self.on_click = self.click

    def get_top_card(self):
        if self.pile:
            return self.pile[-1]

    def click(self, e):
        if self == self.solitaire.stock:
            self.solitaire.restart_stock()


# -------- CARD --------
class Card(ft.GestureDetector):
    def __init__(self, solitaire, suite, rank):
        super().__init__()
        self.solitaire = solitaire
        self.suite = suite
        self.rank = rank
        self.face_up = False
        self.slot = None

        self.mouse_cursor = ft.MouseCursor.MOVE
        self.drag_interval = 5
        self.on_pan_start = self.start_drag
        self.on_pan_update = self.drag
        self.on_pan_end = self.drop
        self.on_tap = self.click

        self.content = ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            bgcolor=ft.Colors.GREEN,
            border_radius=ft.border_radius.all(6),
        )

    def turn_face_up(self):
        self.face_up = True
        self.content.bgcolor = ft.Colors.WHITE

    def turn_face_down(self):
        self.face_up = False
        self.content.bgcolor = ft.Colors.GREEN

    def move_on_top(self):
        self.solitaire.controls.remove(self)
        self.solitaire.controls.append(self)

    def place(self, slot):
        if self.slot:
            self.slot.pile.remove(self)

        self.slot = slot
        slot.pile.append(self)

        if slot in self.solitaire.tableau:
            self.top = slot.top + (len(slot.pile) - 1) * CARD_OFFSET
        else:
            self.top = slot.top

        self.left = slot.left

        if self.solitaire.check_win():
            self.solitaire.winning_sequence()

        self.solitaire.update()

    def start_drag(self, e):
        if self.face_up:
            self.move_on_top()

    def drag(self, e):
        if self.face_up:
            self.top += e.delta_y
            self.left += e.delta_x
            self.update()

    def drop(self, e):
        if not self.face_up:
            return

        # Tableau
        for slot in self.solitaire.tableau:
            if (
                abs(self.top - (slot.top + len(slot.pile) * CARD_OFFSET)) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                return

        # Foundations
        for slot in self.solitaire.foundations:
            if (
                abs(self.top - slot.top) < DROP_PROXIMITY
                and abs(self.left - slot.left) < DROP_PROXIMITY
            ):
                self.place(slot)
                return

        self.place(self.slot)

    def click(self, e):
        if self.slot in self.solitaire.tableau:
            if not self.face_up and self == self.slot.get_top_card():
                self.turn_face_up()
                self.solitaire.update()
        elif self.slot == self.solitaire.stock:
            self.move_on_top()
            self.place(self.solitaire.waste)
            self.turn_face_up()


# -------- SOLITAIRE --------
class Solitaire(ft.Stack):
    def __init__(self):
        super().__init__()
        self.controls = []
        self.width = 1000
        self.height = 600

    def did_mount(self):
        self.create_deck()
        self.create_slots()
        self.deal_cards()

    def create_deck(self):
        suites = ["hearts", "diamonds", "clubs", "spades"]
        ranks = list(range(1, 14))

        self.cards = [
            Card(self, s, r)
            for s in suites
            for r in ranks
        ]

    def create_slots(self):
        self.stock = Slot(self, 0, 0, ft.border.all(1))
        self.waste = Slot(self, 0, 100)

        self.foundations = [
            Slot(self, 0, 300 + i * 100, ft.border.all(1))
            for i in range(4)
        ]

        self.tableau = [
            Slot(self, 150, i * 100)
            for i in range(7)
        ]

        self.controls.extend([self.stock, self.waste])
        self.controls.extend(self.foundations)
        self.controls.extend(self.tableau)

    def deal_cards(self):
        random.shuffle(self.cards)
        self.controls.extend(self.cards)

        i = 0
        for col in range(7):
            for row in range(col, 7):
                card = self.cards[i]
                card.place(self.tableau[row])
                i += 1

        for card in self.cards[i:]:
            card.place(self.stock)

        for slot in self.tableau:
            slot.get_top_card().turn_face_up()

        self.update()

    def restart_stock(self):
        while self.waste.pile:
            card = self.waste.get_top_card()
            card.turn_face_down()
            card.place(self.stock)

    def check_win(self):
        return sum(len(f.pile) for f in self.foundations) == 52

    def winning_sequence(self):
        self.controls.append(
            ft.AlertDialog(title=ft.Text("¡Ganaste!"), open=True)
        )


# -------- MAIN --------
def main(page: ft.Page):
    page.title = "Solitaire"
    page.add(Solitaire())


ft.app(target=main)