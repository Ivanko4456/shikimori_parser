import os.path
from cfg import headers
import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
import tkinter.messagebox


def getHTML(url: str) -> str:
    html = requests.get(url=url, headers=headers)
    if html.status_code == 200:
        return html.text
    else:
        tk.messagebox.showerror(title='Ошибка', message='Пользователь не найден')


def get_anime_list(animehtml: str) -> list:
    anime_names, nums, categs, comments, values = None, None, None, None, None
    soup = BeautifulSoup(animehtml, "html.parser")
    try:
        rawlist = soup.find_all('span', class_="name-ru")
        anime_names = [name.text.replace('√', '') for name in rawlist]

        raw_comments = soup.find_all('div', class_='rate-text')
        comments = [comment.text for comment in raw_comments]

        rawnums = soup.find_all('td', class_='index')
        nums = [int(num.text) for num in rawnums]

        raw_vals = soup.find_all('span', attrs={'data-field': 'score'})
        values = [value.text for value in raw_vals]

        rawcategories = soup.find('div', class_='list-groups').find_all('div', class_='subheadline m5')
        categs = [categ.text for categ in rawcategories]
    except AttributeError:
        tk.messagebox.showerror(title='Ошибка', message='Похоже, у пользователя нет списка')
    return anime_names, nums, categs, comments, values


def make_tuple(names: list, nums: list, categs: list, comments: list, values: list) -> list:
    categ = -1
    anime = []
    isfirst = True
    for i in range(len(nums)):
        if nums[i] != 1:
            anime.append((categs[categ], nums[i], names[i], comments[i], values[i]))
        elif nums[i] == 1:
            if not isfirst:
                anime.append(('', '', '', '', ''))
            categ += 1
            anime.append((categs[categ], nums[i], names[i], comments[i], values[i]))
            isfirst = False
    return anime


def csv_write(anime: list, username: str, new: bool) -> None:
    if not new:
        with open(f"{username}'s list 1.csv", 'w') as file:
            names = ['Статус', 'Название', 'Оценка', 'Комментарий']
            file_writer = csv.DictWriter(file, delimiter=";", lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            for a in anime:
                a = list(a)
                if a[4] == '–' or a[4] == '':
                    a[4] = ' '
                file_writer.writerow({'Статус': a[0], 'Название': a[2], 'Оценка': a[4], 'Комментарий': a[3]})
    else:
        for table in range(1, 100):
            if not os.path.exists(f"{username}'s list {table}.csv"):
                with open(f"{username}'s list {table}.csv", 'w') as file:
                    names = ['Статус', 'Название', 'Оценка', 'Комментарий']
                    file_writer = csv.DictWriter(file, delimiter=";", lineterminator="\r", fieldnames=names)
                    file_writer.writeheader()
                    for a in anime:
                        a = list(a)
                        if a[4] == '–' or a[4] == '':
                            a[4] = ' '
                        file_writer.writerow({'Статус': a[0], 'Название': a[2], 'Оценка': a[4], 'Комментарий': a[3]})
                return


def main(user, new=False):

    url = f'https://shikimori.one/{user}/list/anime'
    html = getHTML(url)
    names, nums, cats, comments, values = get_anime_list(html)
    anime = make_tuple(names, nums, cats, comments, values)

    csv_write(anime=anime, username=user, new=new)

    tk.messagebox.showinfo(title='Готово', message='Таблица успешно создана!')
    quit()

