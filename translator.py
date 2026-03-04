import dictionary as d
class Translator:

    def __init__(self):
        self.dizionario = d.Dictionary()



    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print ("1. Aggiungi nuova parola\n"
               "2. Cerca una traduzione\n"
               "3. Cerca con wildcard\n"
               "4. Exit")




    def loadDictionary(self, dict:str):
        # dict is a string with the filename of the dictionary

        with open (dict, "r", encoding= "utf-8") as fileInput:
            for riga in fileInput:
                parole =riga.split()
                entry= tuple(parole)
                self.dizionario.addWord(entry)
        return self.dizionario




    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        for elemento in entry:
            if elemento.isalpha():
                self.dizionario.addWord(entry)
                return entry
            else: return False




    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        da_verificare=query.lower()
        traduzione = self.dizionario.translate(da_verificare)
        return traduzione

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        n= query.count('?')
        if n==0:
            return self.handleTranslate(query)
        elif n==1:
            return self.dizionario.translateWordWildCard(query)
        else: return False

    def _test_modulo(self):
        self.printMenu()
        self.loadDictionary("dictionary.txt")
        daAggiungere= ("scricgnac", "cane", "oca", "gatto")
        print(self.handleAdd(daAggiungere))
        print(self.handleTranslate("kissa"))

if __name__ == "__main__":
    t=Translator()
    t._test_modulo()



