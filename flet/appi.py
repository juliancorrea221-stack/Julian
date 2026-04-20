import flet as ft
import requests
import re

def main(page: ft.Page):
    page.title = "Hollow Knight Wiki Explorer"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"

    # Input de búsqueda
    input_name = ft.TextField(
        label="Personaje de Hallownest",
        hint_text="Hornet, Grimm, Quirrel...",
        width=300,
        on_submit=lambda _: fetch_character(None)
    )

    # El contenedor de resultados (aquí es donde se "limpia" y se "escribe")
    result = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def fetch_character(e):
        # --- PASO CLAVE: Limpiamos lo que había antes ---
        result.controls.clear()
        page.update() # Actualiza para que el usuario vea que está cargando
        
        query = input_name.value.strip()
        if not query: return

        headers = {"User-Agent": "Mozilla/5.0"}
        url = "https://hollowknight.fandom.com/api.php"
        
        params = {
            "action": "query",
            "format": "json",
            "titles": query,
            "prop": "revisions|pageimages",
            "rvprop": "content",
            "pithumbsize": 500,
            "redirects": 1
        }

        try:
            response = requests.get(url, params=params, headers=headers)
            data = response.json()
            pages = data.get("query", {}).get("pages", {})
            page_id = next(iter(pages))
            
            if page_id == "-1":
                result.controls.append(ft.Text("❌ No encontrado", color="red", size=20))
            else:
                content_node = pages[page_id]
                title = content_node.get("title")
                raw_text = content_node.get("revisions", [{}])[0].get("*", "")
                
                # Limpieza de código Wiki
                clean = re.sub(r'\{\{.*?\}\}', '', raw_text, flags=re.DOTALL)
                clean = re.sub(r'<.*?>', '', clean, flags=re.DOTALL)
                clean = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', clean)
                
                paragraphs = clean.split('\n')
                final_desc = "No se encontró descripción."
                
                for p in paragraphs:
                    p = p.strip()
                    # Filtramos links y textos técnicos cortos
                    if len(p) > 40 and "youtu" not in p and "|" not in p:
                        final_desc = p
                        break 

                image_info = content_node.get("thumbnail", {}).get("source")

                # Agregamos los nuevos elementos al contenedor
                result.controls.append(ft.Text(title, size=35, weight="bold", color="amber"))
                
                if image_info:
                    result.controls.append(ft.Image(src=image_info, width=300, height=300))
                
                result.controls.append(
                    ft.Container(
                        content=ft.Text(final_desc, size=16, text_align="justify"),
                        padding=25,
                        width=550,
                        bgcolor="#1a1a1a",
                        border_radius=15,
                        border=ft.border.all(1, "#333333")
                    )
                )

        except Exception as ex:
            result.controls.append(ft.Text(f"⚠️ Error: {ex}", color="red"))

        # --- PASO CLAVE: Refrescar la página ---
        page.update()

    btn = ft.ElevatedButton("Consultar Diario", on_click=fetch_character)

    page.add(
        ft.Text("🐜 Hallownest Hunter", size=40, weight="bold"),
        ft.Row([input_name, btn], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        result
    )

ft.app(target=main)