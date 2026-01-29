import flet as ft

def card(music, link, deletefunction):
    botaodelete = ft.TextButton("Delete", on_click=lambda e: deletefunction(link))
    return ft.Card(
        content=ft.Container(
            bgcolor="lightblue",
            border_radius=5,
            padding=5,
            content=ft.Column(
                controls=[ft.ListTile(
                bgcolor="black",
                leading=ft.Icon(ft.icons.MUSIC_NOTE),
                title=ft.Text(f"{music}")
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
          