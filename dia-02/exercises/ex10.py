# Faça um programa que receba um número em segundos, converta esse número para horas, minuto e segundos. 
# Exemplos:

# Entrada: 556
# Saída: 0:9:16

# Entrada: 140153
# Saída: 38:55:53

segundos = int(input("Entre com um número em segundos: "))

horas = segundos // (60*60) #horas inteiras

segundos = segundos % (60*60) #resto da divisão por hora

minutos = segundos // 60 #minutos inteiros

segungos = segundos % 60 #resto de segundos da divisão por segundos

print(horas, minutos, segundos, sep=":")