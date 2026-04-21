import flet as ft
import webbrowser
import requests
import re

class PortafolioWeb:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.title = "Mi Portafolio Profesional"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        
        self.page.bgcolor = "bluegrey600"
        self.color_primaria = "black"
        self.color_secundaria = "black"
        
        # Contenedor para los resultados de la API
        self.result_api = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.build_ui()

    def build_ui(self):
        # Restauramos todos los frames
        self.frame_inicio = ft.Container(expand=True, padding=20, visible=True, content=self.build_inicio())
        self.frame_servicio = ft.Container(expand=True, padding=20, visible=False, content=self.build_servicio())
        self.frame_resumen = ft.Container(expand=True, padding=20, visible=False, content=self.build_resumen())
        self.frame_api = ft.Container(expand=True, padding=20, visible=False, content=self.build_api())

        layout = ft.Column(
            expand=True,
            spacing=0,
            controls=[
                # Barra de Navegación superior
                ft.Container(
                    padding=15,
                    bgcolor=self.color_secundaria,
                    content=ft.Row([
                        ft.Text("PORTAFOLIO", color="white", weight="bold", size=20),
                        ft.Row([
                            ft.TextButton("Inicio", on_click=lambda _: self.cambiar_pagina(0), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Servicios", on_click=lambda _: self.cambiar_pagina(1), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Resumen", on_click=lambda _: self.cambiar_pagina(2), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Api", on_click=lambda _: self.cambiar_pagina(3), style=ft.ButtonStyle(color="white")),
                        ]),
                    ], alignment="spaceBetween")
                ),
                ft.Container(
                    expand=True,
                    content=ft.Stack([
                        self.frame_inicio,
                        self.frame_servicio,
                        self.frame_resumen,
                        self.frame_api,
                    ])
                )
            ]
        )
        self.page.add(layout)

    def build_inicio(self):
        def abrir_github(e):
             webbrowser.open_new_tab("https://github.com/juliancorrea221-stack/Julian")
        
        return ft.ResponsiveRow([
            ft.Column([
                ft.Text("Hola, soy Julian Fernando Correa Cardozo", size=45, weight="bold", color=self.color_secundaria),
                ft.Text("Persona de ing de software en formación, responsable, puntual y buena convivencia en el trabajo en equipo", size=20, color="black"),
                ft.Row([ft.Image(src="gmail.svg", width=40), ft.Text("Correo: juliancorrea221@gmail.com", size=20, color="black")]),
                ft.Row([ft.Image(src="telefono.svg", width=40), ft.Text("Numero: 3158399438", size=20, color="black")]),
                ft.ElevatedButton("Entrar al Github", bgcolor=self.color_primaria, color="white", on_click=abrir_github)
            ], col={"md": 8.2}, alignment="center"),
            ft.Container(content=ft.Image(src="yo.png", border_radius=20, fit="cover"), col={"md": 3}, height=400)
        ], vertical_alignment="center")

    def build_servicio(self):
        t1, self.bar_html = self.crear_tarjeta("Diseño Web", "html5.svg", 0.25) 
        t2, self.bar_python = self.crear_tarjeta("Python", "python.svg", 0.6)  
        t3, self.bar_git = self.crear_tarjeta("Repositorios git", "github.png", 0.65) 

        return ft.Column([
            ft.Text("Mis Servicios", size=35, weight="bold", color="white"),
            ft.ResponsiveRow([t1, t2, t3]),
            ft.ElevatedButton("Ver inicio", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(0)),
        ], scroll="auto")

    def build_resumen(self):
        # Recuperamos tu resumen con iconos
        return ft.Column([
            ft.Text("Mi Resumen", size=35, weight="bold", color="white"),
            ft.Row([ft.Image(src="flet.svg", width=40), ft.Image(src="tkinter.svg", width=25), ft.Text("Crear interfaces gráficas en python con Flet y Tkinter.", size=18, color="white")]),
            ft.Row([ft.Image(src="algoritmo.png", width=40), ft.Text("Comprendimiento de los algoritmos", size=18, color="white")]),
            ft.Row([ft.Image(src="html5.svg", width=40), ft.Image(src="github.png", width=40), ft.Text("Gestión de versiones", size=18, color="white")]),
            ft.ElevatedButton("Ver servicios", bgcolor=self.color_primaria, color="white", on_click=lambda _: self.cambiar_pagina(1)),
        ], spacing=20)

    def build_api(self):
        self.input_search = ft.TextField(label="Personaje de Hollow Knight", hint_text="Hornet, Grimm...", width=400, on_submit=self.fetch_wiki_data)
        return ft.Column([
            ft.Text("API Hollow knight🐜", size=35, weight="bold", color="white"),
            ft.Row([self.input_search, ft.ElevatedButton("Buscar", icon="SEARCH", on_click=self.fetch_wiki_data)], alignment="center"),
            ft.Divider(),
            self.result_api 
        ], horizontal_alignment="center", scroll="auto")

    def fetch_wiki_data(self, e):
        self.result_api.controls.clear()
        self.page.update()
        query = self.input_search.value.strip()
        if not query: return
        url = "https://hollowknight.fandom.com/api.php"
        params = {"action": "query", "format": "json", "titles": query, "prop": "revisions|pageimages", "rvprop": "content", "pithumbsize": 500, "redirects": 1}
        try:
            res = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
            data = res.json()
            pages = data.get("query", {}).get("pages", {})
            page_id = next(iter(pages))
            if page_id == "-1":
                self.result_api.controls.append(ft.Text("❌ No encontrado", color="red"))
            else:
                content = pages[page_id]
                raw_text = content.get("revisions", [{}])[0].get("*", "")
                clean = re.sub(r'\{\{.*?\}\}', '', raw_text, flags=re.DOTALL)
                clean = re.sub(r'<.*?>', '', clean, flags=re.DOTALL)
                clean = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', clean)
                paragraphs = [p.strip() for p in clean.split('\n') if len(p.strip()) > 40 and "youtu" not in p]
                desc = paragraphs[0] if paragraphs else "Sin descripción."
                img = content.get("thumbnail", {}).get("source")
                self.result_api.controls.append(ft.Text(content.get("title"), size=30, color="amber", weight="bold"))
                if img: self.result_api.controls.append(ft.Image(src=img, width=250, border_radius=10))
                self.result_api.controls.append(ft.Container(content=ft.Text(desc, text_align="justify", color="white", size=16), padding=20, bgcolor="black", border_radius=15, width=550))
        except Exception as ex:
            self.result_api.controls.append(ft.Text(f"Error: {ex}", color="red"))
        self.page.update()

    def crear_tarjeta(self, titulo, img_src, porcentaje):
        # Creamos la barra con ancho inicial 0 para la animación
        barra_progreso = ft.Container(
            content=ft.Text(f"{int(porcentaje*100)}%", size=10, color="white", weight="bold"),
            bgcolor="blue",
            width=0, 
            height=15,
            border_radius=5,
            alignment=ft.Alignment(0, 0),
            animate_size=1000, # <--- CAMBIADO AQUÍ
        )
        
        tarjeta = ft.Container(
            content=ft.Column([
                ft.Image(src=img_src, width=50, height=50),
                ft.Text(titulo, weight="bold"),
                ft.Container( # Fondo de la barra
                    content=barra_progreso,
                    bgcolor="grey300",
                    width=200,
                    height=15,
                    border_radius=5,
                )
            ], horizontal_alignment="center"),
            bgcolor="bluegrey50", padding=20, border_radius=10, col={"sm": 4}
        )
        return tarjeta, barra_progreso

    def cambiar_pagina(self, index):
        self.frame_inicio.visible = (index == 0)
        self.frame_servicio.visible = (index == 1)
        self.frame_resumen.visible = (index == 2)
        self.frame_api.visible = (index == 3)
        
        self.page.update()
def main(page: ft.Page):
    PortafolioWeb(page)
    page.scroll = ft.ScrollMode.AUTO

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")