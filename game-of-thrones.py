from characters import characters
#print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)


# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))

#Printing characters names starting with "A"
# for i in range(len(characters)):
#     print(characters[i]['name'])

# def characters_name_a():
#     name_count = 0
#     for a in range(len(characters)):
#         if characters["name"][0] == "A":
#             name_count = name_count + 1
#     return
# print(characters_name_a())

# letter_input = input('which letter do you want to count?')

# def name_letter_counter():
#     list_of_characters = []
#     for character in characters:
#         if character['name'][0] == letter_input:
#             list_of_characters.append(character['name'])
#     print(len(list_of_characters))

# name_letter_counter()

# 168 name start with A
# 8 names start with Z

# def dead_characters_counter():
#     list_of_dead_characters = []
#     for character in characters:
#         if character['died'] != '':
#             list_of_dead_characters.append(character['name'])
#     print(len(list_of_dead_characters))

# dead_characters_counter()

# 553 dead characters

#Counting most titles

# def most_titles():
#     max_titles = 0
#     max_title_name = ''
#     for character in characters:
#         if(len(character['titles'])>max_titles):
#             max_titles = len(character['titles'])
#             max_title_name = character['name']
#     print(max_title_name)


# most_titles()
# Balon Greyjoy has the most titles

# def valyrian_counter():
#     list_of_valyrian = []
#     for character in characters:
#         if character['culture'] == 'Valyrian':
#             list_of_valyrian.append(character['name'])
#     print(len(list_of_valyrian))

# valyrian_counter()
# 57 Valyrians

# def hot_pie_actor():
#     hot_pie_name = ''
#     for character in characters:
#         if character['name'] == 'Hot Pie':
#             hot_pie_name = character['playedBy']
#     print(hot_pie_name)

# hot_pie_actor()
# Ben Hawkey plays Hot Pie

# def not_tv_count():
#     count = 0
#     for character in characters:
#         if character['playedBy'][0] == '':
#             count = count + 1
#     print(count)

# not_tv_count()
# 1927 characters not on tv

# def name_targaryen():
#     targ_list = []
#     for character in characters:
#         if "Targaryen" in character['name']:
#             targ_list.append(character['name'])
#     print(len(targ_list))

# name_targaryen()
# 49 Targaryens




def make_house_histogram(character_list):
    histogram = {}
    for person in character_list:
        allegiances = person['allegiances']
        for house in allegiances:
            if house in histogram:
                histogram[house] = histogram[house] + 1
            else:
                histogram[house] = 1

    return histogram

print(make_house_histogram(characters))