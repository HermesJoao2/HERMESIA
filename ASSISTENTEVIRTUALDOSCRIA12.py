# ARQUIVO PRINCIPAL DO HERMES - SEGUNDO PROTÓTIPO
 #   _      ___     _     ___    ___   __  __   _   _   ___
 #  /_\    / __|   /_\   |   \  | __| |  \/  | | | | | / __|
#  / _ \  | (__   / _ \  | |) | | _|  | |\/| | | |_| | \__ \
# /_/ \_\  \___| /_/ \_\ |___/  |___| |_|  |_|  \___/  |___/
# TCC 2022

#                                     \ | ___ | /

#bibliotecas necessárias - team academus - baixar usando o pip ou pip3 no cmd, se n funcionar dar uma olhada nos scripts PATH vlw vlw
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyautogui








audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-br')
            comando = comando.lower()
            if 'Hermes' in comando:
                print(comando)
                comando = comando.replace('hermes', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está funcionando')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'olá' in comando:
        maquina.say('Olá, eu sou hermes, estou pronto para ajudar')
        maquina.runAndWait()
    if 'que horas são' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('reproduzindo')
        maquina.runAndWait()
    if 'bom dia' in comando:
        maquina.say('Olá, eu sou hermes, o que vamos treinar hoje?')
        maquina.runAndWait()
    if 'nome' in comando:
        maquina.say('O meu nome é hermes')
        maquina.runAndWait()
    elif 'abrir navegador' in comando:
        maquina.say('abrindo navegador')
        maquina.runAndWait()
        pyautogui.press('winleft')
        pyautogui.write('brave')
        pyautogui.press('enter')
        # time.sleep(1)
    elif 'abrir valorant' in comando:
        maquina.say('abrindo valorant')
        maquina.runAndWait()
        pyautogui.press('winleft')
        pyautogui.write('valorant')
        pyautogui.press('enter')
    elif 'abrir spotify' in comando:
        maquina.say('abrindo Spotify')
        maquina.runAndWait()
        pyautogui.press('winleft')
        pyautogui.write('spotify')
        pyautogui.press('enter')
    if 'sua' in comando:
        maquina.say('sua vó na minha cama')
        maquina.runAndWait()












comando_voz_usuario()



