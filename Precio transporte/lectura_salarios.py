import pandas as pd

df = pd.read_csv("https://infra.datos.gob.ar/catalog/sspm/dataset/158/distribution/158.1/download/remuneracion-imponible-promedio-trabajadores-estables-ripte-total-pais-pesos-serie-mensual.csv",
                 sep=",")

if __name__ == "__main__":
    df.to_excel("ripte.xlsx", index=False)
