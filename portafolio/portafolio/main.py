import flet as ft

class PortafolioWeb:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.title = "Mi Portafolio Profesional"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        
        
        self.page.bgcolor = "bluegrey600"
        self.color_primaria = "black"
        self.color_secundaria = "black"
        
        self.build_ui()

    def build_ui(self):
        self.cambiar_modo = ft.IconButton(
            icon="dark_mode",
            bgcolor=self.color_primaria,
            icon_color="white",
            on_click=self.cambiar_modo_oscuro,
        )

  
        self.frame_inicio = ft.Container(
            expand=True,
            padding=20,
            visible=True,
            content=self.build_inicio(),
        )

        self.frame_servicio = ft.Container(
            expand=True,
            padding=20,
            visible=False,
            content=self.build_servicio(),
        )

        self.frame_resumen = ft.Container(
            expand=True,
            padding=20,
            visible=False,
            content=self.build_resumen(),
        )

     
        layout = ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    padding=15,
                    bgcolor=self.color_secundaria,
                    content=ft.Row([
                        ft.Text("PORTAFOLIO", color="white", weight="bold", size=20),
                        ft.Row([
                            ft.TextButton("Inicio", on_click=lambda _: self.cambiar_pagina(0), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Servicios", on_click=lambda _: self.cambiar_pagina(1), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Resumen", on_click=lambda _: self.cambiar_pagina(2), style=ft.ButtonStyle(color="white")),
                        ]),
        
                    ], alignment="spaceBetween")
                ),
                ft.Container(
                    expand=True,
                    content=ft.Stack([
                        self.frame_inicio,
                        self.frame_servicio,
                        self.frame_resumen,
                    ])
                )
            ]
        )
        self.page.add(layout)

    def build_inicio(self):
        return ft.ResponsiveRow([
            ft.Column([
                ft.Text("Hola, soy ingeniero de software en formacion", size=45, weight="bold", color=self.color_secundaria),
                ft.Text("Bienvenido a mi espacio de proyectos.", size=20, color="black"),
                ft.ElevatedButton("Ver servicios", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(1)),
                ft.ElevatedButton("Ver resumen", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(2))
            ], col={"md": 8.2}, alignment="center"),
            ft.Container(
                content=ft.Image(src="yo.png", border_radius=20, fit="cover"),
                col={"md": 3},
                height=400
                
            )
        ], vertical_alignment="center")

    def build_servicio(self):
        return ft.Column([
            ft.Text("Mis Servicios", size=35, weight="bold",color="white"),
            ft.ResponsiveRow([
                self.crear_tarjeta("Diseño Web", "html5.svg"),
                self.crear_tarjeta("Python", "python.svg"),
                self.crear_tarjeta("Repositorios git", "github.png"),    
            ]),
            ft.ElevatedButton("Ver inicio", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(0)),
                ft.ElevatedButton("Ver resumen", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(2))
        ], scroll="auto")

    def build_resumen(self):
        return ft.Column([
            ft.Text("Mi Resumen", size=35, weight="bold",color="white"),
            ft.Row([
                ft.Image(src="flet.svg", width=40),
                ft.Image(src="tkinter.svg", width=25),
                ft.Text("Crear interfaces gráficas en python con Flet y Tkinter.", size=18,color="white")
            ]),
            ft.Row([
                ft.Image(src="algoritmo.png", width=40),
                ft.Text("Comprendimiento de los algoritmos", size=18,color="white")
            ]),
            ft.Row([
                ft.Image(src="html5.svg", width=40),
                ft.Image(src="github.png", width=40),
                ft.Text("Gestión de versiones", size=18,color="white"),             
            ]),
             ft.ElevatedButton("Ver servicios", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(1)),
             ft.ElevatedButton("Ver inicio", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(0))
        ], spacing=20)

    def crear_tarjeta(self, titulo, img_src):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=img_src, width=50, height=50),
                ft.Text(titulo, weight="bold")
            ], horizontal_alignment="center"),
            bgcolor="bluegrey50",
            padding=20,
            border_radius=10,
            col={"sm": 4}
        )

    def cambiar_pagina(self, index):
        self.frame_inicio.visible = (index == 0)
        self.frame_servicio.visible = (index == 1)
        self.frame_resumen.visible = (index == 2)
        self.page.update()

    def cambiar_modo_oscuro(self, e):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.cambiar_modo.icon = "dark_mode"
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
            self.cambiar_modo.icon = "light_mode"
        self.page.update()

def main(page: ft.Page):
    PortafolioWeb(page)
    page.scroll = ft.ScrollMode.AUTO

if __name__ == "__main__":
   
    ft.app(target=main, assets_dir="assets")