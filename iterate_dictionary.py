
gene_expression = {
    "BRCA1": 12.5,
    "TP53": 7.8,
    "MCY": 19.2
}

for gene, expression in gene_expression.items():
    print(f'Gene: {gene}, Expression Level: {expression}')

gene_expression_2 = {"DKK1": 15.5, "SHH": 25.1, "FGF5": 4.2}

for gen, expression in gene_expression_2.items():
    print("Gene: {}, Expression level: {}".format(gen, expression))