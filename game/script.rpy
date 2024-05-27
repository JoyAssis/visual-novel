# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Sora", color="#D10363")
define b = Character("Rocco", color="#028391")
define u = Character("você")
define n = Character("...")

define notification = "audio/notificacao.wav"
define mouse_selection = "audio/Mouse_Selection.wav"
define skip = "audio/Skip.wav"
label splashscreen:
    scene black
    with Pause(1)
    
    play sound "audio/Intro.wav"
    show text "Equipe 344 do Hackathon Mulheres no Game Kabum!" with dissolve
    with Pause(10)

    hide text with dissolve
    with Pause(2)
    
    return

# The game starts here.

label start:
    scene black
    with Pause(1)
    scene sala2
    with fade

    #show image:
        #zoom(diminui ou aumenta a proporção 0.5(50%))

    n "O ano é 1998 e Rocco, que tem apenas 1 ano e 3 meses de idade, ganha uma irmãzinha."
    play audio skip
    # show irmao at left:
    #     yalign 0.07
    # with dissolveR
    scene black with fade 
    scene sala2
    show irma
    n "O tempo enquanto filho único foi tão pouco que não houve grandes ajustes na rotina de ninguém, não houve necessidade de adaptação nenhuma."
    play audio skip
    n "Desde que se entende por gente, possui um grande laço de amor com sua irmãzinha. Os jovens pais os amam incondicionalmente e fazem de tudo, de acordo com suas próprias capacidades, para que seus filhos sejam felizes."
    play audio skip
    hide irma
    menu: 
        "Vamos começar!":
            play audio mouse_selection
            jump chapter_1
        
        "Sair":
            play audio mouse_selection
            $ renpy.quit()
 ## capitulo 1 ###########################################################################
 ## inicil sala natal ##########################################################################
label chapter_1:
    scene black
    with Pause(1)
    scene sala1
    stop music 
    # $ valor = 0  # Inicializa o valor da barra de progresso
    # show screen badGoal(valor)
    with fade
    n "4 anos depois, durante os preparativos para o Natal, é tempo de escolher os presentes."
    play audio skip
    n "As crianças terminam a refeição, a mãe pede a Sora que a ajude a recolher a mesa."
    play audio skip
    show irma
    n "Sora ajuda a mãe?"
    play audio skip
    hide irma
    
    menu:
        "Sim":
            play audio mouse_selection
            jump present_girl_yes_boy_no
    
        "Não":
            play audio mouse_selection
            jump present_girl_no_boy_yes


label present_girl_yes_boy_no:
    # Simula a atualização do progresso
    # while valor < 100:
    #     $ valor = update_progress(valor, 10)
    #     pause(1.0)  # Pausa de 1 segundo entre as atualizações
    show irma
    g "Claro, mãe. Eu ajudo a recolher a mesa."
    play audio skip
    hide irma
    n "Enquanto Sora ajuda a mãe, Rocco vai tomar seu banho. No caminho ele se distrai com um minigame que estava no chão do corredor e começa a jogar tetris."
    play audio skip
    show irmao
    with Pause(1)
    n "Quando Sora vai tomar banho, Rocco que já deveria estar de banho tomado ainda está jogando tetris."
    play audio skip
    hide irmao
    menu:
        n "O que a mãe deve fazer?"
        "Insistir":
            play audio mouse_selection
            jump insistir_banho_irmao
        "Dar banho nas duas crianças":
            play audio mouse_selection
            jump banho_duas_criancas

label present_girl_no_boy_yes:
    show irmao
    b "Deixa que eu ajudo mãe!" 
    play audio skip
    n "Diz Rocco. Sora vai tomar banho. No caminho Sora se distrai com um minigame que estava no chão do corredor e começa a jogar tetris."
    hide irmao
    show irma
    n "Quando Rocco vai tomar banho, Sora que já deveria estar de banho tomado ainda está jogando tetris."
    play audio skip
    
    menu:
        n "O que a mãe deve fazer?"
        "Insistir":
            jump insistir_banho_irmao
        "Dar banho nas duas crianças":
            jump banho_duas_criancas
 ## fim sala natal ###########################################################################################
 
 ## inicio banho #############################################################################################
label insistir_banho_irmao:
    hide irmao
    n "A mãe dá banho em Sora e pede que o pai leve Rocco para tomar banho também, mas o pai diz que está assistindo TV. Ela explica que ainda precisa se arrumar, e ele continua dizendo que não vai, que já está pronto e não quer se molhar."
    play audio skip
    
    menu:
        n "O que a mãe deve fazer?"
        "Insistir":
            play audio mouse_selection
            jump insistir_final
    
        "Dar banho nas duas crianças":
            play audio mouse_selection
            jump banho_duas_criancas_final

label insistir_final:
    show irmao
    #show rocco chorando
    n "O pai sai da frente da TV gritando com Rocco, que se assusta, e derruba o minigame no chão. O pai dá banho na criança, de forma impaciente, enquanto o menino chora."
    play audio skip
    jump loja_brinquedos
label banho_duas_criancas_final:
    n "Depois de dar banho nas duas crianças, a mãe vai se arrumar."
    play audio skip
    jump loja_brinquedos
label banho_duas_criancas:
    n "Depois de dar banho nas duas crianças, a mãe vai se arrumar."
    play audio skip
    hide irmao
    jump loja_brinquedos
    ## fim banho ###########################################################################################
    
    ## inicio loja de brinquedo ############################################################################
label loja_brinquedos:
    #scene loja de brinquedo
    n "Quando todos estão prontos, eles seguem juntos para a loja de brinquedos."
    play audio skip
    scene loja
    n "Os pais decidem se separar para comprar os presentes." 
    play audio skip
    
    show irma
    menu:
        n "Com quem Sora vai escolher seu presente?"
        "Com o pai":
            play audio mouse_selection
            jump brinquedo_com_pai
        "Com a mãe":
            play audio mouse_selection
            jump brinquedo_com_mae
    
label brinquedo_com_pai:
    #scene corredor de bonecas
    show irma
    
    hide irma
    menu:
        n "Que brinquedo Sora vai escolher?"
        "Uma boneca bebe":
            play audio mouse_selection
            jump fim_cena
        "Uma boneca com kit de cozinha":
            play audio mouse_selection
            jump fim_cena
label fim_cena:
    #scene  presentes 
    show irma
    n "Sora gostou muito de seu presente! Seu irmão Rocco escolheu um console de videogame"
    play audio skip
    jump curiosidade_brinquedo
    ## fim loja de brinquedo ##############################################################################

 ## inicio do fim ##########################################################################
label curiosidade_brinquedo:
    show irma
    n "Sora ficou curiosa com o presente de seu irmão. Então ela..."
    play audio skip
    menu:
        "Observa Rocco jogando":
            play audio mouse_selection
            jump observa_jogando
        "Pede para jogar":
            play audio mouse_selection
            jump pede_para_jogar

label observa_jogando:
    n "Sora brinca com sua boneca enquanto observa as jogadas de Rocco no seu console."
    play audio skip
    jump chama_para_jogar

label pede_para_jogar:
    n "Rocco ficou feliz com o pedido de Sora e os dois revezam o jogo."
    play audio skip
    jump jogando

label chama_para_jogar:
    n "Rocco percebe Sora observando e a chama para jogar."
    play audio skip
    jump jogando

label jogando:
   #scene jogando adolecentes no quarto
   n "jogando juntos no quarto"
   play audio skip

return

# screen badGoal(valor):
#     frame:
#         vbox:
#             text "Progresso de incentivo" style "progress_bar_text"
#             bar value AnimatedValue(value=valor, range=100) style "progress_bar"

# init python:
#     # Define uma função para atualizar o valor da barra
#     def update_progress(valor, increment):
#         valor += increment
#         return valor