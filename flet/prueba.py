import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Hola, Julián"))

    input_texto = ft.TextField(label="Escribe algo")
    input_texto2 = ft.TextField(label="Escribe algo")

    resultado1 = ft.Text("")
    resultado2 = ft.Text("")

    def mostrar(e):
        resultado1.value = input_texto.value
        page.update()

    def mostrar2(e):
        resultado2.value = input_texto2.value
        page.update()

    boton = ft.ElevatedButton("Mostrar", on_click=mostrar)
    boton2 = ft.ElevatedButton("Mostrar", on_click=mostrar2)

    page.add(input_texto, boton, resultado1)
    page.add(input_texto2, boton2, resultado2)

ft.app(target=main)
