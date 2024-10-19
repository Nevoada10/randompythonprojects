# Definindo os valores conhecidos
distancia = float(input(" Distância em metros: "))  # metros
tempo = float(input(" Tempo em segundos: "))  # segundos

# Calculando a velocidade média em m/s
velocidade_media_m_s = distancia / tempo

# Convertendo para km/h (1 m/s = 3.6 km/h)
velocidade_media_km_h = velocidade_media_m_s * 3.6

# Arredondando para duas casas decimais
velocidade_media_m_s = round(velocidade_media_m_s, 2)
velocidade_media_km_h = round(velocidade_media_km_h, 2)

print(velocidade_media_m_s, velocidade_media_km_h)
