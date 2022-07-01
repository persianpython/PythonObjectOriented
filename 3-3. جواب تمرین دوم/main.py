from string import ascii_letters, punctuation
from random import choices


class Password:
    """Password Sefareshi nesbat be tool va ghodrat.

    baste be ghodrat va tool moshakhas shode tavasote karbar ye password be sorate random sakhte mishavad.
    nesbat be ghodrat ( strength ) ( low -> 8 , mid -> 12, high -> 16 ) tool password be sorate default
    moshakhas mishavad magar inke karbar khodesh hengame sakhte object moshakhas konad.

    :param strength: ghavi bodane password nesbat be hamalat
    :type strength: str, optional

    :param length: toole password
    :type length: int, optional
    """

    INPUT_CHARACTERS = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }

    DEFAULT_LENGTHS = {
        "low": 8,
        "mid": 12,
        "high": 16
    }

    @classmethod
    def show_input(cls):
        """horof va adad va ashkali ke dar password estefade mishavad ra return mikone

        :rtype: dict (of list-s)
        """
        return cls.INPUT_CHARACTERS

    def __init__(self, strength="mid", length=None):
        """Constructor method"""
        self.strength = strength
        self.length = length

        self._generate()

    def _generate(self):
        """password ra ba tavajoh be tool va ghodrat moshakhas shode dar zaman sakht object misazad
        """

        population = self.INPUT_CHARACTERS["letters"].copy()
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

        if self.strength == "high":
            population += self.INPUT_CHARACTERS["numbers"] + self.INPUT_CHARACTERS["punctuation"]
        else:
            population += self.INPUT_CHARACTERS["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))


if __name__ == "__main__":
    p_low = Password(strength="low")
    print("low password: " + p_low.password)

    p_mid = Password(strength="mid", length=20)
    print("Mid password: " + p_mid.password)

    p_high = Password(strength="high", length=40)
    print("High password: " + p_high.password)

    p_default = Password()
    print("Default password: " + p_default.password)
