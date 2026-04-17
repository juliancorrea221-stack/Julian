import flet as ft

def main(page: ft.Page):
    page.title = "Mi Portafolio"
    page.scroll = ft.ScrollMode.AUTO


    def proyecto(nombre, imagen_url, descripcion, color_texto):
        return ft.Container(
            content=ft.Column([
                ft.Text(nombre, size=20, weight=ft.FontWeight.BOLD,color=color_texto),
                ft.Image(src=imagen_url, width=300, height=300, fit="cover"),
                ft.Text(descripcion, color=color_texto)
            
            ]),
            padding=10,
            border_radius=10,
            bgcolor=ft.Colors.GREEN,
        )

    page.add(
        ft.Text("Mi Portafolio", size=30, weight=ft.FontWeight.BOLD),
        ft.Text("Estos son mis proyectos:"),
        proyecto(
            "Proyecto 1",
            "perico.png",
            "Mucha comida de pajaros",
            ft.Colors.WHITE
        ),
        proyecto(
            "Proyecto 2",
            "uribista.png",
            "Muy uribista",
            ft.Colors.WHITE
        ),
        proyecto(
            "Perfil",
            "yo.png",
            "odio a los uribistas",
            ft.Colors.WHITE
        )
    )
    

ft.app(target=main, assets_dir="assets")