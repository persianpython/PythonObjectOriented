class Contact:
    def __init__(self, name, last_name, phone=None, email=None, display_mode="masked"):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False

        if (self.email is not None and self.email == other.email) or \
                (self.phone is not None and self.phone == other.phone):
            return True

        return self.name == other.name and self.last_name == other.last_name

    def __hash__(self):
        return hash((self.name, self.last_name, self.phone, self.email))

    def __repr__(self):
        if self.display_mode == "masked":
            return f"{self:masked}"

        return f"{self:unmasked}"

    def __str__(self):
        return f"{self.last_name[0].upper()}{self.name[0].upper()}"

    def __format__(self, format_spec):
        if format_spec == "unmasked":
            return f"Contact(name='{self.name}', last_name='{self.last_name}', phone='{self.phone}', email='{self.email}')"

        return f"Contact(name='{self._obfuscate(self.name)}', last_name='{self._obfuscate(self.last_name)}')"

    @staticmethod
    def _obfuscate(text):
        return text[:2] + '*' * (len(text) - 2)


if __name__ == '__main__':
    c1 = Contact(name="mohammad", last_name="fadakar", display_mode="unmasked")
    c2 = Contact(name="mohammad", last_name="fadakar")
    print(c1==c2)
    print(repr(c1))
    print(repr(c2))
    print(c1)
    print(c2)
    print(f"{c1:masked}")
    print(f"{c2:unmasked}")
