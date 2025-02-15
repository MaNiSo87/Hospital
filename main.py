from PIL import Image, ImageDraw, ImageFont
import os
import random

class solution():
    def __init__(self, width, height, houses):
        self.height = height
        self.width = width
        self.houses = houses
        self.hospitals = []
        self.sep_width = 0
        self.sep_height = 0

    def calcost(self, index):
        x = 0
        for house in self.houses:
            x += abs(house[0] - index[0]) + abs(house[1] - index[1])
        return x

    def solve(self):
        h = []
        w = []
        for i in range(self.height):
            x  = 0
            for j in self.houses:
                j = j[0]
                if i > j:
                    x -= 1
                elif i < j:
                    x += 1
            h.append(abs(x))
        for i in range(self.width):
            x  = 0
            for j in self.houses:
                j = j[1]
                if i > j:
                    x -= 1
                elif i < j:
                    x += 1
            w.append(abs(x))

        hi = []
        wi = []
        for i in range(len(h)):
            if h[i] == min(h) or h[i] == min(h) + 1:
                hi.append(i)   
        for i in range(len(w)):
            if w[i] == min(w) or w[i] == min(w) + 1:
                wi.append(i)

        print(hi, wi)

        locs = []
        costs = []

        for i in hi:
            for j in wi:
                a = (i, j)
                if a not in self.houses:
                    locs.append(a)
                    costs.append(s.calcost(a))

        for i in range(len(costs)):
            if costs[i] == min(costs):
                self.hospitals = [locs[i]]
                break

    def output_image(self, filename):
        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10
        img = Image.new(
            "RGBA",
            (self.width * cell_size,
            self.height * cell_size + cost_size + padding * 2),
            "white"
        )
        house = Image.open("assets/images/House.png").resize((cell_size, cell_size))
        hospital = Image.open("assets/images/Hospital.png").resize((cell_size, cell_size))
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):
                rect = [
                    (j * cell_size + cell_border,
                    i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                    (i + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="black")

                if (i, j) in self.houses:
                    img.paste(house, rect[0], house)
                if (i, j) in self.hospitals:
                    img.paste(hospital, rect[0], hospital)

        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size,
            self.height * cell_size + cost_size + padding * 2),
            "black"
        )
        draw.text(
            (padding, self.height * cell_size + padding),
            f"Cost: Note calculated yet...",
            fill="white",
            font=font
        )

        img.save(filename)

#os.remove(r'C:\Users\manis\OneDrive\Desktop\src4\M\Main.png')
houses = []
width = int(input('Width: '))
height = int(input('Height: '))

for _ in range(int(input('How many houses? '))):
    x = input().split()
    houses.append((int(x[0]), int(x[1])))

s = solution(width, height, houses)
s.solve()
s.output_image(f'Main.png')