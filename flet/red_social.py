import flet as ft

class red_social:
    def __init__(self,page:ft.page):
        self.page = page
        self.page.padding = 0
        self.page.title = "Focus routine"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        
        self.page.bgcolor = "black"
        self.color_primaria = "black"
        self.color_secundaria = "green800"
        self.result_api = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.build_ui()

    def build_ui(self):
       
        self.frame_inicio = ft.Container(expand=True, padding=20, visible=True, content=self.build_inicio())
        self.frame_retos = ft.Container(expand=True, padding=20, visible=False, content=self.build_retos())
        self.frame_grupos = ft.Container(expand=True, padding=20, visible=False, content=self.build_grupos())
        self.frame_perfil = ft.Container(expand=True, padding=20, visible=False, content=self.build_perfil())
        layout = ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    padding=15,
                    bgcolor=self.color_secundaria,
                    content=ft.Row([
                        ft.Text("Intefaz", color="white", weight="bold", size=20),
                        ft.Row([
                            ft.TextButton("Inicio", on_click=lambda _: self.cambiar_pagina(0), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Retos", on_click=lambda _: self.cambiar_pagina(1), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Grupos de apoyo", on_click=lambda _: self.cambiar_pagina(2), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Perfil", on_click=lambda _: self.cambiar_pagina(3), style=ft.ButtonStyle(color="white")),
                        ]),
                    ], alignment="spaceBetween")
                ),
                ft.Container(
                    expand=True,
                    content=ft.Stack([
                        self.frame_inicio,
                        self.frame_retos,
                        self.frame_grupos,
                        self.frame_perfil,

                    ])
                )
            ]
        )
        self.page.add(layout)
    
    def build_inicio(self):
        return ft.Column([
            ft.Text("Bienvenido a Focus Routine", size=30, weight="bold", color="white"),
            ft.Row([ft.Image(src="uribista.png", width=60), ft.Text("El uribista mas grande de toda la historia de colombia", size=18, color="white")]),
        ],spacing=20)

    def build_retos(self):
        return ft.Column([
            ft.Text("Desafios", size=30, weight="bold", color="white")
            ])
    def build_grupos(self):
        return ft.Column([
            ft.Text("Gremios", size=30, weight="bold", color="white")
            ])
    def build_perfil(self):
        return ft.Column([
            ft.Text("Perfil", size=30, weight="bold", color="white")
            ])
    
    def cambiar_pagina(self, index):
        self.frame_inicio.visible = (index == 0)
        self.frame_retos.visible = (index == 1)
        self.frame_grupos.visible = (index == 2)
        self.frame_perfil.visible = (index == 3)
        self.page.update()


def main(page: ft.Page):
    red_social(page)
    page.scroll = ft.ScrollMode.AUTO
    
ft.app(target=main)

