import camelot
import pandas as pd

def extract_transactions_from_pdf(pdf_path):
    """
    Extrai transações bancárias do extrato do Itaú em PDF usando Camelot.

    :param pdf_path: Caminho do arquivo PDF
    :return: DataFrame com colunas [Data, Lançamento, Valor, Saldo]
    """
    # Extrai as tabelas do PDF (presumindo que os dados estejam estruturados em formato tabular)
    tables = camelot.read_pdf(pdf_path, pages="all")  # Extraindo de todas as páginas

    if tables.n == 0:
        print("Nenhuma tabela detectada no PDF. Verifique se o formato é adequado para o Camelot.")
        return None

    # Combina todas as tabelas extraídas em um único DataFrame
    df_list = [table.df for table in tables]
    df = pd.concat(df_list, ignore_index=True)

    # Limpeza e renomeação das colunas (ajuste conforme a estrutura do PDF)
    df.columns = ["Data", "Lançamento", "Valor", "Saldo"]

    # Convertendo valores numéricos
    df["Valor"] = df["Valor"].str.replace(".", "").str.replace(",", ".").astype(float)
    df["Saldo"] = df["Saldo"].str.replace(".", "").str.replace(",", ".").astype(float)

    return df

def extract_transactions_from_csv(csv_path):
    """
    Extrai transações bancárias de um arquivo CSV.

    :param csv_path: Caminho do arquivo CSV
    :return: DataFrame com colunas [Data, Lançamento, Valor, Saldo]
    """
    df = pd.read_csv(csv_path, delimiter=";")  # Ajuste o delimitador se necessário
    return df
