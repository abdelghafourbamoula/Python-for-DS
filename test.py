from random import shuffle

def question(q):
    print(q['question'])
    choix = [q['correcte']]+q['incorrecte']
    shuffle(choix)
    print(choix)
    reponse = input(">>> La reponse est: ")
    print("\n Bonne réponse!") if reponse==q['correcte'] else print("\n Mauvaise réponse !" )
    
    return +1 if  reponse==q['correcte'] else -1


def Quiz(q):
    shuffle(q)
    score = 0
    for quest in q:
        score += question(quest)
    print(score)
    return "votre score est: {:.2f}".format((score*len(q))/100)


qs = [
    {'question': "Quelle est la couleur du cheval blanc d’Henry IV ?",
     'correcte': "blanc",
     'incorrecte': ["gris","noir","orange"]},
    
    {'question': "2 + 2 = ?",
     'correcte': "4",
     'incorrecte': ["42","44","0"]},
    
    {'question': "Qui publia et quand fut publié le premier algorithme ?",
     'correcte': "Al-Khwarizmi",
     'incorrecte': ["Edmund Husserl","John van Neumann","Guido van Rossum"]},
    
    {'question': "Chasser l'intrus parmi les langages de programmation suivants:",
     'correcte': "Linux",
     'incorrecte': ["Python","C++","Java"]},
]

Quiz(qs)