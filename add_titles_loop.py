titles =[]                                                                          #Создаем список
title = (input("Введите заголовок (или оставьте пустым для завершения): "))         #Запрашиваем первый заголовок
if len(title) != 0:                                                                 #Если что-то введено, то продолжаем запрашивать заголовки
    while len(title) != 0:                                                          #Пока заголовки вводятся
        titles.append(title)                                                        #Добавляем заголовок в список
        title = (input("Введите заголовок (или оставьте пустым для завершения): ")) #Вводим новый заголовок
    else:                                                                           #Если пользователь хочет закончить ввод заголовков, то
        print("Ваши заголовки: \n")                                                 #Выводим итог
        for item in titles:                                                         #Каждый элемент(заголовок) в списке titles
            print("-", item, end='\n\n')                                            #Выводится с дефисом через строку
else:                                                                               #Если ни один заголовок не был введен
    print("Заголовок не был введен")                                                #Вывод "Заголовок не был введен"