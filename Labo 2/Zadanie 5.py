def generujWykonaj(template, **kwargs):
    code = template.format(**kwargs)
    exec(code)

# Przykładowe użycie:
template = """
def generated_function(x):
    return x + {increment}

print(generated_function({value}))
"""
generujWykonaj(template, increment=5, value=10)
