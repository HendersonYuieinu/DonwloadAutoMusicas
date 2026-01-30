import flet as ft

def card(music, link, deletefunction):
    botaodelete = ft.TextButton("Excluir", style=ft.ButtonStyle(color="#0057D9", text_style=ft.TextStyle(size=16,weight=ft.FontWeight.BOLD)), on_click=lambda e: deletefunction(link))
    return ft.Card(
        shadow_color=ft.Colors.ON_SURFACE_VARIANT,
        elevation=5,
        content=ft.Container(
            bgcolor="#FFFFFF",
            border_radius=8,
            padding=8,
            content=ft.Column(
                controls=[ft.ListTile(
                bgcolor="#F2F4F8",
                leading=ft.Icon(ft.icons.MUSIC_NOTE, color="black"),
                title=ft.Text(f"{music}", color="black", weight=ft.FontWeight.BOLD)
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    ft.Text(f'{link}', visible=False),
                    botaodelete
                    ])
                ]  
            )
            )
        )
          