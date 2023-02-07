import requests
from bs4 import BeautifulSoup
import csv


def beautiful_requests(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


# Exercise 1
# Affiche le lien de l'image de l'URL donnée
def exercise_1(url_exercise1):
    response = beautiful_requests(url_exercise1)
    line = response.findAll('img')
    print(f"My image: {line[4]['src']} //")

# Exercise 2
# Extrais les titres des 250 meilleurs films de tous les temps
def exercise_2(url_exercise2):
    response = beautiful_requests(url_exercise2)
    all_links = response.findAll('a')
    # res = all_links
    for movie in all_links:
        try:
            x = movie['role']
            continue
        except:
            try:
                print(movie['title'])
            except:
                continue


# Exercise 3
# Extrais les noms des pays et leurs PIB et stocke les dans un fichier csv
def exercise_3(url_exercise3):
    response = beautiful_requests(url_exercise3)


if __name__ == '__main__':
    ton_pseudo_github = 'ton_pseudo_github'
    url_exercise1 = 'https://github.com/VictorDelamonica/'
    url_exercise2 = 'https://www.imdb.com/chart/top/'
    url_exercise3 = 'https://fr.wikipedia.org/wiki/Liste_des_pays_par_PIB_nominal'
    print("Exercise 1: ")
    exercise_1(url_exercise1)
    print("\n\nExercise 2: ")
    exercise_2(url_exercise2)
    print("\n\nExercise 3: ")
    # exercise_3(url_exercise3)
