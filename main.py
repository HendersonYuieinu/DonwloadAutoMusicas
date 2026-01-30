from flet import (
    Page,
    ThemeMode,
    MainAxisAlignment,
    CrossAxisAlignment,
    alignment,
    TextAlign,
    FontWeight,
    CupertinoButton,
    Column,
    Container,
    TextField,
    Text,
    Row,
    border,
    app,
    margin
)
from Script import download_API
import time


from utils import musiccard


def main(page: Page):
    page.bgcolor = '#F2F4F8'
    page.theme_mode = ThemeMode.LIGHT
    page.title = "DownMusic"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.window.width = 600
    page.window.height = 800
    page.padding = 20
    page.window.min_width = 400
    page.window.min_height = 600
    page.window.alignment = alignment.center
    page.window.resizable = False
    
    selecionados = {}
    
    avisor = download_API().aviso
    def deletar(link):
        selecionados.pop(link, None)
        print(selecionados)
        atualizarLista()
        
    def criarCard(music, link, deletarfunction=deletar):
        return musiccard.card(music, link, deletarfunction)
        
    def atualizarLista():
        LISTselecionados.controls.clear()
        for link, nome in selecionados.items():
            card = criarCard(nome, link)
            LISTselecionados.controls.append(card)
        page.update()
        
    def adicionar(e):
        
        if link_music.value == "":
            aviso.color = 'blacK'
            aviso.value = "Digite a url para realizar o download!"
            botaoDownload.disabled = False
            return False
        
        nome = download_API().get_name(link_music.value)
        if nome[1] == "ERROR":
            aviso.color = "RED"
            aviso.value = f'Não foi possível localizar o endereço.'
            page.update()
            return False
        if link_music.value in selecionados:
            aviso.color = "RED"
            aviso.value = f'Link já adicionado.'
            page.update()
            return False
            
        selecionados[link_music.value] = nome[0]
            
        card = criarCard(nome[0], link_music.value)
        LISTselecionados.controls.append(card)
        link_music.value = ""
        aviso.value = ''
        print(selecionados)
        page.update()
        return True
    
    def baixar(e):
        aviso.color = 'black'
        aviso.value = 'Carregando...'
        botaoDownload.disabled = True
        resultfinal = ""
        page.update()
        time.sleep(1)
        for link in selecionados.keys():
            result = download_API().audio(link)
            
            if result != "COMPLETE":
                aviso.color = "RED"
                aviso.value = f'Não foi possível baixar {selecionados[link]}.'
                botaoDownload.disabled = False
                page.update()
                return False
        resultfinal = "COMPLETE"
        
        if resultfinal == "COMPLETE":
            selecionados.clear()
            aviso.color = "green"
            aviso.value = "Downloads Completos."
            botaoDownload.disabled = False
            atualizarLista()    
        page.update()
        return True

    link_music = TextField(hint_text='Digite a url aqui...', text_align=TextAlign.LEFT, expand=True, bgcolor="white", color='black')
    aviso = Text(avisor, size=25, font_family="Arial", weight=FontWeight.BOLD)
    intro_text = Container(
                        content = Text('Baixar audio do youtube em mp3', size=25, weight = FontWeight.BOLD, font_family="Arial", text_align=TextAlign.CENTER, color='black'),
                        margin = margin.only(bottom=20),
                        alignment = alignment.center,
                        #bgcolor = "pink"          
                    )
    botaoADD = CupertinoButton("Adicionar", on_click=adicionar, bgcolor='#0057D9', color='#FFFFFF', width=150, height=50)
    botaoDownload = CupertinoButton("Download", on_click=baixar, bgcolor='#0057D9', color='#FFFFFF', width = 250)

    LISTselecionados = Column(
        controls=[],
        expand=True,
        width=500,
        scroll="auto",
    )
    
    lista = Container(
        content=LISTselecionados,
        expand=True,
        #bgcolor="white",
        alignment=alignment.top_center,
        border=border.all(1, '#0057D9'),
        border_radius=8,
    )
    
    campos = Container(
        content = Row(
            [link_music, botaoADD], 
        ),
        alignment = alignment.center,
        #bgcolor = 'green',
        padding = 10
    )

    aviso_container = Container(
        content = aviso,
        alignment = alignment.center
    )
    
    main = Column(
        controls=[intro_text, campos, lista, botaoDownload, aviso_container],
        horizontal_alignment=CrossAxisAlignment.CENTER,
        alignment=MainAxisAlignment.START,
        expand=True,
    )
    
    def update_layout(width, campos):
        if width <= 400:
            campos.content = Column(
                    [link_music, botaoADD],
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                )

        else:
            campos.content = Row(
                    [link_music, botaoADD],
                    alignment = MainAxisAlignment.CENTER,
                )
        page.update()
        
    
    page.on_resized = lambda e: update_layout(page.window.width, campos)
    update_layout(page.window.width, campos)
    
    page.add(
            main   
        )
    
app(host='0.0.0.0', target=main)
