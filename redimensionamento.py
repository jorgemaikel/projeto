imagem_colorida = [
  [[255, 0, 0],   [0, 255, 0]],    # Linha 1: Vermelho, Verde
  [[0, 0, 255],   [80, 80, 80]],   # Linha 2: Azul, Cinza Escuro
  [[200, 200, 200], [255, 255, 0]] # Linha 3: Cinza Claro, Amarelo
]

# Convertendo para tons de cinza
altura = len(imagem_colorida)
largura = len(imagem_colorida[0])
imagem_cinza = []

for i in range(altura):
  linha_cinza = []
  for j in range(largura):
    pixel_colorido = imagem_colorida[i][j]
    R = pixel_colorido[0]
    G = pixel_colorido[1]
    B = pixel_colorido[2]


valor_pixel_cinza = (0.299 * R) + (0.587 * G) + (0.114 * B)
    linha_cinza.append(int(valor_pixel_cinza))
  imagem_cinza.append(linha_cinza)


print("Resultado da Imagem em Tons de Cinza:")
for linha in imagem_cinza:
    print(linha)


# Binarizar para Preto e Branco
print("\nIniciando a Etapa 2: Conversão para Preto e Branco...")

imagem_preto_e_branco = []
limiar = 128

for i in range(altura):
  linha_pb = []
  for j in range(largura):
    # Acessando o valor do pixel calculado
    pixel_cinza = imagem_cinza[i][j]

    # Aplicando a lógica do limiar (threshold)
    if pixel_cinza < limiar:
      novo_pixel_pb = 0  # Preto
    else:
      novo_pixel_pb = 255 # Branco

    linha_pb.append(novo_pixel_pb)
  imagem_preto_e_branco.append(linha_pb)

print("Resultado da Imagem em Preto e Branco:")
for linha in imagem_preto_e_branco:
    print(linha)
