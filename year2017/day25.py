class TuringMachine:
    def __init__(self, state='A', pos=0):
        self.state = 'A'
        self.pos = 0
        self.tape = set()

    @property
    def value(self):
        if self.pos in self.tape:
            return 1
        else:
            return 0

    def step(self):
        if self.state == 'A':
            if self.value == 0:
                self.tape.add(self.pos)
                self.pos += 1
                self.state = 'B'
            else:
                self.tape.remove(self.pos)
                self.pos -= 1
                self.state = 'C'
        elif self.state == 'B':
            if self.value == 0:
                self.tape.add(self.pos)
                self.pos -= 1
                self.state = 'A'
            else:
                self.tape.add(self.pos)
                self.pos += 1
                self.state = 'D'
        elif self.state == 'C':
            if self.value == 0:
                self.tape.add(self.pos)
                self.pos += 1
                self.state = 'A'
            else:
                self.tape.remove(self.pos)
                self.pos -= 1
                self.state = 'E'
        elif self.state == 'D':
            if self.value == 0:
                self.tape.add(self.pos)
                self.pos += 1
                self.state = 'A'
            else:
                self.tape.remove(self.pos)
                self.pos += 1
                self.state = 'B'
        elif self.state == 'E':
            if self.value == 0:
                self.tape.add(self.pos)
                self.pos -= 1
                self.state = 'F'
            else:
                self.tape.add(self.pos)
                self.pos -= 1
                self.state = 'C'
        elif self.state == 'F':
            if self.value == 0:
                self.tape.add(self.pos)
                self.pos += 1
                self.state = 'D'
            else:
                self.tape.add(self.pos)
                self.pos += 1
                self.state = 'A'

    @property
    def checksum(self):
        return len(self.tape)


def fn_p1():
    machine = TuringMachine()
    for _ in range(12173597):
        machine.step()
    return machine.checksum


if __name__ == '__main__':
    print("Part 1:", fn_p1())  # 2870
