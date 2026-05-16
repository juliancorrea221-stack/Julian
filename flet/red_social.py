import flet as ft
import random
import webbrowser
import requests
import re

class red_social:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.padding = 0
        self.page.title = "Focus routine"
        self.page.theme_mode = ft.ThemeMode.DARK     
        self.page.bgcolor = "black"
        self.color_primaria = "black"
        self.color_secundaria = "green800"
        self.usuarios = {
            "1": "2"
        }
        self.result_creditos = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)
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

        self.user_tf = ft.TextField(
            label="Usuario",
            width=300,
            border_color="green",
            color="white"
        )

        self.pass_tf = ft.TextField(
            label="Contraseña",
            password=True,
            width=300,
            border_color="green",
            color="white"
        )

        def validar(e):
            usuario = self.user_tf.value
            clave = self.pass_tf.value
            
            if usuario in self.usuarios and self.usuarios[usuario] == clave:

                self.page.vertical_alignment = "start"
                self.page.horizontal_alignment = "start"

                self.page.clean()

                self.build_ui()

        def ir_registro(e):
            self.mostrar_registro()

        self.page.add(
            ft.Text(
                "Focus Routine",
                size=40,
                weight="bold",
                color="green"
            ),

            ft.Text(
                "Inicia sesión para continuar",
                color="white"
            ),

            self.user_tf,
            self.pass_tf,

            ft.ElevatedButton(
                "Entrar",
                on_click=validar,
                bgcolor="green",
                color="white"
            ),

            ft.ElevatedButton(
                "Crear cuenta",color="white",bgcolor="green",
                on_click=ir_registro
            )
        )

        self.page.update()

    def mostrar_registro(self):
        self.page.clean()

        nuevo_user = ft.TextField(
            label="Nuevo usuario",color="white",border_color="green",
            width=300
        )

        nueva_pass = ft.TextField(
            label="Nueva contraseña",color="white",border_color="green",
            password=True,
            width=300
        )

        def crear_cuenta(e):
            usuario = nuevo_user.value
            clave = nueva_pass.value

            if usuario in self.usuarios:

                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Ese usuario ya existe")
                )

            else:
                self.usuarios[usuario] = clave

                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Cuenta creada correctamente")
                )

                self.mostrar_login()

            self.page.snack_bar.open = True
            self.page.update()

        self.page.add(
            ft.Text(
                "Crear Cuenta",color="green400",
                size=30
            ),

            nuevo_user,
            nueva_pass,

            ft.ElevatedButton(
                "Registrarse",color="white",bgcolor="green",
                on_click=crear_cuenta
            )
        )

        self.page.update()
    def abrir_nueva_ventana(self, e):
        self.page.clean()
        self.info_inicio = ft.Container(visible=True, content=self.inicio())
        self.info_justificacion = ft.Container(visible=False, content=self.justificacion())
        self.info_objetivos = ft.Container(visible=False, content=self.objetivos())
        self.info_creditos = ft.Container(visible=False, content=self.creditos())
        def cambiar_info(index):
            self.info_inicio.visible = (index == 0)
            self.info_justificacion.visible = (index == 1)
            self.info_objetivos.visible = (index == 2)
            self.info_creditos.visible = (index == 3)
            self.page.update()

        barra_superior = ft.Container(
        padding=15,
        bgcolor=self.color_secundaria,
        expand=True,  
        content=ft.Row(
            [
                ft.Text("Información del Proyecto", color="white", size=20),

                ft.Row(  
                    [
                        ft.TextButton("Inicio", on_click=lambda _: cambiar_info(0), style=ft.ButtonStyle(color="white")),
                        ft.TextButton("Justificación", on_click=lambda _: cambiar_info(1), style=ft.ButtonStyle(color="white")),
                        ft.TextButton("Objetivos", on_click=lambda _: cambiar_info(2), style=ft.ButtonStyle(color="white")),
                        ft.TextButton("Creditos", on_click=lambda _: cambiar_info(3), style=ft.ButtonStyle(color="white")),
                        ft.TextButton("Volver", on_click=lambda _: self.volver_inicio(), style=ft.ButtonStyle(color="white")),
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN 
            )
        )
        self.page.add(
            ft.Column(
                expand=True,
                controls=[
                    barra_superior,
                    self.info_inicio,
                    self.info_justificacion,
                    self.info_objetivos,
                    self.info_creditos,
                ]
            )
        )
        self.page.update()
    def inicio(self):
        def abrir_github(e):
             webbrowser.open_new_tab("https://github.com/juliancorrea221-stack/Julian")
        
        return ft.ResponsiveRow([
            ft.Column([
                ft.Text("Sistema de gestión de grupos y disciplina", size=45, weight="bold", color="green400"),
                ft.Text("Introducción", size=20, color="green400"),
                ft.Text("Actualmente muchos jóvenes les cuesta mas trabajo mentalmente para desarrollar disciplina" \
                "con lo que  desarrollare una aplicación tipo red social donde habran grupos en lo que tendran en comun"\
                "lo que al abarcarse en un entorno positivo dara una emoción de competencia en la que comentaran y"\
                "subira evidencias para recibir consejos o mensajes positivos, ayudando a largo plazo en un entorno mas adecuado", size=20, color="white"),
                ft.Text("Problemática", size=20, color="green400"),
                ft.Text("Teniendo en cuenta el anterior contexto,Las plataformas digitales existentes no están diseñadas específicamente para fomentar disciplina"\
                        " mediante reglas obligatorias. No existe un sistema estructurado donde:"\
                        "-Se establezcan compromisos periódicos."\
                        "-Se controle el cumplimiento."\
                        "-Se generen penalizaciones por inactividad."\
                        "-Se fomente la competencia saludable dentro de reglas claras."\
                        "Por lo tanto, se plantea el desarrollo de un sistema que permita crear grupos donde los participantes deban subir evidencias"\
                        "de progreso en intervalos definidos", size=20, color="white"),
                ft.ElevatedButton("Entrar al Github", bgcolor="green", color="white", on_click=abrir_github),
            ], col={"md": 8.2}, alignment="center"),
        ], vertical_alignment="center")

    def justificacion(self):
        def abrir_fuentes(e):
            webbrowser.open_new_tab("https://revistas.utb.edu.ec/index.php/magazine/article/view/3671/3325")
        return ft.ResponsiveRow([
            ft.Column([
            ft.Text("Justificación", size=35, weight="bold", color="green400"),
            ft.Text("Se propone el desarrollo de un sistema que permita crear grupos con reglas definidas, donde los miembros deban cumplir con publicaciones periódicas como evidencia de avance."
            "Este proyecto se justifica académicamente porque:"
            "-Permite aplicar Programación Orientada a Objetos mediante la creación de clases como Usuario, Grupo, Reto y Publicación."
            "-Requiere organización por módulos para estructurar correctamente el sistema."
            "-Implementa una interfaz gráfica mediante Flet."
            "-Integra validaciones, estructuras de datos y lógica condicional compleja."
            "-Simula un sistema real con reglas dinámicas y seguimiento."
            ,size=25, weight="bold", color="white"),
            ft.Text("Antecedentes", size=35, weight="bold", color="green400"),
            ft.Text("según (González, 2024) que tuvieron aumentos constantes de uso por medio de Angular y Ionic, fomentando a aumentar el desarrollo de buenos hábitos," \
            " esto visto como los sistemas de videojuegos logros, recompensas, desafíos donde muchos  son atraídos por esta práctica atractiva, por lo que ahora se dará en"\
            "un enfoque más beneficioso a largo plazo que solo diversión pura afectando positivamente si se aplica desde un punto tecnológico, psicológica y metodológica.", size=25, weight="bold", color="white"),
            ft.Container(content=ft.Image(src="antecedentes.png", border_radius=20, fit="cover"), col={"md": 3}, height=400),
            ft.ElevatedButton("Fuentes", bgcolor="green", color="white", on_click=abrir_fuentes)],col={"md": 8.2}, alignment="center"),
            ft.ElevatedButton("Ver inicio", bgcolor="green", color="white", on_click=lambda _: self.cambiar_pagina(0)),
        ], scroll="auto")
    
    
    def objetivos(self):
        return ft.Column([
            ft.Text("Objetivos", size=35, weight="bold", color="green400"),
            ft.Text("Objetivo general",size=25, weight="bold", color="green400"),
            ft.Text("Desarrollar un sistema de escritorio que permita la gestión de grupos de disciplina y retos, promoviendo la constancia"
            "mediante reglas obligatorias de cumplimiento y seguimiento de progreso.",size=25, weight="bold", color="white"),
            ft.Text("Objetivos específicos",size=25, weight="bold", color="green400"),
            ft.Text("-Diseñar una estructura basada en Programación Orientada a Objetos.",size=25, weight="bold", color="white"),
            ft.Text("- Implementar una interfaz gráfica funcional utilizando Flet.",size=25, weight="bold", color="white"),
            ft.Text("- Organizar las funciones independientes para mejorar la estructura del código.", size=25, weight="bold", color="white"),
            ft.Row([ft.Image(src="flet.svg", width=40,color="white"), ft.Image(src="tkinter.svg", width=25,color="white"), ft.Text("Crear interfaces gráficas en python con Flet y Tkinter.", size=18, color="white")]),
            ft.Row([ft.Image(src="algoritmo.png", width=40,color="white"), ft.Text("Comprendimiento de los algoritmos", size=18, color="white")]),
            ft.Row([ft.Image(src="html5.svg", width=40,color="white"), ft.Image(src="github.png", width=40), ft.Text("Gestión de versiones", size=18, color="white")]),
            ft.ElevatedButton("Ver justificación", bgcolor="green", color="white", on_click=lambda _: self.cambiar_pagina(1)),
        ], spacing=20)
    def creditos(self):
        return ft.Column([
           ft.Text("Creditos", size=35,weight="bold", color="green400"),
           ft.Text("Julian Fernando Correa Cardozo", size=25,weight="bold", color="green400"),
           ft.Container(content=ft.Image(src="yo.png", border_radius=20, fit="cover"), col={"md": 3}, height=400),
           ft.Row([ft.Image(src="gmail.svg", width=40,color="green"), ft.Text("Correo: juliancorrea221@gmail.com", size=20, color="white")]),
           ft.Row([ft.Image(src="telefono.svg", width=40,color="green"), ft.Text("Numero: 3158399438", size=20, color="white")])
        ], horizontal_alignment="center", scroll="auto")



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
            ft.Text("Bienvenido a Focus Routine", size=30, weight="bold", color="green400"),
            ft.Text("Se trata de una de un programa donde simula una experiencia"\
            "de una red social, tiene algunos conceptos como unirse a un grupo,"\
            "iniciar/cerrar sesión, crear un usuario y contraseña, creditos, actualmente"\
            "es solamente un protipo basico de lo que se espera de una red social real", size=25, weight="bold", color="white"),
            ft.Row([ft.Image(src="grupo.png", width=300),]),
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
                        bgcolor="green",color="white",
                    )
                ], alignment="spaceBetween")
            )
        return ft.Column([
            ft.Text("Retos diarios", size=30, color="green400"),
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
                                color="white" if lleno else "white",
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
            ft.Text("Gremios", size=30, weight="bold", color="green400"),
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
            ft.Text("Perfil", size=30, weight="bold",color="green400"),
            ft.ElevatedButton("Créditos", on_click=self.abrir_nueva_ventana,bgcolor="green",color="white"),
            ft.ElevatedButton("Cerrar Sesión", on_click=lambda _: self.mostrar_login(),bgcolor="green", color="white")
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
ft.app(target=main,view=ft.AppView.WEB_BROWSER)