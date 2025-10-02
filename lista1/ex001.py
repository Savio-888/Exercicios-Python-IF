temp = int(input("Digite o tempo gasto em horas na viagem: "))
vm = float(input("Digite a velocidade media do carro durante a viagem [Km/h]: "))
distancia = temp * vm
gas = distancia/12
print(f'A quantidade de litros em gasolina gasta é de {gas}L.\nVM: {vm}\nTEMPO: {temp}\nDISTANCIA {distancia}')
