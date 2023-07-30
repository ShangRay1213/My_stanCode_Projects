"""
File: webcrawler.py
Name: Ray
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        data_list = []
        boy_tags = soup.find_all('td')
        for data in boy_tags:
            text = data.text.split()
            if len(text) == 1:
                data_list.append(text[0])
        text_count = 0
        rank_list = []
        male = ''
        female = ''
        sum_male = 0
        sum_female = 0
        for word in data_list:
            text_count += 1
            rank_list.append(word)
            if text_count % 5 == 0 and text_count <= 1000:
                # male
                for ch in rank_list[2]:
                    if ch.isdigit():
                        male += ch
                sum_male += int(male)
                male = ''
                # female
                for ch in rank_list[4]:
                    if ch.isdigit():
                        female += ch
                sum_female += int(female)
                female = ''
                rank_list = []
        print(f'Male Number: {sum_male}')
        print(f'Female Number: {sum_female}')


if __name__ == '__main__':
    main()
