import flet as ft
import random

def main(page: ft.Page):
    page.title = "Ruleta animada"

    nombres = ["Juan", "Ana", "Luis", "Sofia", "Pedro"]
    rotacion_actual = 0

    resultado = ft.Text("Presiona girar", size=20)

    truco = ft.Switch(label="Activar truco")
    input_truco = ft.TextField(label="Forzar resultado")

    ruleta = ft.Container(
        content=ft.Image(
            src="https://i.imgur.com/6o5VZ7C.png",
            width=300,
            height=300,
        ),
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(2000, "easeOut"),
    )

    def girar(e):
        nonlocal rotacion_actual

        # 🔥 decidir ganador
        if truco.value and input_truco.value in nombres:
            ganador = input_truco.value
        else:
            ganador = random.choice(nombres)

        # calcular ángulo correcto
        seccion = 360 / len(nombres)
        indice = nombres.index(ganador)

        # vueltas + posición final
        vueltas = random.randint(5, 8) * 360
        angulo = vueltas + (indice * seccion)

        rotacion_actual += angulo

        # ⚠️ IMPORTANTE: actualizar rotate correctamente
        ruleta.rotate = ft.transform.Rotate(
            angle=rotacion_actual,
            alignment=ft.alignment.center
        )

        resultado.value = f"Ganador: {ganador}"

        page.update()

    boton = ft.ElevatedButton("Girar", on_click=girar)

    page.add(
        ruleta,
        resultado,
        truco,
        input_truco,
        boton
    )

ft.app(target=main)