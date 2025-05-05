# hexadecode.py

# -------------------------------
# Este script tem como objetivo decodificar uma string hexadecimal para texto ASCII legível.
# Foi desenvolvido como parte de um desafio CTF do projeto Global Solutions da FIAP,
# no curso de Cibersegurança. Ideal para análise de dados codificados ou capturados
# em desafios de segurança (como CTFs).
# -------------------------------

# Sequência hexadecimal fornecida entre aspas triplas (formato exigido pelo desafio)
codigo_hex = """
4120666c616720706172612065737465206465736166696f20c3a920464941507b6865785f746f5f61736349497d0a
"""

# Remover espaços em branco e quebras de linha da string hexadecimal
# Isso garante que apenas os caracteres válidos de hexadecimal sejam processados
codigo_hex = codigo_hex.replace("\n", "")

# Converter a string hexadecimal para bytes:
# - bytes.fromhex() interpreta cada par de caracteres como um byte (ex: '41' = 0x41 = 'A')
# - decode('utf-8') transforma os bytes em uma string legível em formato UTF-8
codigo_decodificado = bytes.fromhex(codigo_hex).decode('utf-8')

# Exibir o resultado final da decodificação no console
print("Resultado da Decodificação:", codigo_decodificado)
