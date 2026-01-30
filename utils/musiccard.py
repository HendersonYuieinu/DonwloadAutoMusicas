from flet import (
    Card,
    Container,
    Text,
    Icon,
    ListTile,
    Row,
    Column,
    TextButton,
    ButtonStyle,
    TextStyle,
    FontWeight,
    Colors,
    MainAxisAlignment,
    icons
)

def card(music, link, deletefunction):
    botaodelete = TextButton("Excluir", style=ButtonStyle(color="#0057D9", text_style=TextStyle(size=16,weight=FontWeight.BOLD)), on_click=lambda e: deletefunction(link))
    return Card(
        shadow_color=Colors.ON_SURFACE_VARIANT,
        elevation=5,
        content=Container(
            bgcolor="#FFFFFF",
            border_radius=8,
            padding=8,
            content=Column(
                controls=[ListTile(
                bgcolor="#F2F4F8",
                leading=Icon(icons.MUSIC_NOTE, color="black"),
                title=Text(f"{music}", color="black", weight=FontWeight.BOLD)
            ),
            Row(
                alignment=MainAxisAlignment.END,
                controls=[
                    Text(f'{link}', visible=False),
                    botaodelete
                    ])
                ]  
            )
            )
        )
          