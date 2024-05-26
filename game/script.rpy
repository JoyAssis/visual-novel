# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Sora")
define b = Character("Rocco")
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
    n: "O tempo enquanto filho único foi tão pouco que não houve grandes ajustes na rotina de ninguém, não houve necessidade de adaptação nenhuma. Desde que se entende por gente, possui um grande laço de amor com sua irmãzinha. Os jovens pais os amam incondicionalmente e fazem de tudo, de acordo com suas próprias capacidades, para que seus filhos sejam felizes."
    show irma
    menu: 
        "Vamos começar!":
            jump chapter_1
        
        "Sair":
            $ renpy.quit()

label chapter_1:
     #scene sala
    
    n "4 anos depois, durante os preparativos para o Natal, é tempo de escolher os presentes."
    n "As crianças terminam a refeição, a mãe pede a birina que a ajude a recolher a mesa."

    hide irma
    hide irmao

    p "Crianças, hoje vocês podem escolher um presente especial. Qual vocês querem?"
    
    menu:
        "Irmão ganha um videogame, irmã ganha uma boneca":
            jump present_boy_videogame_girl_doll
    
        "Irmã ganha um videogame, irmão ganha uma boneca":
            jump present_girl_videogame_boy_doll

# Consequências para o presente: irmão recebe videogame, irmã recebe boneca
label present_boy_videogame_girl_doll:
    show irmao
    c "Um videogame! Isso vai ser incrível!"
    hide irmao

    show irma
    e "Eu ganhei uma boneca... legal."
    hide irma

    p "Divirtam-se com seus presentes, crianças."

    # Consequências do presente
    show irmao
    c "O videogame realmente me inspirou a aprender mais sobre tecnologia."
    hide irmao
    show irma
    e "Eu me sentia limitada com a boneca."

    # Pulando para o futuro
    # jump future_boy_tech_girl_limited

# Consequências para o presente: irmã recebe videogame, irmão recebe boneca
label present_girl_videogame_boy_doll:
    show irma
    e "Um videogame! Isso vai ser incrível!"
    hide irma
    show irmao
    c "Eu ganhei uma boneca... legal."
    hide irmao
    p "Divirtam-se com seus presentes, crianças."

    # Consequências do presente
    show irma
    e "O videogame realmente me inspirou a aprender mais sobre tecnologia."
    hide irma
    show irmao
    c "Eu me sentia limitado com a boneca."
    hide irmao

    # Pulando para o futuro
    # jump future_girl_tech_boy_limited

# # Futuro: irmão inspirado em tecnologia, irmã se sentindo limitada
# label future_boy_tech_girl_limited:
#     scene bg_room_future
#     show irmao
#     c "Graças ao videogame, eu decidi seguir carreira em tecnologia."
#     show irma
#     e "Me senti limitada pela boneca e tive dificuldade em encontrar meu caminho."

#     return

# # Futuro: irmã inspirada em tecnologia, irmão se sentindo limitado
# label future_girl_tech_boy_limited:
#     scene bg_room_future
#     show irma
#     e "Graças ao videogame, eu decidi seguir carreira em tecnologia."
#     show irmao
#     c "Me senti limitado pela boneca e tive dificuldade em encontrar meu caminho."


    # This ends the game.

    return
