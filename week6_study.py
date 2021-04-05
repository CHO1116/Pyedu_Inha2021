class Cookie:
    sugar_gram = 0

    def sugar(self, value):
        self.sugar_gram += value
        Cookie.count += 1

class Macaron(Cookie):
    def sugar(self, value):
        self.sugar_gram = value
        if self.sugar_gram < 50:
            self.sugar_gram = 50

macaron1, macaron2, macaron3 = None, None, None

macaron1 = Macaron()
macaron1.sugar(35)
print(macaron1.sugar_gram)