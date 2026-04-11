from dataclasses import field
import flet as ft


def main(page: ft.Page):
    page.title = "Calc App"

    result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)
    current = ""

    def button_click(e):
        nonlocal current
        text = e.control.content.value

        current += text
        result.value = current
        page.update()

    def clear(e):
        nonlocal current
        current = ""
        result.value = "0"
        page.update()

    def calculate(e):
        nonlocal current
        try:
            current = str(eval(current))
        except:
            current = "Error"

        result.value = current
        page.update()

    # -------- BOTONES --------
    @ft.control
    class CalcButton(ft.ElevatedButton):
        expand: int = field(default_factory=lambda: 1)

    @ft.control
    class DigitButton(CalcButton):
        bgcolor: ft.Colors = ft.Colors.WHITE_24
        color: ft.Colors = ft.Colors.WHITE

    @ft.control
    class ActionButton(CalcButton):
        bgcolor: ft.Colors = ft.Colors.ORANGE
        color: ft.Colors = ft.Colors.WHITE

    @ft.control
    class ExtraActionButton(CalcButton):
        bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
        color: ft.Colors = ft.Colors.BLACK

    # -------- UI --------
    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.BorderRadius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),

                    ft.Row(
                        controls=[
                            ExtraActionButton(content=ft.Text("AC"), on_click=clear),
                            ExtraActionButton(content=ft.Text("+/-")),
                            ExtraActionButton(content=ft.Text("%")),
                            ActionButton(content=ft.Text("/"), on_click=button_click),
                        ]
                    ),

                    ft.Row(
                        controls=[
                            DigitButton(content=ft.Text("7"), on_click=button_click),
                            DigitButton(content=ft.Text("8"), on_click=button_click),
                            DigitButton(content=ft.Text("9"), on_click=button_click),
                            ActionButton(content=ft.Text("*"), on_click=button_click),
                        ]
                    ),

                    ft.Row(
                        controls=[
                            DigitButton(content=ft.Text("4"), on_click=button_click),
                            DigitButton(content=ft.Text("5"), on_click=button_click),
                            DigitButton(content=ft.Text("6"), on_click=button_click),
                            ActionButton(content=ft.Text("-"), on_click=button_click),
                        ]
                    ),

                    ft.Row(
                        controls=[
                            DigitButton(content=ft.Text("1"), on_click=button_click),
                            DigitButton(content=ft.Text("2"), on_click=button_click),
                            DigitButton(content=ft.Text("3"), on_click=button_click),
                            ActionButton(content=ft.Text("+"), on_click=button_click),
                        ]
                    ),

                    ft.Row(
                        controls=[
                            DigitButton(content=ft.Text("0"), expand=2, on_click=button_click),
                            DigitButton(content=ft.Text("."), on_click=button_click),
                            ActionButton(content=ft.Text("="), on_click=calculate),
                        ],
                    ),
                ]
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)