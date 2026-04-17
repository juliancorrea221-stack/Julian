import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Api Hollow knight"
    page.scroll = "auto"

    # Input para ID del personaje
    input_id = ft.TextField(
        label="ID del personaje",
        hint_text="Ej: 3",
        width=200
    )

    # Contenedor de resultados
    result = ft.Column()

    def fetch_character(e):
        result.controls.clear()
        
        char_id = input_id.value.strip()
        if not char_id.isdigit():
            result.controls.append(ft.Text("❌ Ingresa un número válido"))
            page.update()
            return
        
        url = f"https://hollowknight.wiki/mw/index.php?title=The_Knight&action=edit{char_id}"
        
        try:
            response = requests.get(url)
            data = response.json()

            # Mostrar datos básicos
            result.controls.append(ft.Text(f"Nombre: {data.get('name', 'N/A')}", size=20, weight="bold"))
            result.controls.append(ft.Text(f"Género: {data.get('gender', 'N/A')}"))
            result.controls.append(ft.Text(f"Estado: {data.get('status', 'N/A')}"))
            result.controls.append(ft.Text(f"Key: {data.get('description', 'N/A')}"))

            # Imagen
            if data.get("image"):
                result.controls.append(
                    ft.Image(
                        src=data["image"],
                        width=200,
                        height=200,
                        fit=ft.ImageFit.CONTAIN
                    )
                )

        except Exception as ex:
            result.controls.append(ft.Text(f"⚠️ Error: {ex}"))

        page.update()

    # Botón
    btn = ft.ElevatedButton("Buscar personaje", on_click=fetch_character)

    # Layout
    page.add(
        ft.Column([
            ft.Text("🐜 Hollow knight API App", size=30, weight="bold"),
            input_id,
            btn,
            ft.Divider(),
            result
        ])
    )

# Ejecutar app en navegador
ft.app(target=main)