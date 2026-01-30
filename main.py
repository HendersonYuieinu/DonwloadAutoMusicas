import flet as ft
from Script import download_API
import time
from utils import musiccard


def main(page: ft.Page):
    page.bgcolor = '#F2F4F8'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "DownMusic"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 600
    page.window.height = 800
    page.padding = 20
    page.window.min_width = 400
    page.window.min_height = 600
    page.window.alignment = ft.alignment.center
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

    link_music = ft.TextField(hint_text='Digite a url aqui...', text_align=ft.TextAlign.LEFT, expand=True, bgcolor="white", color='black')
    aviso = ft.Text(avisor, size=25, font_family="Arial", weight=ft.FontWeight.BOLD)
    intro_text = ft.Container(
                        content = ft.Text('Baixar audio do youtube em mp3', size=25, weight = ft.FontWeight.BOLD, font_family="Arial", text_align=ft.TextAlign.CENTER, color='black'),
                        margin = ft.margin.only(bottom=20),
                        alignment = ft.alignment.center,
                        #bgcolor = "pink"          
                    )
    botaoADD = ft.CupertinoButton("Adicionar", on_click=adicionar, bgcolor='#0057D9', color='#FFFFFF', width=150, height=50)
    botaoDownload = ft.CupertinoButton("Download", on_click=baixar, bgcolor='#0057D9', color='#FFFFFF', width = 250)

    LISTselecionados = ft.Column(
        controls=[],
        expand=True,
        width=500,
        scroll="auto",
    )
    
    lista = ft.Container(
        content=LISTselecionados,
        expand=True,
        #bgcolor="white",
        alignment=ft.alignment.top_center,
        border=ft.border.all(1, '#0057D9'),
        border_radius=8,
    )
    
    campos = ft.Container(
        content = ft.Row(
            [link_music, botaoADD], 
        ),
        alignment = ft.alignment.center,
        #bgcolor = 'green',
        padding = 10
    )

    aviso_container = ft.Container(
        content = aviso,
        alignment = ft.alignment.center
    )
    
    main = ft.Column(
        controls=[intro_text, campos, lista, botaoDownload, aviso_container],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.START,
        expand=True,
    )
    
    def update_layout(width, campos):
        if width <= 400:
            campos.content = ft.Column(
                    [link_music, botaoADD],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )

        else:
            campos.content = ft.Row(
                    [link_music, botaoADD],
                    alignment = ft.MainAxisAlignment.CENTER,
                )
        page.update()
        
    
    page.on_resized = lambda e: update_layout(page.window.width, campos)
    update_layout(page.window.width, campos)
    
    page.add(
            main   
        )
    
ft.app(host='0.0.0.0', target=main)
