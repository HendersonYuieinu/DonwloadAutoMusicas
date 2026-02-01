# 🎵 DownloadAutoMusicas

O **DownloadAutoMusicas** é a evolução do antigo projeto **DownMusic**, trazendo uma aplicação totalmente nova, com interface moderna, novas funcionalidades e correções de erros da versão anterior.  
Seu objetivo é simples: baixar músicas do YouTube em formato **MP3** com qualidade de áudio otimizada.

---

## 🚀 Tecnologias

- **Python** → linguagem principal do projeto  
- **Flet** → framework para criação da interface gráfica no estilo Flutter  
- **yt-dlp** → ferramenta integrada para baixar vídeos do YouTube  
- **ffmpeg** → pós-processamento para converter vídeos em MP3 com boa qualidade de áudio  

> Futuramente será adicionada a opção para o usuário escolher a qualidade do áudio.

---

## ⚙️ Funcionalidades

- Inserir o link da música do YouTube e adicionar à lista  
- Criar uma lista de músicas, exibindo na tela o nome de cada faixa adicionada  
- Baixar todas as músicas da lista em sequência  
- Converter automaticamente os vídeos para **MP3**  
- Salvar os arquivos em uma pasta chamada **Musicas**, criada dentro do diretório do projeto ou do executável  

---

## 📖 Como usar

1. Abra o aplicativo  
2. Insira o link da música do YouTube  
3. Clique em **Adicionar** para incluir na lista  
4. Após montar sua lista, clique em **Download**  
5. As músicas serão baixadas e convertidas para MP3, ficando disponíveis na pasta **Musicas**  

---

## 📌 Diferenciais em relação ao DownMusic

- O antigo **DownMusic** baixava apenas músicas individualmente  
- O novo **DownloadAutoMusicas** permite criar listas e baixar várias músicas de uma vez  
- Interface gráfica mais moderna e intuitiva  
- Melhor gerenciamento de downloads e conversão automática para MP3  

---

## 📸 Capturas de Tela

Aqui estão algumas demonstrações da interface do **DownloadAutoMusicas**:

### Tela principal
<img width="585" height="788" alt="Captura de tela 2026-02-01 124354" src="https://github.com/user-attachments/assets/a631855a-04c4-4faa-83be-beb4bd5be5f1" />


### Lista de músicas adicionadas
<img width="585" height="793" alt="Captura de tela 2026-02-01 124559" src="https://github.com/user-attachments/assets/4cbfa1dd-1f18-4b22-8833-82fae83567b4" />


### Processo de download
https://github.com/user-attachments/assets/8651fd6d-d1f9-49a8-893b-cfa046317647

---

## 🛠️ Futuras melhorias

- Escolha da qualidade do áudio pelo usuário  
- Opções avançadas de configuração de download  
- Melhorias na interface gráfica

## adendo:
para o código rodar corretamento, é necessário ter instalado o ffmpeg e configurado no PATH do sistema. ao transformar em executável eu envio junto o ffmpeg na pasta /dist, gerado pelo flet.
