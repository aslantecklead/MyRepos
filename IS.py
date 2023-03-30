import pyodbc
import inline
from array import *
from colorama import init, Fore, Back, Style

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-K84V7A9L\MYSQLSERVER;DATABASE=Pilaf;Trusted_Connection=yes;'
)

connectionCursor = connection.cursor()
connectionCursor.close()


### Вход в систему ()
def Registration():
    name = input(" Введите ваше имя: ")
    login = input(" Введите логин: ")
    password = input(" Введите пароль: ")
    registerQ = f"insert into dbo.[Buyer] ([Name], [Balance], [Role], [Login], [Password], [Cart], [Position], " \
                f"[PosCount], [DateBuy]) values ('{name}', 0, '', '{login}', \
    '{password}', '', '', 0, '');"
    registerCursor = connection.cursor()
    registerCursor.execute(registerQ)
    connection.commit()
    print()
    print(Fore.GREEN + " Вы успешно зарегестрировались !")
    print(Fore.RESET)
    main()


def EnterAsUser(login, password):
    asUserQ = f"select * from [dbo].[Buyer] where [Role] != 'admin' and [Login] = '{login}' " \
              f"and [Password] = '{password}';"
    userCursor = connection.cursor()
    userCursor.execute(asUserQ)
    if userCursor.rowcount < 0:
        print()
        print(Fore.GREEN + " Вы авторизировались как покупатель !")
        print(Fore.RESET)
        userCursor.close()
        main()
    else:
        EnterAsAdmin(login, password)


def EnterAsAdmin(login, password):
    asAdminQ = f"select * from [dbo].[Buyer] where [Role] = 'admin' and [Login] = '{login}' " \
               f"and [Password] = '{password}';"
    adminCursor = connection.cursor()
    adminCursor.execute(asAdminQ)
    if adminCursor.rowcount == -1:
        print()
        print(Fore.GREEN + " Вы авторизировались как администратор !")
        adminCursor.close()
        print(Fore.WHITE)
        AdminInterface()
    else:
        print()
        print(Fore.RED + " Неверный Логин или пароль!")
        main()
        print(Fore.WHITE)

#Покупка товаров админов Окночание
def ResetAdminBalance(lastBalance):
    balanceUpdateQ = f"update [dbo].[Buyer] set Balance = {lastBalance} where [ID_Buyer] = 1 and [Role] = 'admin'"
    balanceCursor = connection.cursor()
    balanceCursor.execute(balanceUpdateQ)
    connection.commit()
    print(Fore.RED + " Оплата произведена, текущий баланс: ", GetAdminBalance())

### Покупка товаров Админом
def GetRicePrice():
    rice1PriceQ = "select [Rice_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    rice1PriceC = connection.cursor()
    rice1PriceC.execute(rice1PriceQ)
    rice1Price = rice1PriceC.fetchval()
    rice1PriceC.close()

    rice2PriceQ = "select [Rice_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    rice2PriceC = connection.cursor()
    rice2PriceC.execute(rice2PriceQ)
    rice2Price = rice2PriceC.fetchval()
    rice2PriceC.close()

    rice3PriceQ = "select [Rice_3price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    rice3PriceC = connection.cursor()
    rice3PriceC.execute(rice3PriceQ)
    rice3Price = rice3PriceC.fetchval()
    rice3PriceC.close()
    return rice1Price, rice2Price, rice3Price

def GetFruitPrice():
    fruitPriceQ = "select [Fruit_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    fruit1PriceC = connection.cursor()
    fruit1PriceC.execute(fruitPriceQ)
    fruit1Price = fruit1PriceC.fetchval()
    fruit1PriceC.close()

    fruitPriceQ = "select [Fruit_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    fruit2PriceC = connection.cursor()
    fruit2PriceC.execute(fruitPriceQ)
    fruit2Price = fruit2PriceC.fetchval()
    fruit2PriceC.close()

    fruitPriceQ = "select [Fruit_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    fruit3PriceC = connection.cursor()
    fruit3PriceC.execute(fruitPriceQ)
    fruit3Price = fruit3PriceC.fetchval()
    fruit3PriceC.close()

    return fruit1Price, fruit2Price, fruit3Price

def GetTeaPrice():
    teaPriceQ = "select [Tea_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    tea1PriceC = connection.cursor()
    tea1PriceC.execute(teaPriceQ)
    tea1Price = tea1PriceC.fetchval()
    tea1PriceC.close()

    teaPriceQ = "select [Tea_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    tea2PriceC = connection.cursor()
    tea2PriceC.execute(teaPriceQ)
    tea2Price = tea2PriceC.fetchval()
    tea2PriceC.close()

    teaPriceQ = "select [Tea_3price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    tea3PriceC = connection.cursor()
    tea3PriceC.execute(teaPriceQ)
    tea3Price = tea3PriceC.fetchval()
    tea3PriceC.close()

    return tea1Price, tea2Price, tea3Price

def GetPapperPrice():
    papperPriceQ = "select [Papper_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    papper1PriceC = connection.cursor()
    papper1PriceC.execute(papperPriceQ)
    papper1Price = papper1PriceC.fetchval()
    papper1PriceC.close()

    papperPriceQ = "select [Papper_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    papper2PriceC = connection.cursor()
    papper2PriceC.execute(papperPriceQ)
    papper2Price = papper2PriceC.fetchval()
    papper2PriceC.close()

    papperPriceQ = "select [Papper_3price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    papper3PriceC = connection.cursor()
    papper3PriceC.execute(papperPriceQ)
    papper3Price = papper3PriceC.fetchval()
    papper3PriceC.close()

    return papper1Price, papper2Price, papper3Price

def GetSpicesPrice():
    spicesPriceQ = "select [Specties_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    spices1PriceC = connection.cursor()
    spices1PriceC.execute(spicesPriceQ)
    spices1Price = spices1PriceC.fetchval()
    spices1PriceC.close()

    spicesPriceQ = "select [Specties_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    spices2PriceC = connection.cursor()
    spices2PriceC.execute(spicesPriceQ)
    spices2Price = spices2PriceC.fetchval()
    spices2PriceC.close()

    spicesPriceQ = "select [Specties_3price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    spices3PriceC = connection.cursor()
    spices3PriceC.execute(spicesPriceQ)
    spices3Price = spices3PriceC.fetchval()
    spices3PriceC.close()

    return spices1Price, spices2Price, spices3Price

def GetOnionPrice():
    onionPriceQ = "select [Onion_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    onion1PriceC = connection.cursor()
    onion1PriceC.execute(onionPriceQ)
    onion1Price = onion1PriceC.fetchval()
    onion1PriceC.close()

    onionPriceQ = "select [Onion_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    onion2PriceC = connection.cursor()
    onion2PriceC.execute(onionPriceQ)
    onion2Price = onion2PriceC.fetchval()
    onion2PriceC.close()

    onionPriceQ = "select [Onion_3price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    onion3PriceC = connection.cursor()
    onion3PriceC.execute(onionPriceQ)
    onion3Price = onion3PriceC.fetchval()
    onion3PriceC.close()

    return onion1Price, onion2Price, onion3Price

def GetCarrotPrice():
    carrotPriceQ = "select [Carrot_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    carrot1PriceC = connection.cursor()
    carrot1PriceC.execute(carrotPriceQ)
    carrot1Price = carrot1PriceC.fetchval()
    carrot1PriceC.close()

    carrotPriceQ = "select [Carrot_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    carrot2PriceC = connection.cursor()
    carrot2PriceC.execute(carrotPriceQ)
    carrot2Price = carrot2PriceC.fetchval()
    carrot2PriceC.close()

    carrotPriceQ = "select [Carrot_3price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    carrot3PriceC = connection.cursor()
    carrot3PriceC.execute(carrotPriceQ)
    carrot3Price = carrot3PriceC.fetchval()
    carrot3PriceC.close()
    return carrot1Price, carrot2Price, carrot3Price

def GetMeatPrice():
    meat1PriceQ = "select [Meat_1price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    meat1PriceC = connection.cursor()
    meat1PriceC.execute(meat1PriceQ)
    meat1Price = meat1PriceC.fetchval()
    meat1PriceC.close()

    meat2PriceQ = "select [Meat_2price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    meat2PriceC = connection.cursor()
    meat2PriceC.execute(meat2PriceQ)
    meat2Price = meat2PriceC.fetchval()
    meat2PriceC.close()

    meat3PriceQ = "select [Meat_3price] from [dbo].[Products] inner join dbo.[Products_Price] on [Products_Price_ID] = [ID_Products]"
    meat3PriceC = connection.cursor()
    meat3PriceC.execute(meat3PriceQ)
    meat3Price = meat3PriceC.fetchval()
    meat3PriceC.close()
    return meat1Price, meat2Price, meat3Price


def RiceType():
    print(" Раздел: Рис ")
    rice1Price, rice2Price, rice3Price = GetRicePrice()
    riceType = float(input(f" Выберите сорт риса: \n"
                         f"   1. Басмати - {rice1Price} руб\n"
                         f"   2. Жасмин - {rice2Price} руб\n"
                         f"   3. Длиннозерный рис - {rice3Price} руб\n"
                         f"   0. Выход\n"))
    if riceType == 1:
        kgValue = float(input(" Введитье объем риса Басмати в (кг): "))
        name = "Басмати"
        return kgValue, kgValue * rice1Price, name
    elif riceType == 2:
        kgValue = float(input(" Введитье объем (кг): "))
        name = "Жасмин"
        return kgValue, kgValue * rice2Price, name
    elif riceType == 3:
        kgValue = float(input(" Введитье объем (кг): "))
        name = "Длиннозерный рис"
        return kgValue, kgValue * rice3Price, name
    elif riceType == 0:
        AdminBuyProducts()

def TeaType():
    print(" Раздел: Чай ")
    tea1Price, tea2Price, tea3Price = GetTeaPrice()
    teaType = int(input(f" Выберите специю: \n"
                          f"   1. Зеленый - {tea1Price} руб\n"
                          f"   2. Черный - {tea2Price} руб\n"
                          f"   3. Улун  - {tea3Price} руб\n"
                          f"   0. Выход\n"))
    if teaType == 1:
        kgValue = float(input(" Введитье объем Зеленого чая (кг): "))
        name = "Зеленый"
        return kgValue, kgValue * tea1Price, name
    elif teaType == 2:
        kgValue = float(input(" Введитье объем Черного чая (кг): "))
        name = "Черный"
        return kgValue, kgValue * tea2Price, name
    elif teaType == 3:
        kgValue = float(input(" Введитье объем чая Улун (кг): "))
        name = "Улун"
        return kgValue, kgValue * tea3Price, name
    elif teaType == 0:
        AdminBuyProducts()

def PapperType():
    print(" Раздел: Специи ")
    papper1Price, papper2Price, papper3Price = GetPapperPrice()
    papperType = int(input(f" Выберите специю: \n"
                          f"   1. Чили - {papper1Price} руб\n"
                          f"   2. Черный - {papper2Price} руб\n"
                          f"   3. Молотый  - {papper3Price} руб\n"
                          f"   0. Выход\n"))
    if papperType == 1:
        kgValue = float(input(" Введитье объем Зиры (кг): "))
        name = "Чили"
        return kgValue, kgValue * papper1Price, name
    elif papperType == 2:
        kgValue = float(input(" Введитье объем Чеснока (кг): "))
        name = "Черный"
        return kgValue, kgValue * papper2Price, name
    elif papperType == 3:
        kgValue = float(input(" Введитье объем Перца (кг): "))
        name = "Молотый"
        return kgValue, kgValue * papper3Price, name
    elif papperType == 0:
        AdminBuyProducts()

def SpicesType():
    print(" Раздел: Специи ")
    spices1Price, spices2Price, spices3Price = GetSpicesPrice()
    fruitType = int(input(f" Выберите специю: \n"
                          f"   1. Зира - {spices1Price} руб\n"
                          f"   2. Чеснок - {spices2Price} руб\n"
                          f"   3. Перец  - {spices3Price} руб\n"
                          f"   0. Выход\n"))
    if fruitType == 1:
        kgValue = float(input(" Введитье объем Зиры (кг): "))
        name = "Зира"
        return kgValue, kgValue * spices1Price, name
    elif fruitType == 2:
        kgValue = float(input(" Введитье объем Чеснока (кг): "))
        name = "Чеснок"
        return kgValue, kgValue * spices2Price, name
    elif fruitType == 3:
        kgValue = float(input(" Введитье объем Перца (кг): "))
        name = "Перец"
        return kgValue, kgValue * spices3Price, name
    elif fruitType == 0:
        AdminBuyProducts()

def FruitType():
    print(" Раздел: Сухофрукты ")
    fruit1Price, fruit2Price, fruit3Price = GetFruitPrice()
    fruitType = int(input(f" Выберите сухофрукт: \n"
                          f"   1. Курага - {fruit1Price} руб\n"
                          f"   2. Изюм - {fruit2Price} руб\n"
                          f"   3. Чернослив  - {fruit3Price} руб\n"
                          f"   0. Выход\n"))
    if fruitType == 1:
        kgValue = float(input(" Введитье объем Кураги (кг): "))
        name = "Курага"
        return kgValue, kgValue * fruit1Price, name
    elif fruitType == 2:
        kgValue = float(input(" Введитье объем Изюма (кг): "))
        name = "Изюм"
        return kgValue, kgValue * fruit2Price, name
    elif fruitType == 3:
        kgValue = float(input(" Введитье объем Чернослива (кг): "))
        name = "Чернослив"
        return kgValue, kgValue * fruit3Price, name
    elif fruitType == 0:
        AdminBuyProducts()

def OnoionType():
    print(" Раздел: Мяско ")
    onion1Price, onion2Price, onion3Price = GetOnionPrice()
    onionType = int(input(f" Выберите лук: \n"
                         f"   1. Севок - {onion1Price} руб\n"
                         f"   2. Голландский озимый - {onion2Price} руб\n"
                         f"   3. Шалот - {onion3Price} руб\n"
                         f"   0. Выход\n"))
    if onionType == 1:
        kgValue = float(input(" Введитье объем лука Севок в (кг): "))
        name = "Севок"
        return kgValue, kgValue * onion1Price, name
    elif onionType == 2:
        kgValue = float(input(" Введитье объем лука Голландский озимый (кг): "))
        name = "Голландский озимый"
        return kgValue, kgValue * onion2Price, name
    elif onionType == 3:
        kgValue = float(input(" Введитье объем лука Шалот (кг): "))
        name = "Шалот"
        return kgValue, kgValue * onion3Price, name
    elif onionType == 0:
        AdminBuyProducts()

def CarrotType():
    print(" Раздел: Морковь ")
    carrot1Price, carrot2Price, carrot3Price = GetCarrotPrice()
    meatType = int(input(f" Выберите морковь: \n"
                         f"   1. Корейская - {carrot1Price} руб\n"
                         f"   2. Красная - {carrot2Price} руб\n"
                         f"   3. Русская - {carrot3Price} руб\n"
                         f"   0. Выход \n"))
    if meatType == 1:
        kgValue = float(input(" Введитье объем Корейской моркови в (кг): "))
        name = "Корейская"
        return kgValue, kgValue * carrot1Price, name
    elif meatType == 2:
        kgValue = float(input(" Введитье объем красной моркови (кг): "))
        name = "Красная"
        return kgValue, kgValue * carrot2Price, name
    elif meatType == 3:
        kgValue = float(input(" Введитье объем Русской моркови (кг): "))
        name = "Русская"
        return kgValue, kgValue * carrot3Price, name
    elif meatType == 4:
        AdminBuyProducts()

def MeatType():
    print(" Раздел: Мяско ")
    meat1Price, meat2Price, meat3Price = GetMeatPrice()
    meatType = int(input(f" Выберите мясо: \n"
                         f"   1. Баранина - {meat1Price} руб\n"
                         f"   2. Говьяяядина - {meat2Price} руб\n"
                         f"   3. Курица - {meat3Price} руб\n"
                         f"   0. Выход \n"))
    if meatType == 1:
        kgValue = float(input(" Введитье объем Баранины в (кг): "))
        name = "Баранина"
        return kgValue, kgValue * meat1Price, name
    elif meatType == 2:
        kgValue = float(input(" Введитье объем Говядины (кг): "))
        name = "Говядина"
        return kgValue, kgValue * meat2Price, name
    elif meatType == 3:
        kgValue = float(input(" Введитье объем Курицы (кг): "))
        name = "Курица"
        return kgValue, kgValue * meat3Price, name
    elif meatType == 0:
        AdminBuyProducts()


def SetRicePrice():
    print(" Раздел: Рис ")
    rice1Price, rice2Price, rice3Price = GetRicePrice()
    riceType = int(input(f" Выберите сорт риса: \n"
                         f"   1. Басмати - {rice1Price} руб\n"
                         f"   2. Жасмин - {rice2Price} руб\n"
                         f"   3. Длиннозерный рис - {rice3Price} руб\n"
                         f"   0. Выход\n"))
    if riceType == 1:
        rubValue = float(input(" Введитье новую цену риса Басмати в (руб): "))
        name = "Басмати"
        return rubValue, name
    elif riceType == 2:
        rubValue = float(input(" Введитье новую цену риса Жасмин в (руб): "))
        name = "Жасмин"
        return rubValue, name
    elif riceType == 3:
        rubValue = float(input(" Введитье новую цену Длиннозернового риса в (руб): "))
        name = "Длиннозерный рис"
        return rubValue, name
    elif riceType == 0:
        AdminChangesPrices()

def SetMeatPrice():
    print(" Раздел: Мяско ")
    meat1Price, meat2Price, meat3Price = GetMeatPrice()
    meatType = int(input(f" Выберите мясо: \n"
                         f"   1. Баранина - {meat1Price} руб\n"
                         f"   2. Говьяяядина - {meat2Price} руб\n"
                         f"   3. Курица - {meat3Price} руб\n"
                         f"   0. Выход \n"))
    if meatType == 1:
        rubValue = float(input(" Введитье новую цену Баранины в (руб): "))
        name = "Баранина"
        return rubValue, name
    elif meatType == 2:
        rubValue = float(input(" Введитье новую цену Говядины (руб): "))
        name = "Говядина"
        return rubValue, name
    elif meatType == 3:
        rubValue = float(input(" Введитье новую цену Курицы (руб): "))
        name = "Курица"
        return rubValue, name
    elif meatType == 0:
        AdminChangesPrices()

def SetPapperPrice():
    print(" Раздел: Специи ")
    papper1Price, papper2Price, papper3Price = GetPapperPrice()
    papperType = int(input(f" Выберите специю: \n"
                          f"   1. Чили - {papper1Price} руб\n"
                          f"   2. Черный - {papper2Price} руб\n"
                          f"   3. Молотый  - {papper3Price} руб\n"
                          f"   0. Выход\n"))
    if papperType == 1:
        kgValue = float(input(" Введитье новую цену Зиры (руб): "))
        name = "Чили"
        return kgValue, name
    elif papperType == 2:
        kgValue = float(input(" Введитье новую цену Чеснока (руб): "))
        name = "Черный"
        return kgValue, name
    elif papperType == 3:
        kgValue = float(input(" Введитье новую цену Перца (руб): "))
        name = "Молотый"
        return kgValue, name
    elif papperType == 0:
        AdminChangesPrices()

def SetSpeciesPrice():
    print(" Раздел: Специи ")
    spices1Price, spices2Price, spices3Price = GetSpicesPrice()
    fruitType = int(input(f" Выберите специю: \n"
                          f"   1. Зира - {spices1Price} руб\n"
                          f"   2. Чеснок - {spices2Price} руб\n"
                          f"   3. Перец  - {spices3Price} руб\n"
                          f"   0. Выход\n"))
    if fruitType == 1:
        kgValue = float(input(" Введитье новую ценум Зиры (руб): "))
        name = "Зира"
        return kgValue, name
    elif fruitType == 2:
        kgValue = float(input(" Введитье новую ценум Чеснока (руб): "))
        name = "Чеснок"
        return kgValue,name
    elif fruitType == 3:
        kgValue = float(input(" Введитье новую ценум Перца (руб): "))
        name = "Перец"
        return kgValue, name
    elif fruitType == 0:
        AdminChangesPrices()

def SetFruitPrice():
    print(" Раздел: Сухофрукты ")
    fruit1Price, fruit2Price, fruit3Price = GetFruitPrice()
    fruitType = int(input(f" Выберите сухофрукт: \n"
                          f"   1. Курага - {fruit1Price} руб\n"
                          f"   2. Изюм - {fruit2Price} руб\n"
                          f"   3. Чернослив  - {fruit3Price} руб\n"
                          f"   0. Выход\n"))
    if fruitType == 1:
        kgValue = float(input(" Введитье новую цену Кураги (руб): "))
        name = "Курага"
        return kgValue, name
    elif fruitType == 2:
        kgValue = float(input(" Введитье новую цену Изюма (руб): "))
        name = "Изюм"
        return kgValue, name
    elif fruitType == 3:
        kgValue = float(input(" Введитье новую цену Чернослива (руб): "))
        name = "Чернослив"
        return kgValue, name
    elif fruitType == 0:
        AdminChangesPrices()

def SetOnionPrice():
    print(" Раздел: Мяско ")
    onion1Price, onion2Price, onion3Price = GetOnionPrice()
    onionType = int(input(f" Выберите лук: \n"
                         f"   1. Севок - {onion1Price} руб\n"
                         f"   2. Голландский озимый - {onion2Price} руб\n"
                         f"   3. Шалот - {onion3Price} руб\n"
                         f"   0. Выход\n"))
    if onionType == 1:
        kgValue = float(input(" Введитье новую цену лука Севок в (руб): "))
        name = "Севок"
        return kgValue, name
    elif onionType == 2:
        kgValue = float(input(" Введитье новую цену лука Голландский озимый (руб): "))
        name = "Голландский озимый"
        return kgValue, name
    elif onionType == 3:
        kgValue = float(input(" Введитье новую цену лука Шалот (руб): "))
        name = "Шалот"
        return kgValue, name
    elif onionType == 0:
        AdminChangesPrices()

def SetCarrotPrice():
    print(" Раздел: Морковь ")
    carrot1Price, carrot2Price, carrot3Price = GetCarrotPrice()
    meatType = int(input(f" Выберите морковь: \n"
                         f"   1. Корейская - {carrot1Price} руб\n"
                         f"   2. Красная - {carrot2Price} руб\n"
                         f"   3. Русская - {carrot3Price} руб\n"
                         f"   0. Выход \n"))
    if meatType == 1:
        kgValue = float(input(" Введитье новую цену Корейской моркови в (руб): "))
        name = "Корейская"
        return kgValue, name
    elif meatType == 2:
        kgValue = float(input(" Введитье новую цену красной моркови (руб): "))
        name = "Красная"
        return kgValue, name
    elif meatType == 3:
        kgValue = float(input(" Введитье новую цену Русской моркови (руб): "))
        name = "Русская"
        return kgValue, name
    elif meatType == 4:
        AdminChangesPrices()

def SetOnoionPrice():
    print(" Раздел: Мяско ")
    onion1Price, onion2Price, onion3Price = GetOnionPrice()
    onionType = int(input(f" Выберите лук: \n"
                         f"   1. Севок - {onion1Price} руб\n"
                         f"   2. Голландский озимый - {onion2Price} руб\n"
                         f"   3. Шалот - {onion3Price} руб\n"
                         f"   0. Выход\n"))
    if onionType == 1:
        kgValue = float(input(" Введитье новую цену Севок в (руб): "))
        name = "Севок"
        return kgValue, name
    elif onionType == 2:
        kgValue = float(input(" Введитье новую цену Голландский озимый (руб): "))
        name = "Голландский озимый"
        return kgValue, name
    elif onionType == 3:
        kgValue = float(input(" Введитье новую цену лука Шалот (руб): "))
        name = "Шалот"
        return kgValue, name
    elif onionType == 0:
        AdminChangesPrices()

def SetTeaPrice():
    print(" Раздел: Чай ")
    tea1Price, tea2Price, tea3Price = GetTeaPrice()
    teaType = int(input(f" Выберите специю: \n"
                          f"   1. Зеленый - {tea1Price} руб\n"
                          f"   2. Черный - {tea2Price} руб\n"
                          f"   3. Улун  - {tea3Price} руб\n"
                          f"   0. Выход\n"))
    if teaType == 1:
        kgValue = float(input(" Введитье новую цену Зеленого чая (руб): "))
        name = "Зеленый"
        return kgValue, name
    elif teaType == 2:
        kgValue = float(input(" Введитье новую цену Черного чая (руб): "))
        name = "Черный"
        return kgValue, name
    elif teaType == 3:
        kgValue = float(input(" Введитье новую цену чая Улун (руб): "))
        name = "Улун"
        return kgValue, name
    elif teaType == 0:
        AdminChangesPrices()

selectProducts = {'ID_Products': 1, 'Rice_1': 0, 'Rice_2': 0, 'Rice_3': 0, 'Meat_1': 0, 'Meat_2': 0, 'Meat_3': 0,
                    'Carrot_1': 0, 'Carrot_2': 0, 'Carrot_3': 0, 'Onion_1': 0, 'Onion_2': 0, 'Onion_3': 0,
                    'Fruit_1': 0, 'Fruit_2': 0, 'Fruit_3': 0, 'Specties_1': 0, 'Specties_2': 0, 'Specties_3': 0,
                    'Papper_1': 0, 'Papper_2': 0, 'Papper_3': 0, 'Tea_1': 0, 'Tea_2': 0, 'Tea_3': 0}

def RefreshSysDictionary(prod):
    prodQ = f"select * from [dbo].[Products];"
    prodCursor = connection.cursor()
    prod = prodCursor.execute(prodQ)
    connection.commit()
    return prod


def SetAllProducts(prod):
    prodListQ = f"update dbo.[Products] set [Rice_1] = {prod['Rice_1']}, [Rice_2] = {prod['Rice_1']}, [Rice_3] = {prod['Rice_3']}, " \
                f"[Meat_1] = {prod['Meat_1']}, [Meat_2] = {prod['Meat_2']}, [Meat_3] = {prod['Meat_3']}, [Carrot_1] = {prod['Carrot_1']}, " \
                f"[Carrot_2] = {prod['Carrot_2']}, [Carrot_3] = {prod['Carrot_3']}, [Onion_1] = {prod['Onion_1']}, " \
                f"[Onion_2] = {prod['Onion_2']}, [Onion_3] = {prod['Onion_2']}, [Fruit_1] = {prod['Fruit_1']}, [Fruit_2] = {prod['Fruit_2']}," \
                f" [Fruit_3] = {prod['Fruit_3']}, [Specties_1] = {prod['Specties_1']}, [Specties_2] = {prod['Specties_2']}," \
                f" [Specties_3] = {prod['Specties_3']}, [Papper_1] = {prod['Papper_1']}, [Papper_2] = {prod['Papper_2']}, " \
                f"[Papper_3] = {prod['Papper_3']}, [Tea_1] = {prod['Tea_1']}, [Tea_2] = {prod['Tea_2']}, [Tea_3] = {prod['Tea_3']} " \
                f"where dbo.[Products].[ID_Products] = 1"
    prodListCursor = connection.cursor()
    prodListCursor.execute(prodListQ)
    connection.commit()
    RefreshSysDictionary(selectProducts)
    AdminInterface()

selectProductsPrices = {'ID_Products_Price': 1, 'Rice_1price': 0, 'Rice_2price': 0, 'Rice_3price': 0, 'Meat_1price': 0, 'Meat_2price': 0, 'Meat_3price': 0,
                    'Carrot_1price': 0, 'Carrot_2price': 0, 'Carrot_3price': 0, 'Onion_1price': 0, 'Onion_2price': 0, 'Onion_3price': 0,
                    'Fruit_1price': 0, 'Fruit_2price': 0, 'Fruit_3price': 0, 'Specties_1price': 0, 'Specties_2price': 0, 'Specties_3price': 0,
                    'Papper_1price': 0, 'Papper_2price': 0, 'Papper_3price': 0, 'Tea_1price': 0, 'Tea_2price': 0, 'Tea_3price': 0}

def GetPriceFromDB():
    prodListCursor = connection.cursor()
    prodListCursor.execute("select * from [dbo].[Products_Price]")
    for row in prodListCursor.fetchall():
        selectProductsPrices['ID_Products_Price'] = 1
        selectProductsPrices['Rice_1price'] = row[1]
        selectProductsPrices['Rice_2price'] = row[2]
        selectProductsPrices['Rice_3price'] = row[3]
        selectProductsPrices['Meat_1price'] = row[4]
        selectProductsPrices['Meat_2price'] = row[5]
        selectProductsPrices['Meat_3price'] = row[6]
        selectProductsPrices['Carrot_1price'] = row[7]
        selectProductsPrices['Carrot_2price'] = row[8]
        selectProductsPrices['Carrot_3price'] = row[9]
        selectProductsPrices['Onion_1price'] = row[10]
        selectProductsPrices['Onion_2price'] = row[11]
        selectProductsPrices['Onion_3price'] = row[12]
        selectProductsPrices['Fruit_1price'] = row[13]
        selectProductsPrices['Fruit_2price'] = row[14]
        selectProductsPrices['Fruit_3price'] = row[15]
        selectProductsPrices['Specties_1price'] = row[16]
        selectProductsPrices['Specties_2price'] = row[17]
        selectProductsPrices['Specties_3price'] = row[18]
        selectProductsPrices['Papper_1price'] = row[19]
        selectProductsPrices['Papper_2price'] = row[20]
        selectProductsPrices['Papper_3price'] = row[21]
        selectProductsPrices['Tea_1price'] = row[22]
        selectProductsPrices['Tea_2price'] = row[23]
        selectProductsPrices['Tea_3price'] = row[24]
    return selectProductsPrices  # возвращаем словарь


def SetAllProductsPrice(prod):
    prodListQ = f"update dbo.[Products_Price] set [Rice_1price] = {prod['Rice_1price']}, [Rice_2price] = {prod['Rice_2price']}, " \
                f"[Rice_3price] = {prod['Rice_3price']}, [Meat_1price] = {prod['Meat_1price']}, [Meat_2price] = {prod['Meat_2price']}, " \
                f"[Meat_3price] = {prod['Meat_3price']}, [Carrot_1price] = {prod['Carrot_1price']}, [Carrot_2price] = {prod['Carrot_2price']}, " \
                f"[Carrot_3price] = {prod['Carrot_3price']}, [Onion_1price] = {prod['Onion_1price']}, [Onion_2price] = {prod['Onion_2price']}, " \
                f"[Onion_3price] = {prod['Onion_3price']},  [Fruit_1price] = {prod['Fruit_1price']}, [Fruit_2price] = {prod['Fruit_2price']}, " \
                f"[Fruit_3price] = {prod['Fruit_3price']}, [Specties_1price] = {prod['Specties_1price']}, [Specties_2price] = {prod['Specties_2price']}, " \
                f"[Specties_3price] = {prod['Specties_3price']}, [Papper_1price] = {prod['Papper_1price']}, [Papper_2price] = {prod['Papper_2price']}, " \
                f"[Papper_3price] = {prod['Papper_3price']}, [Tea_1price] = {prod['Tea_1price']}, [Tea_2price] = {prod['Tea_2price']}, " \
                f"[Tea_3price] = {prod['Tea_3price']} where [Products_Price].[ID_Products_Price] = 1"
    prodListCursor = connection.cursor()
    prodListCursor.execute(prodListQ)
    connection.commit()
    RefreshSysDictionary(selectProducts)
    AdminInterface()

def ResetProductsPrices(intRub, strName):
    if strName == "Басмати":
        selectProductsPrices["Rice_1price"] =+ intRub
    if strName == "Жасмин":
        selectProducts["Rice_2price"] =+ intRub
    if strName == "Длиннозерный рис":
        selectProductsPrices["Rice_3price"] =+ intRub
    if strName == "Баранина":
        selectProductsPrices['Meat_1price'] =+ intRub
    if strName == "Говьяяядина":
        selectProductsPrices['Meat_2price'] =+ intRub
    if strName == "Курица":
        selectProductsPrices['Meat_3price'] =+ intRub
    if strName == "Корейская":
        selectProductsPrices['Carrot_1price'] =+ intRub
    if strName == "Красная":
        selectProductsPrices['Carrot_2price'] =+ intRub
    if strName == "Русская":
        selectProductsPrices['Carrot_3price'] =+ intRub
    if strName == "Севок":
        selectProducts['Onion_1price'] =+ intRub
    if strName == "Голландский озимый":
        selectProducts['Onion_2price'] =+ intRub
    if strName == "Шалот":
        selectProducts['Onion_3price'] =+ intRub
    if strName == "Курага":
        selectProductsPrices['Fruit_1price'] =+ intRub
    if strName == "Изюм":
        selectProductsPrices['Fruit_2price'] =+ intRub
    if strName == "Чернослив":
        selectProductsPrices['Fruit_3price'] =+ intRub
    if strName == "Зира":
        selectProductsPrices['Specties_1price'] =+ intRub
    if strName == "Чеснок":
        selectProductsPrices['Specties_2price'] =+ intRub
    if strName == "Перец":
        selectProductsPrices['Specties_3price'] =+ intRub
    if strName == "Чили":
        selectProductsPrices['Papper_1price'] =+ intRub
    if strName == "Черный":
        selectProductsPrices['Papper_2price'] =+ intRub
    if strName == "Молотый":
        selectProductsPrices['Papper_3price'] =+ intRub
    if strName == "Зеленый":
        selectProductsPrices['Tea_1price'] =+ intRub
    if strName == "Черный":
        selectProductsPrices['Tea_2price'] =+ intRub
    if strName == "Улун":
        selectProductsPrices['Tea_3price'] =+ intRub


def ResetProductCount(intKg, strName):
    if strName == "Басмати":
        selectProducts["Rice_1"] =+ intKg
    if strName == "Жасмин":
        selectProducts["Rice_2"] =+ intKg
    if strName == "Длиннозерный рис":
        selectProducts["Rice_3"] =+ intKg
    if strName == "Баранина":
        selectProducts['Meat_1'] =+ intKg
    if strName == "Говьяяядина":
        selectProducts['Meat_2'] =+ intKg
    if strName == "Курица":
        selectProducts['Meat_3'] =+ intKg
    if strName == "Корейская":
        selectProducts['Carrot_1'] =+ intKg
    if strName == "Красная":
        selectProducts['Carrot_2'] =+ intKg
    if strName == "Русская":
        selectProducts['Carrot_3'] =+ intKg
    if strName == "Севок":
        selectProducts['Carrot_1'] =+ intKg
    if strName == "Голландский озимый":
        selectProducts['Carrot_2'] =+ intKg
    if strName == "Шалот":
        selectProducts['Carrot_3'] =+ intKg
    if strName == "Курага":
        selectProducts['Fruit_1'] =+ intKg
    if strName == "Изюм":
        selectProducts['Fruit_2'] =+ intKg
    if strName == "Чернослив":
        selectProducts['Fruit_3'] =+ intKg
    if strName == "Зира":
        selectProducts['Specties_1'] =+ intKg
    if strName == "Чеснок":
        selectProducts['Specties_2'] =+ intKg
    if strName == "Перец":
        selectProducts['Specties_3'] =+ intKg
    if strName == "Чили":
        selectProducts['Papper_1'] =+ intKg
    if strName == "Черный":
        selectProducts['Papper_2'] =+ intKg
    if strName == "Молотый":
        selectProducts['Papper_3'] =+ intKg
    if strName == "Зеленый":
        selectProducts['Tea_1'] =+ intKg
    if strName == "Черный":
        selectProducts['Tea_2'] =+ intKg
    if strName == "Улун":
        selectProducts['Tea_3'] =+ intKg


def GetAdminBalance():
    getBalanceQ = "select [Balance] from [dbo].[Buyer] where [Role] = 'admin'"
    balanceCursor = connection.cursor()
    balanceCursor.execute(getBalanceQ)
    balanceRecord = balanceCursor.fetchval()
    return balanceRecord


price = array('i', [])
currentBalance = array('i', [0])


def AdminChangesPrices():
    productCategory = int(input(" Цену какой категории вы хотите изменить ? : \n"
                                "   1. Рис \n"
                                "   2. Мясо \n"
                                "   3. Морковь \n"
                                "   4. Лук \n"
                                "   5. Сухофрукт \n"
                                "   6. Специя \n"
                                "   7. Перец \n"
                                "   8. Чай \n"
                                "   0. Изменить всю цену \n"))
    if productCategory >= 1 or productCategory <= 8 or productCategory == 99 or productCategory == 0:
        if productCategory == 0:
            print(
                Fore.GREEN + f" Цена изменена " + Fore.WHITE)
            list = GetPriceFromDB(selectProductsPrices)
            SetAllProductsPrice(list)
        elif productCategory == 1:
            rubRice, name = SetRicePrice()
            print("")
            print(Fore.GREEN + f" Новая цена за рис {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        elif productCategory == 2:
            rubRice, name = SetMeatPrice()
            print("")
            print(Fore.GREEN + f" Новая цена за мясо {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        elif productCategory == 3:
            rubRice, name = SetCarrotPrice()
            print("")
            print(Fore.GREEN + f" Новая цена за мясо {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        elif productCategory == 4:
            rubRice, name = SetOnionPrice()
            print("")
            print(Fore.GREEN + f" Новая цена за лук {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        elif productCategory == 5:
            rubRice, name = SetFruitPrice()
            print("")
            print(Fore.GREEN + f" Новая цена за сухофрукт {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        elif productCategory == 6:
            rubRice, name = SetSpeciesPrice()
            print("")
            print(Fore.GREEN + f" Новая цена за специю {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        elif productCategory == 7:
            rubRice, name = SetPapperPrice()
            print("")
            print(Fore.GREEN + f" Новая цена за перец {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        elif productCategory == 8:
            rubRice, name = SetTeaPrice()
            print("")
            print(Fore.GREEN + f" Новая цена за чай {name}: {rubRice} рублей" + Fore.WHITE)
            ResetProductsPrices(rubRice, name)
        AdminChangesPrices()


def AdminBuyProducts():
    balance = GetAdminBalance()
    currentBalance[0] = balance - sum(price)
    print(Fore.GREEN + f" Общая цена закупки: {sum(price)} рублей " + Fore.WHITE)
    print(Fore.GREEN + f" Остаточный баланс администратора: {currentBalance[0]} рублей " + Fore.WHITE)
    if currentBalance[0] >= 0:
        productCategory = int(input(" Выберите категорию продукта: \n"
                                    "   1. Рис \n"
                                    "   2. Мясо \n"
                                    "   3. Морковь \n"
                                    "   4. Лук \n"
                                    "   5. Сухофрукт \n"
                                    "   6. Специя \n"
                                    "   7. Перец \n"
                                    "   8. Чай \n"
                                    "   0. Произвести оплату товаров \n"))
        if productCategory >= 1 or productCategory <=8 or productCategory == 99 or productCategory == 0:
            if productCategory == 0:
                lastBalance = currentBalance[0]
                ResetAdminBalance(lastBalance)
                SetAllProducts(selectProducts)
            elif productCategory == 99:
                print(
                    Fore.GREEN + f" Оплата не произведена, баланс - {GetAdminBalance()} рублей остался неизменным " + Fore.WHITE)
                currentBalance[0] = GetAdminBalance()
                price.remove(price[0])
                main()
            elif productCategory == 1:
                kgRice, ricePrice, name = RiceType()
                print("")
                print(Fore.GREEN + f" Цена за рис {name}: {ricePrice} рублей")
                price.append(ricePrice)
                ResetProductCount(kgRice, name)
            elif productCategory == 2:
                kgMeat, meatPrice, name = MeatType()
                print("")
                print(Fore.GREEN + f" Цена за мясо {name}: {meatPrice} рублей")
                price.append(meatPrice)
                ResetProductCount(kgMeat, name)
            elif productCategory == 3:
                kgCarrot, carrotPrice, name = CarrotType()
                print("")
                print(Fore.GREEN + f" Цена за морковь {name}: {carrotPrice} рублей")
                price.append(carrotPrice)
                ResetProductCount(kgCarrot, name)
            elif productCategory == 4:
                kgOnion, onionPrice, name = OnoionType()
                print("")
                print(Fore.GREEN + f" Цена за лук {name}: {onionPrice} рублей")
                price.append(onionPrice)
                ResetProductCount(kgOnion, name)
            elif productCategory == 5:
                kgFruit, fruitPrice, name = FruitType()
                print("")
                print(Fore.GREEN + f" Цена за сухофрукт {name}: {fruitPrice} рублей")
                price.append(fruitPrice)
                ResetProductCount(kgFruit, name)
            elif productCategory == 6:
                kgSpices, spicesPrice, name = SpicesType()
                print("")
                print(Fore.GREEN + f" Цена за специю {name}: {spicesPrice} рублей")
                price.append(spicesPrice)
                ResetProductCount(kgSpices, name)
            elif productCategory == 7:
                kgPapper, papperPrice, name = PapperType()
                print("")
                print(Fore.GREEN + f" Цена за перец {name}: {papperPrice} рублей")
                price.append(papperPrice)
                ResetProductCount(kgPapper, name)
            elif productCategory == 8:
                kgTea, teaPrice, name = TeaType()
                print("")
                print(Fore.GREEN + f" Цена за чай {name}: {teaPrice} рублей")
                price.append(teaPrice)
                ResetProductCount(kgTea, name)
            AdminBuyProducts()
            print("")
        elif sum(price) > GetAdminBalance():
            print(
                Fore.RED + " Баланс нулевой, реализуйте товар чтобы заработать больше денег и возврщайтесь " + Fore.WHITE)
            AdminInterface()
        else:
            print(
                Fore.RED + f" Введите число строго в диапазоне ! " + Fore.WHITE)
            AdminBuyProducts()


## Интерфейс Админа
def AdminInterface():
    print(Fore.GREEN + f" Баланс администратора - {GetAdminBalance()} рублей " + Fore.WHITE)
    adminAction = int(input(" Выберите дейсвтие: \n"
                            "   1. Закупить товары \n"
                            "   2. Изменить цену продукта \n"
                            "   3. Выход \n"))
    if adminAction == 1:
        AdminBuyProducts()
        print("")
    elif adminAction == 2:
        AdminChangesPrices()
        print("")
    elif adminAction == 3:
        main()
        print("")


## Точка входа
print()
print(" Добро пожаловать в обитель плова 'Восточное гостеприимство' ")


def main():
    authOrReg = int(input(" Выберите дейсвтие: \n"
                          "   1. Авторизация \n"
                          "   2. Регистрация \n"
                          "   3. Админ\n"))
    if authOrReg == 1:
        login = str(input(" Введите логин: "))
        password = str(input(" Введите пароль: "))
        EnterAsUser(login, password)
    elif authOrReg == 2:
        Registration()
    elif authOrReg == 3:
        AdminInterface()


main()