import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Inserire un codice per iniziare: ")

    # Add input control here!

    if int(txtIn) == 1:
        print("OK, quale parola devo aggiungere?")
        txtIn = input()
        entry=tuple(txtIn.split())
        t.handleAdd(entry)
        print ("Aggiunta!")
        txtIn = input("Inserire un codice per continuare: ")

    if int(txtIn) == 2:
        print("OK, quale parola devo Tradurre?")
        txtIn = input()
        print(t.handleTranslate(txtIn))
        print("Tradotta!")
        txtIn = input("Inserire un codice per continuare: ")

    if int(txtIn) == 3:
        print("OK, quale parola devo Tradurre?")
        txtIn = input()
        print(t.handleWildCard(txtIn))
        print("Tradotta!")
        txtIn = input("Inserire un codice per continuare: ")

    if int(txtIn) == 4:
        break