import pdfplumber
import pandas as pd
import re

def extract_transactions_from_pdf(pdf_path):
    """
    Extrai transações bancárias do extrato do Itaú em PDF.

    :param pdf_path: Caminho do arquivo PDF
    :return: DataFrame com colunas [Data, Lançamento, Valor, Saldo]
    """
    transactions = []

    # Abre o PDF
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()  # Extrai o texto do PDF
            if text:
                lines = text.split("\n")  # Divide o texto em linhas

                for line in lines:
                    # Usamos Regex para capturar Data, Lançamento, Valor e Saldo
                    match = re.search(r'(\d{2}/\d{2}/\d{4})\s+(.+?)\s+(-?\d+,\d{2})\s+(-?\d+,\d{2})', line)
                    if match:
                        date, description, amount, balance = match.groups()
                        amount = float(amount.replace(".", "").replace(",", "."))  # Converter para float
                        balance = float(balance.replace(".", "").replace(",", "."))  # Converter para float
                        transactions.append([date, description.strip(), amount, balance])

    # Criar DataFrame
    df = pd.DataFrame(transactions, columns=["Data", "Lançamento", "Valor", "Saldo"])
    return df




























