import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        
        if altura <= 0:
            raise ValueError("A altura deve ser maior que zero.")
        if peso <= 0:
            raise ValueError("O peso deve ser maior que zero.")

        imc = peso / (altura ** 2)
        imc_formatado = f"{imc:.2f}"
        
        # Determinando a situação do IMC
        if imc < 18.5:
            situacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            situacao = "Peso normal"
        elif 25 <= imc < 29.9:
            situacao = "Sobrepeso"
        else:
            situacao = "Obesidade"

        messagebox.showinfo("Resultado do IMC", f"Seu IMC é: {imc_formatado}\nSituação: {situacao}")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x300")
janela.configure(bg="#f0f8ff")

# Criando os componentes da interface com estilo aprimorado
label_titulo = tk.Label(janela, text="Calculadora de IMC", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4682b4")
label_titulo.pack(pady=10)

label_altura = tk.Label(janela, text="Altura (em metros):", bg="#f0f8ff", font=("Helvetica", 12))
label_altura.pack()

entry_altura = tk.Entry(janela, font=("Helvetica", 12), width=10, justify="center")
entry_altura.pack(pady=5)

label_peso = tk.Label(janela, text="Peso (em kg):", bg="#f0f8ff", font=("Helvetica", 12))
label_peso.pack()

entry_peso = tk.Entry(janela, font=("Helvetica", 12), width=10, justify="center")
entry_peso.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc, font=("Helvetica", 12, "bold"), bg="#4682b4", fg="white")
botao_calcular.pack(pady=15)

# Executando a aplicação
janela.mainloop()
