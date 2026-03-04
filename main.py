import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("filename.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("OK, quale parola devo aggiungere?")
        txtIn = input()
        entry=tuple(input.split())
        t.handleAdd(entry)
        print ("Aggiunta!")

    if int(txtIn) == 2:
        print("OK, quale parola devo Tradurre?")
        txtIn = input()
        print(t.handleTranslate(txtIn))
        print("Tradotta!")
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break