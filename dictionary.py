class Dictionary:
    def __init__(self):
        diz = {}
        self.dizionario = diz

    def addWord(self, entry):
        chiave =entry[0].lower()
        valori=list(v.lower() for v in entry[1:])
        self.dizionario[chiave]= valori

    def translate(self, chiave):
        for k in self.dizionario:
            if chiave== k.lower():
                return self.dizionario [chiave]

    def translateWordWildCard(self, pattern:str):
        for k in self.dizionario:
            if len(pattern)!=len(k):
                return False
            else:
                for c1, c2 in zip(k,pattern):
                    if c1!='?' and c1!=c2:
                        return False
                    else: self.translate(k)
