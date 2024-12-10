def inverter_fila(fila_de_pacientes):
    fila_invertida = []
    while fila_de_pacientes:
        fila_invertida.append(fila_de_pacientes.pop(0))
    fila_invertida.reverse()
    return fila_invertida


if __name__ == "__main__":
    fila_de_pacientes = ["Paciente 1", "Paciente 2", "Paciente 3", "Paciente 4"]
    print("Fila original:", fila_de_pacientes)
    fila_invertida = inverter_fila(fila_de_pacientes)
    print("Fila invertida:", fila_invertida)
