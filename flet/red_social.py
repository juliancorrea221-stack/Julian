import flet as ft
import random

class red_social:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.title = "Focus routine"
        self.page.theme_mode = ft.ThemeMode.DARK     
        self.page.bgcolor = "black"
        self.color_primaria = "black"
        self.color_secundaria = "green800"
        self.result_api = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        self.grupo_actual = None
        self.grupos_disponibles = [
        {"nombre": "Fitness Hardcore", "miembros": 3, "capacidad": 5},
        {"nombre": "Programadores Python", "miembros": 5, "capacidad": 5},
        {"nombre": "Gamers Colombia", "miembros": 2, "capacidad": 5},
        {"nombre": "Lectura diaria", "miembros": 1, "capacidad": 5},
            ]
        self.usuario = {
        "nombre": "Tú",
        "puntos": 0,
        "retos_completados": 0
        }
        self.retos = [
        {"nombre": "Entrenar 1 hora", "puntos": 10},
        {"nombre": "Leer 20 páginas", "puntos": 5},
        {"nombre": "Despertar 5AM", "puntos": 15},
        ]
        self.ultimo_usuario = None
        self.usuario_en_grupo = False       
        self.mostrar_login()

    def mostrar_login(self):
        self.page.clean()  
        self.page.vertical_alignment = "center"
        self.page.horizontal_alignment = "center"
        self.page.bgcolor = "black"
        self.user_tf = ft.TextField(label="Usuario", width=300, border_color="green", color="white")
        self.pass_tf = ft.TextField(label="Contraseña", password=True, width=300, border_color="green", color="white")

        def validar(e):
            if self.user_tf.value == "uribista" and self.pass_tf.value == "premium":
                self.page.vertical_alignment = "start" 
                self.page.horizontal_alignment = "start"
                self.page.clean()
                self.build_ui()
            else:
                self.page.snack_bar = ft.SnackBar(ft.Text("Usuario o clave incorrectos"))
                self.page.snack_bar.open = True
                self.page.update()

        # Agregamos los controles directamente a la página
        self.page.add(
            ft.Text("Focus Routine", size=40, weight="bold", color="green"),
            ft.Text("Inicia sesión para continuar", color="white"),
            self.user_tf,
            self.pass_tf,
            ft.ElevatedButton("Entrar", on_click=validar, bgcolor="green800", color="white"),
             
        )
        self.page.update()

    def abrir_nueva_ventana(self, e):
        self.page.clean() 
        self.page.vertical_alignment = "start"
        self.page.horizontal_alignment = "start" 
        barra_superior = ft.Container(
            padding=15,
            bgcolor=self.color_secundaria,
            content=ft.Row([
                ft.Text("Información del Proyecto", color="white", weight="bold", size=20),
            ], alignment="spaceBetween")
        )
        self.page.add(
            ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    barra_superior,
                    ft.Container(    
                        padding=20,
                        content=ft.Column([
                            ft.Text("Información", size=40, color="green", weight="bold"),
                            ft.Text("Creador proyecto:", size=30, color="white"),
                            ft.Container(
                                # Asegúrate de que "yo.png" esté en la misma carpeta
                                content=ft.Image(src="yo.png", border_radius=20, fit="cover"), 
                                height=400
                            ),
                            ft.Text("Julian Fernando Correa Cardozo", size=30, color="white"),
                            ft.ElevatedButton("Volver", on_click=lambda _: self.volver_inicio()) 
                        ], scroll=ft.ScrollMode.AUTO)
                    )
                ]
            )
        )
        self.page.update()

    def volver_inicio(self):
        self.page.clean()
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
                        ft.Text("Interfaz", color="white", weight="bold", size=20),
                        ft.Row([
                            ft.TextButton("Inicio", on_click=lambda _: self.cambiar_pagina(0), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Retos", on_click=lambda _: self.cambiar_pagina(1), style=ft.ButtonStyle(color="white")),
                            ft.TextButton("Grupos", on_click=lambda _: self.cambiar_pagina(2), style=ft.ButtonStyle(color="white")),
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
        self.page.update() 
    
    def build_inicio(self):
        return ft.Column([
            ft.Text("Bienvenido a Focus Routine", size=30, weight="bold", color="white"),
            ft.Row([ft.Image(src="uribista.png", width=60), ft.Text("Contenido principal cargado.", size=18, color="white")]),
        ], spacing=20)

    def build_retos(self):
        lista = ft.Column()

        def completar(reto):
            self.usuario["puntos"] += reto["puntos"]
            self.usuario["retos_completados"] += 1
            self.page.snack_bar = ft.SnackBar(
                ft.Text(f"+{reto['puntos']} puntos")
            )
            self.page.snack_bar.open = True
            self.page.update()
        for reto in self.retos:
            lista.controls.append(
                ft.Row([
                    ft.Text(reto["nombre"], color="white"),
                    ft.ElevatedButton(
                        "Completar",
                        on_click=lambda e, r=reto: completar(r),
                        bgcolor="green"
                    )
                ], alignment="spaceBetween")
            )
        return ft.Column([
            ft.Text("Retos diarios", size=30, color="white"),
            lista
        ])

    def build_grupos(self):
        self.lista_grupos = ft.Column()

        def buscar(e):
            texto = self.buscador.value.lower()
            self.lista_grupos.controls.clear()
            for grupo in self.grupos_disponibles:
                if texto in grupo["nombre"].lower():

                    lleno = grupo["miembros"] >= grupo["capacidad"]

                    self.lista_grupos.controls.append(
                        ft.Row([
                            ft.Column([
                                ft.Text(grupo["nombre"], color="white"),
                                ft.Text(
                                    f'{grupo["miembros"]}/{grupo["capacidad"]} miembros',
                                    color="white",
                                    size=12
                                )
                            ]),
                            ft.ElevatedButton(
                                "Lleno" if lleno else "Unirse",
                                disabled=lleno,
                                bgcolor="grey" if lleno else "green",
                                on_click=lambda e, g=grupo: unirse(g)
                            )
                        ], alignment="spaceBetween")
                    )
            self.page.update()

        def unirse(grupo):
            if self.usuario_en_grupo:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Ya estás en un grupo")
                )
                self.page.snack_bar.open = True
                self.page.update()
                return
            if grupo["miembros"] < grupo["capacidad"]:
                grupo["miembros"] += 1
                self.grupo_actual = grupo
                self.usuario_en_grupo = True

                self.page.snack_bar = ft.SnackBar(
                    ft.Text(f"Entraste a {grupo['nombre']}")
                )
                self.page.snack_bar.open = True

                self.abrir_chat_grupo()
            else:
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Este grupo ya está lleno")
                )
                self.page.snack_bar.open = True
            self.page.update()
        self.buscador = ft.TextField(
            label="Buscar grupos",
            border_color="green",
            color="white",
            on_change=buscar
        )
        return ft.Column([
            ft.Text("Gremios", size=30, weight="bold", color="white"),
            self.buscador,
            self.lista_grupos
        ], spacing=20)
    
    def abrir_chat_grupo(self):
        self.page.clean()
        ranking = ft.Column()
        def salir_grupo(e):
            if self.grupo_actual:
                self.grupo_actual["miembros"] -= 1
                self.usuario_en_grupo = False
                self.grupo_actual = None
            self.volver_inicio()
        def actualizar_ranking():
            ranking.controls.clear()
            jugadores = [
                {"nombre": "Ana", "puntos": 30},
                {"nombre": "Luis", "puntos": 20},
                self.usuario
            ]
            jugadores_ordenados = sorted(jugadores, key=lambda x: x["puntos"], reverse=True)
            for i, j in enumerate(jugadores_ordenados):
                ranking.controls.append(
                    ft.Text(f"{i+1}. {j['nombre']} - {j['puntos']} pts", color="white")
                )
        mensajes = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
        input_mensaje = ft.TextField(
            hint_text="Escribe un mensaje...",
            expand=True,
            color="white"
        )

        def enviar(e):
         if input_mensaje.value.strip() != "":
            texto = input_mensaje.value
            mensajes.controls.append(
                ft.Text(f"Tú: {texto}", color="white")
            )
            input_mensaje.value = ""
            usuarios=[
                "Ana",
                "Luis",
                "Eduardo"
            ]
            respuestas_por_usuario = {
                "Ana": ["Buen progreso 🔥", "Vas muy bien 💪", "Sigue así"],
                "Luis": ["Disciplina 💯", "No pares", "Concéntrate"],
                "Eduardo": ["Vamos fuerte 💪", "Hoy toca duro 🔥", "Actitud"]
            }
            usuario = random.choice(usuarios)
            respuesta = random.choice(respuestas_por_usuario[usuario])
            self.ultimo_usuario = usuario
            mensajes.controls.append(
                ft.Text(f"{usuario}: {respuesta}", color="green")
            )
            actualizar_ranking()
            self.page.update()
        self.page.add(
            ft.Column([
                ft.Container(
                    padding=15,
                    bgcolor=self.color_secundaria,
                    content=ft.Row([
                        ft.Text(self.grupo_actual["nombre"], color="white", size=20),
                        ft.TextButton("Salir",on_click=salir_grupo,style=ft.ButtonStyle(color="white"))
                    ], alignment="spaceBetween")
                ),
                ft.Text("Ranking del grupo", color="green", size=18),
                ranking, 
                ft.Divider(color="white"),
                mensajes,
                ft.Row([
                    input_mensaje,
                    ft.IconButton(
                        icon=ft.Icons.SEND,
                        on_click=enviar,
                        icon_color="green"
                    )
                ])
            ], expand=True)
        )
        actualizar_ranking()      
        self.page.update()

    def build_perfil(self):
        return ft.Column([
            ft.Text("Perfil", size=30, weight="bold", color="white"),
            ft.ElevatedButton("Créditos", on_click=self.abrir_nueva_ventana),
            ft.ElevatedButton("Cerrar Sesión", on_click=lambda _: self.mostrar_login(), color="red")
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
    page.window.icon = "logo.ico"  
ft.app(target=main)