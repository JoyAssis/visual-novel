# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Sora", color="#D10363")
define b = Character("Rocco", color="#028391")
define u = Character("você")
define n = Character("...")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene boy 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    n "O ano é 1998 e Rocco, que tem apenas 1 ano e 3 meses de idade, ganha uma irmãzinha."
    show irmao
    n "O tempo enquanto filho único foi tão pouco que não houve grandes ajustes na rotina de ninguém, não houve necessidade de adaptação nenhuma. Desde que se entende por gente, possui um grande laço de amor com sua irmãzinha. Os jovens pais os amam incondicionalmente e fazem de tudo, de acordo com suas próprias capacidades, para que seus filhos sejam felizes."
    show irma
    menu: 
        "Vamos começar!":
            jump chapter_1
        
        "Sair":
            $ renpy.quit()

label chapter_1:
     #scene sala
    
    n "4 anos depois, durante os preparativos para o Natal, é tempo de escolher os presentes."
    hide irma
    hide irmao 
    n "As crianças terminam a refeição, a mãe pede a Sora que a ajude a recolher a mesa."
    n "Sora ajuda a mãe?"
    
    menu:
        "Sim":
            jump present_girl_yes_boy_no
    
        "Não":
            jump present_girl_no_boy_yes

# Consequências para o presente: Sora ajuda a mão
label present_girl_yes_boy_no:
    g "Claro, mãe. Eu ajudo a recolher a mesa."
    n "Enquanto Sora ajuda a mãe, Rocco vai tomar seu banho. No caminho ele se distrai com um minigame que estava no chão do corredor e começa a jogar tetris."
    hide irma
    show irmao
    n "Quando Sora vai tomar banho, Rocco que já deveria estar de banho tomado ainda está jogando tetris."
    
    menu:
        n "O que a mãe deve fazer?"
        "Insistir":
            jump insistir_banho_irmao
        "Dar banho nas duas crianças":
            jump banho_duas_criancas

label present_girl_no_boy_yes:
    b "Deixa que eu ajudo mãe!" 
    n "Diz Rocco. Sora vai tomar banho. No caminho Sora se distrai com um minigame que estava no chão do corredor e começa a jogar tetris."
    hide irmao
    show irma
    n "Quando Rocco vai tomar banho, Sora que já deveria estar de banho tomado ainda está jogando tetris."
    n "O que a mãe deve fazer?"
    menu:
        "Insistir":
            jump insistir_banho_irmao
        "Dar banho nas duas crianças":
            jump banho_duas_criancas

label insistir_banho_irmao:
    n "A mãe dá banho em Sora e pede que o pai leve Rocco para tomar banho também, mas o pai diz que está assistindo TV. Ela explica que ainda precisa se arrumar, e ele continua dizendo que não vai, que já está pronto e não quer se molhar."
    n "O que a mãe deve fazer?"
    menu:
        "Insistir":
            jump insistir_final
    
        "Dar banho nas duas crianças":
            jump banho_duas_criancas_final

label insistir_final:
    n "O pai sai da frente da TV gritando com Rocco, que se assusta, e derruba o minigame no chão. O pai dá banho na criança, de forma impaciente, enquanto o menino chora."

label banho_duas_criancas_final:
    n "Depois de dar banho nas duas crianças, a mãe vai se arrumar."

label banho_duas_criancas:
    n "O pai sai da frente da TV resmungando, pega o minigame da mão de Rocco e leva para o banho. O pai dá banho na criança em silêncio, mas seu rosto transparece impaciência."

label loja_brinquedos:
    #scene loja de brinquedo
    n "Quando todos estão prontos, eles seguem juntos para a loja de brinquedos."
    n "Os pais decidem se separar para comprar os presentes." 
    n "Com quem Sora vai escolher seu presente?"
    show irma
    menu:
        "Com o pai":
            jump brinquedo_com_pai
        "Com a mãe":
            jump brinquedo_com_mae
    
label brinquedo_com_pai:
    #scene corredor de bonecas
    show irma
    n "Que brinquedo Sora vai escolher?"
    hide irma
    menu:
        "Uma boneca bebe":
            jump fim_cena
        "Uma boneca com kit de cozinha":
            jump fim_cena
    show irma #com a boneca?
label fim_cena:
    #scene  presentes 
    n "Sora gostou muito de seu presente! Seu irmão Rocco escolheu um console de videogame"

         
    # This ends the game.
    return
