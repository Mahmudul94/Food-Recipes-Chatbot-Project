# requests: Used to send HTTP requests to web pages.
# BeautifulSoup: Parses the HTML content so we can extract specific elements like links.
from bs4 import BeautifulSoup
import pandas as pd
import logging
import re
from openai import OpenAI
import os
import json
import streamlit as st

#grabe category and recipe name
category_and_recipe = dict()
recipe_ingredients_direction = dict()
recipe_item_dict = {}
allrecipes_existing_json_file = None 

if os.path.exists(r'allrecipe_data.json'):
    with open(r'allrecipe_data.json') as file:
        existing_data = json.load(file)
        allrecipes_existing_json_file = existing_data

#Extract ingredients 
import requests 
from bs4 import BeautifulSoup
def extract_ingredinets (link):
# url ="https://www.allrecipes.com/recipe/23891/grilled-cheese-sandwich/"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("h2", string ='Ingredients')
    ingredients_list = []
    if name:
        for li in name.find_all_next('li', class_='mm-recipes-structured-ingredients__list-item'):
            text = ' '.join(span.text for span in li.find_all('span'))
            ingredients_list.append(text)
    return ingredients_list

import requests 
from bs4 import BeautifulSoup
def extract_direction(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("h2", string ='Directions')
    direction_list =[]
    if name:
        for li in name.find_all_next('p', class_='comp mntl-sc-block mntl-sc-block-html'):
            text = li.get_text(strip=True)
            direction_list.append(text)
    return direction_list

#append the data into dictionary
def final_generate_file (daily_meal_name):
    if daily_meal_name not in allrecipes_existing_json_file:
       allrecipes_existing_json_file[daily_meal_name] =[]
       allrecipes_existing_json_file[daily_meal_name].append(recipe_ingredients_direction)