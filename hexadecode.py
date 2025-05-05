# hexadecode.py

# -------------------------------
# Este script tem como objetivo decodificar uma string hexadecimal para texto ASCII legível
# Ideal para análise de dados codificados ou capturados em desafios de segurança (ex: CTFs)
# -------------------------------


# Sequência hexadecimal fornecida
codigo_hex = """

4120666c616720706172612065737465206465736166696f20c3a920464941507b6865785f746f5f61736349497d0a


"""


# Remover espaços e quebras de linha
codigo_hex = codigo_hex.replace("\n", "")

# Conversão do hexadecimal para bytes, e depois decodificação UTF-8 para obter o texto original

# bytes.fromhex() converte a string hexadecimal em uma sequência de bytes binários

# decode('utf-8') transforma essa sequência de bytes em uma string legível
codigo_decodificado = bytes.fromhex(codigo_hex).decode('utf-8')

# Exibição do resultado final no console
print("Resultado da Decodificação:", codigo_decodificado)