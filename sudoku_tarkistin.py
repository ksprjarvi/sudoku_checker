# Tarkastaa onko parametrina saatu sudokun rivi oikein. 
def rivi_oikein(sudoku: list, rivi_nro: int):
    for sarake in sudoku[rivi_nro]:
        if sarake > 0:  # Ei huomioi täyttämättömiä sarakkeita. 
            if sudoku[rivi_nro].count(sarake) > 1:  # Jos sama numero esiintyy rivillä yli kerran, palautetaan False.
                return False
    return True  # Muutoin True

# Tarkastaa onko parametrina saatu pystysarake oikein. 
def sarake_oikein(sudoku: list, sarake_nro: int):
    lista = []  # Luodaan lista alkioita varten. 
    for rivi in sudoku:
        if rivi[sarake_nro] > 0 and rivi[sarake_nro] in lista:  # Jos pystysarakkeen alkio on yli 0 ja sarake löytyy listalta: 
            return False  # Palautetaan False
        lista.append(rivi[sarake_nro])  # Muutoin lisätään alkio listalle. 
    return True  # Jos saavutaan tähän, pystysarake on oikein, palautetaan True.

# Tarkastaa onko parametreina saaduista arvoista lähtevä 3x3 neliö täytetty oikein. 
def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    lista = []  # Luodaan lista alkioita varten. 
    for rivi in range(rivi_nro, rivi_nro + 3):  # Käydään haluttu rivi - haluttu rivi + 3 väli läpi. 
        for sarake in range(sarake_nro, sarake_nro + 3):  # Käydään rivin haluttu sarake - haluttu sarake + 3 läpi. 
            if sudoku[rivi][sarake] > 0 and sudoku[rivi][sarake] in lista:  # Jos alkio yli 0 ja löytyy listasta:
                return False  # Neliö on väärin täytetty ja palautetaan False. 
            lista.append(sudoku[rivi][sarake])  # Muutoin lisätään alkio listalle. 
    return True  # Palautetaan True jos neliö oikein. 

# Tarkastaa onko koko sudoku oikein TOISTAISEKSI, käyttämällä ylläolevia funktioita. 
def sudoku_oikein(sudoku: list):
    for i in range(9):
        if not rivi_oikein(sudoku, i):
            return False
    
    for i in range(9):
        if not sarake_oikein(sudoku, i):
            return False
    
    for i in range(0, 9, 3):
         if not nelio_oikein(sudoku, i, i):
             return False
    return True


if __name__ == '__main__':

    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(rivi_oikein(sudoku, 0))
    print(sudoku_oikein(sudoku))




