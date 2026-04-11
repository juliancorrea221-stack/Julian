from dataclasses import dataclass
import flet as ft


@dataclass
class Message:
    user_name: str
    text: str
    message_type: str


@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.message = message

        # 👇 condición: quién envía el mensaje
        is_user = self.message.user_name == "Julian"

        self.alignment = (
            ft.MainAxisAlignment.END if is_user else ft.MainAxisAlignment.START
        )

        self.controls = [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            self.message.user_name,
                            weight=ft.FontWeight.BOLD,
                            size=12,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Text(self.message.text, color=ft.Colors.WHITE),
                    ],
                    tight=True,
                    spacing=5,
                ),
                bgcolor=ft.Colors.BLUE if is_user else ft.Colors.GREY_800,
                padding=10,
                border_radius=10,
            )
        ]
    def get_initials(self, user_name: str):
        return user_name[:1].capitalize() if user_name else "?"

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.Colors.AMBER, ft.Colors.BLUE, ft.Colors.BROWN, ft.Colors.CYAN,
            ft.Colors.GREEN, ft.Colors.INDIGO, ft.Colors.LIME, ft.Colors.ORANGE,
            ft.Colors.PINK, ft.Colors.PURPLE, ft.Colors.RED, ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat"


    async def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    user_selector.value,  # 👈 AQUÍ eliges quién habla
                    new_message.value,
                    message_type="chat_message",
                    
                )
            )
            new_message.value = ""
            await new_message.focus()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        else:
            m = ft.Text(message.text, italic=True, size=12)

        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # 🔹 CHAT
    chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    # 🔹 INPUT MENSAJE
    new_message = ft.TextField(
        hint_text="Write a message...",
        expand=True,
        on_submit=send_message_click,
    )

    # 🔥 SELECTOR DE USUARIO
    user_selector = ft.Dropdown(
        options=[
            ft.dropdown.Option("Colvin"),
            ft.dropdown.Option("Carlos"),
            ft.dropdown.Option("Julian"),
            ft.dropdown.Option("Almanza")
        ],
        value="Julian",
        width=120,
    )

    # 🔹 UI FINAL
    page.add(
        ft.Container(
            content=chat,
            border=ft.Border.all(1),
            padding=10,
            expand=True,
        ),
        ft.Row(
            controls=[
                user_selector,  # 👈 selector aquí
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND,
                    on_click=send_message_click,
                ),
            ]
        ),
    )


ft.run(main)