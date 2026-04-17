import flet as ft


class PortafolioWeb(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.padding = 0
        self.page.fonts = {"Starjhol": "../assets/Starjhol.ttf"}
        self.page.title = "Mi Portafolio"
        self.page.bgcolor = ft.colors.SURFACE_VARIANT
        self.color_primaria = ft.colors.GREEN_500
        self.color_secundaria = ft.colors.BLUE_GREY_800

        self.build()

    def build(self):
        self.cambiar_modo = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            bgcolor=self.color_primaria,
            icon_color=ft.colors.WHITE,
            tooltip="Cambiar modo",
            on_click=self.cambiar_modo_oscuro,
        )

        self.animation_style = ft.animation.Animation(800, ft.AnimationCurve.EASE_OUT_CUBIC)

        self.frame_inicio = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(0, 0),
            content=self.build_inicio(),
        )

        self.frame_servicio = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2, 0),
            content=self.build_servicio(),
        )

        self.titulo_resumen = ft.Text(
            "Mi experiencia profesional",
            size=32,
            weight=ft.FontWeight.W_900,
            color=self.color_primaria,
        )

        self.frame_experiencia = ft.Container(
            expand=True,
            content=ft.Column(
                spacing=16,
                controls=[
                    ft.Text(
                        "Ingeniero de software con enfoque en proyectos reales, diseño elegante y soluciones funcionales.",
                        size=18,
                        color=ft.colors.BLACK87,
                    ),
                    self.card_info(
                        "Desarrollo web completo",
                        "Integro front-end y back-end con una experiencia intuitiva y moderna.",
                        "assets/html5.svg",
                    ),
                    self.card_info(
                        "Herramientas inteligentes",
                        "Automatizo procesos y construyo aplicaciones interactivas con Python y JavaScript.",
                        "assets/python.svg",
                    ),
                ],
            ),
        )

        self.frame_eduacion = ft.Container(
            expand=True,
            visible=False,
            content=ft.Column(
                spacing=16,
                controls=[
                    ft.Text(
                        "Formación sólida y actualizada para desarrollar proyectos con sentido y estilo.",
                        size=18,
                        color=ft.colors.BLACK87,
                    ),
                    self.card_info(
                        "Ingeniería de Sistemas",
                        "Estudios técnicos que incluyen programación, bases de datos y arquitectura de software.",
                        "assets/matlab.svg",
                    ),
                    self.card_info(
                        "Aprendizaje constante",
                        "Capacitación en UI/UX, diseño responsivo y nuevas tecnologías.",
                        "assets/react.svg",
                    ),
                ],
            ),
        )

        self.frame_habilidades = ft.Container(
            expand=True,
            visible=False,
            content=ft.Column(
                spacing=18,
                controls=[
                    ft.Text(
                        "Habilidades técnicas que impulsan cada proyecto con calidad y detalle.",
                        size=18,
                        color=ft.colors.BLACK87,
                    ),
                    self.skill_row("Python", 0.95, "assets/python.svg"),
                    self.skill_row("JavaScript", 0.88, "assets/js.svg"),
                    self.skill_row("React", 0.80, "assets/react.svg"),
                    self.skill_row("SolidWorks", 0.72, "assets/solidworks.svg"),
                ],
            ),
        )

        self.frame_resumen = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2, 0),
            content=self.build_resumen(),
        )

        self.frame_contacto = ft.Container(
            expand=True,
            padding=20,
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.only(top_left=20, top_right=20),
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2, 0),
            content=self.build_contacto(),
        )

        self.content = ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    padding=18,
                    bgcolor=self.color_secundaria,
                    content=ft.ResponsiveRow(
                        spacing=12,
                        run_spacing=12,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                col={"xs": 12, "md": 3},
                                content=ft.Text(
                                    "Nom",
                                    size=28,
                                    weight=ft.FontWeight.W_900,
                                    color=ft.colors.GREEN_100,
                                ),
                            ),
                            ft.Container(
                                col={"xs": 12, "md": 8},
                                content=ft.ResponsiveRow(
                                    spacing=6,
                                    run_spacing=6,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextButton(
                                            "Inicio",
                                            style=ft.ButtonStyle(color=ft.colors.WHITE),
                                            col={"xs": 12, "sm": 6, "md": 3},
                                            on_click=lambda e: self.cambiar_pagina(0),
                                        ),
                                        ft.TextButton(
                                            "Servicios",
                                            style=ft.ButtonStyle(color=ft.colors.WHITE),
                                            col={"xs": 12, "sm": 6, "md": 3},
                                            on_click=lambda e: self.cambiar_pagina(1),
                                        ),
                                        ft.TextButton(
                                            "Resumen",
                                            style=ft.ButtonStyle(color=ft.colors.WHITE),
                                            col={"xs": 12, "sm": 6, "md": 3},
                                            on_click=lambda e: self.cambiar_pagina(2),
                                        ),
                                        ft.TextButton(
                                            "Contacto",
                                            style=ft.ButtonStyle(color=ft.colors.WHITE),
                                            col={"xs": 12, "sm": 6, "md": 3},
                                            on_click=lambda e: self.cambiar_pagina(3),
                                        ),
                                    ],
                                ),
                            ),
                            ft.Container(
                                col={"xs": 12, "md": 1},
                                alignment=ft.alignment.center_right,
                                content=self.cambiar_modo,
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    expand=True,
                    content=ft.Stack(
                        controls=[
                            self.frame_inicio,
                            self.frame_servicio,
                            self.frame_resumen,
                            self.frame_contacto,
                        ]
                    ),
                ),
                ft.Container(
                    padding=18,
                    gradient=ft.LinearGradient(colors=[self.color_primaria, ft.colors.TRANSPARENT]),
                    content=ft.Text(
                        "Copyright 2024 Nombre Apellido · Todos los derechos reservados",
                        size=14,
                        color=ft.colors.WHITE,
                    ),
                ),
            ],
        )

        self.page.add(self.content)

    def build_inicio(self):
        return ft.ResponsiveRow(
            expand=True,
            spacing=20,
            run_spacing=20,
            controls=[
                ft.Container(
                    col={"xs": 12, "md": 7},
                    padding=20,
                    content=ft.Column(
                        spacing=20,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Text(
                                "Hola, soy Nombre Apellido",
                                size=44,
                                weight=ft.FontWeight.W_900,
                                color=self.color_secundaria,
                            ),
                            ft.Text(
                                "Diseño y desarrollo experiencias digitales con estilo claro, funcional y práctico.",
                                size=20,
                                color=ft.colors.BLACK54,
                            ),
                            ft.Text(
                                "Transformo ideas en soluciones reales, desde portafolios con personalidad hasta aplicaciones profesionales.",
                                size=16,
                                color=ft.colors.BLACK45,
                            ),
                            ft.Row(
                                spacing=12,
                                controls=[
                                    ft.ElevatedButton(
                                        "Ver mis servicios",
                                        bgcolor=self.color_primaria,
                                        on_click=lambda e: self.cambiar_pagina(1),
                                    ),
                                    ft.OutlinedButton("Descargar perfil", on_click=lambda e: None),
                                ],
                            ),
                            ft.ResponsiveRow(
                                spacing=16,
                                run_spacing=16,
                                controls=[
                                    ft.Container(col={"xs": 12, "sm": 4}, content=self.stat_card("Proyectos", "+12")),
                                    ft.Container(col={"xs": 12, "sm": 4}, content=self.stat_card("Experiencia", "3 años")),
                                    ft.Container(col={"xs": 12, "sm": 4}, content=self.stat_card("Clientes", "+8")),
                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    col={"xs": 12, "md": 5},
                    height=360,
                    border_radius=20,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    content=ft.Image(src="assets/foto.jpg", fit=ft.ImageFit.COVER),
                ),
            ],
        )

    def build_servicio(self):
        return ft.Column(
            expand=True,
            spacing=24,
            controls=[
                ft.Text(
                    "Servicios que ofrezco",
                    size=34,
                    weight=ft.FontWeight.W_900,
                    color=self.color_secundaria,
                ),
                ft.Text(
                    "Trabajo con imágenes, código y diseño para entregar productos visualmente atractivos y fáciles de usar.",
                    size=18,
                    color=ft.colors.BLACK54,
                ),
                ft.ResponsiveRow(
                    spacing=18,
                    run_spacing=18,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, expand=True, content=self.service_card(
                            "Sitios web modernos",
                            "Desarrollo interfaces responsivas con HTML5, CSS y componentes atractivos.",
                            "assets/html5.svg",
                        )),
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, expand=True, content=self.service_card(
                            "Apps con Python",
                            "Construyo herramientas efectivas para automatizar procesos y visualizar datos.",
                            "assets/python.svg",
                        )),
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, expand=True, content=self.service_card(
                            "Diseño técnico",
                            "Integración de proyectos con CAD, modelado 3D y soluciones creativas.",
                            "assets/solidworks.svg",
                        )),
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, expand=True, content=self.service_card(
                            "Interfaces interactivas",
                            "Experiencias dinámicas con React y JavaScript.",
                            "assets/react.svg",
                        )),
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, expand=True, content=self.service_card(
                            "Contenido multimedia",
                            "Uso imágenes, video y animaciones para contar historias con claridad.",
                            "assets/js.svg",
                        )),
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, expand=True, content=self.service_card(
                            "Análisis inteligente",
                            "Optimizaciones basadas en datos que mejoran cada proyecto.",
                            "assets/matlab.svg",
                        )),
                    ],
                ),
            ],
        )

    def build_resumen(self):
        return ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.ResponsiveRow(
                    spacing=12,
                    run_spacing=12,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Container(col={"xs": 12, "md": 6}, content=self.titulo_resumen),
                        ft.Container(
                            col={"xs": 12, "md": 6},
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.END,
                                spacing=12,
                                controls=[
                                    ft.ElevatedButton("Experiencia", on_click=lambda e: self.cambiar_pagina_resumen(0)),
                                    ft.OutlinedButton("Educación", on_click=lambda e: self.cambiar_pagina_resumen(1)),
                                    ft.OutlinedButton("Habilidades", on_click=lambda e: self.cambiar_pagina_resumen(2)),
                                ],
                            ),
                        ),
                    ],
                ),
                self.frame_experiencia,
                self.frame_eduacion,
                self.frame_habilidades,
            ],
        )

    def build_contacto(self):
        return ft.Column(
            expand=True,
            spacing=24,
            controls=[
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"xs": 12, "md": 7},
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text(
                                        "Hablemos de tu próximo proyecto",
                                        size=34,
                                        weight=ft.FontWeight.W_900,
                                        color=self.color_secundaria,
                                    ),
                                    ft.Text(
                                        "Estoy listo para colaborar, crear una propuesta personalizada o lanzar una idea con fuerza.",
                                        size=18,
                                        color=ft.colors.BLACK54,
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"xs": 12, "md": 5},
                            width=220,
                            height=220,
                            border_radius=20,
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                            content=ft.Image(src="assets/linkedin.png", fit=ft.ImageFit.CONTAIN),
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=18,
                    run_spacing=18,
                    controls=[
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, content=self.contact_card("Correo", "hola@ejemplo.com", "assets/github.png")),
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, content=self.contact_card("Teléfono", "+57 300 123 4567", "assets/youtube.png")),
                        ft.Container(col={"xs": 12, "sm": 6, "md": 4}, content=self.contact_card("LinkedIn", "linkedin.com/in/usuario", "assets/linkedin.png")),
                    ],
                ),
                ft.Text(
                    "Escribe un mensaje para recibir una asesoría, comenzar un proyecto o compartir tu idea.",
                    size=16,
                    color=ft.colors.BLACK54,
                ),
            ],
        )

    def stat_card(self, title: str, value: str):
        return ft.Container(
            padding=16,
            width=140,
            border_radius=16,
            bgcolor=ft.colors.GREEN_50,
            content=ft.Column(
                spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(value, size=24, weight=ft.FontWeight.W_900, color=self.color_primaria),
                    ft.Text(title, size=14, color=ft.colors.BLACK45),
                ],
            ),
        )

    def service_card(self, title: str, subtitle: str, icon_src: str):
        return ft.Container(
            expand=True,
            padding=20,
            border_radius=20,
            bgcolor=ft.colors.BLUE_GREY_50,
            shadow=ft.BoxShadow(blur_radius=12, color=ft.colors.BLACK12, offset=ft.Offset(0, 8)),
            content=ft.Column(
                spacing=16,
                controls=[
                    ft.Image(src=icon_src, width=64, height=64, fit=ft.ImageFit.CONTAIN),
                    ft.Text(title, size=18, weight=ft.FontWeight.W_800, color=self.color_secundaria),
                    ft.Text(subtitle, size=14, color=ft.colors.BLACK54),
                ],
            ),
        )

    def card_info(self, title: str, description: str, icon_src: str):
        return ft.Container(
            padding=18,
            border_radius=20,
            bgcolor=ft.colors.GREEN_50,
            content=ft.Row(
                spacing=16,
                controls=[
                    ft.Image(src=icon_src, width=50, height=50, fit=ft.ImageFit.CONTAIN),
                    ft.Column(
                        spacing=6,
                        controls=[
                            ft.Text(title, size=18, weight=ft.FontWeight.W_900, color=self.color_secundaria),
                            ft.Text(description, size=14, color=ft.colors.BLACK54),
                        ],
                    ),
                ],
            ),
        )

    def skill_row(self, name: str, value: float, icon_src: str):
        return ft.Row(
            spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(src=icon_src, width=36, height=36, fit=ft.ImageFit.CONTAIN),
                ft.Column(
                    expand=True,
                    spacing=8,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(name, size=16, weight=ft.FontWeight.W_700, color=self.color_secundaria),
                                ft.Text(f"{int(value * 100)}%", size=14, color=ft.colors.BLACK54),
                            ],
                        ),
                        ft.ProgressBar(value=value, color=self.color_primaria),
                    ],
                ),
            ],
        )

    def contact_card(self, title: str, detail: str, icon_src: str):
        return ft.Container(
            expand=True,
            padding=18,
            border_radius=20,
            bgcolor=ft.colors.BLUE_GREY_50,
            content=ft.Row(
                spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=48,
                        height=48,
                        border_radius=16,
                        bgcolor=ft.colors.WHITE,
                        content=ft.Image(src=icon_src, fit=ft.ImageFit.CONTAIN),
                    ),
                    ft.Column(
                        spacing=6,
                        controls=[
                            ft.Text(title, size=14, weight=ft.FontWeight.W_800, color=self.color_secundaria),
                            ft.Text(detail, size=14, color=ft.colors.BLACK54),
                        ],
                    ),
                ],
            ),
        )

    def cambiar_pagina(self, e):
        self.frame_inicio.offset.x = -2
        self.frame_servicio.offset.x = -2
        self.frame_resumen.offset.x = -2
        self.frame_contacto.offset.x = -2

        if e == 0:
            self.frame_inicio.offset.x = 0
        elif e == 1:
            self.frame_servicio.offset.x = 0
        elif e == 2:
            self.frame_resumen.offset.x = 0
        elif e == 3:
            self.frame_contacto.offset.x = 0

        self.page.update()

    def cambiar_modo_oscuro(self, e):
        if e.control.icon == "dark_mode":
            self.cambiar_modo.icon = ft.icons.LIGHT_MODE
            self.page.theme_mode = "light"
        else:
            self.cambiar_modo.icon = ft.icons.DARK_MODE
            self.page.theme_mode = "dark"
        self.page.update()

    def cambiar_pagina_resumen(self, e):
        self.frame_experiencia.visible = False
        self.frame_eduacion.visible = False
        self.frame_habilidades.visible = False

        if e == 0:
            self.frame_experiencia.visible = True
            self.titulo_resumen.value = "Mi experiencia profesional"
        elif e == 1:
            self.frame_eduacion.visible = True
            self.titulo_resumen.value = "Mi educación"
        elif e == 2:
            self.frame_habilidades.visible = True
            self.titulo_resumen.value = "Mis habilidades"

        self.page.update()


ft.app(target=lambda page: PortafolioWeb(page), view=ft.WEB_BROWSER, assets_dir="assets")
