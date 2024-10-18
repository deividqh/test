personas = [{"Ana":{"edad":28,"ciudad":"Murcia"}},
             {"Luis":{"edad":38,"ciudad":"Madrid"}},
             {"Alberto":{"edad":23,"ciudad":"Murcia"}}]

personas1 = [{"nombre":"Ana","edad":28,"ciudad":"Murcia"},
             {"nombre":"Luis","edad":38,"ciudad":"Murcia"},
             {"nombre":"Angel","edad":37,"ciudad":"Molina"}]
print()
print(personas)
for persona in personas:
    for clave,valor in persona.items():
        if valor["ciudad"] == "Murcia":
            print(clave)
# ------------------------------------Cambia ana por alicia
result= [personas.pop(i) for i,persona in enumerate(personas)
                            for clave,valor in persona.items()
                                if clave == "Ana" ]

if result:
    # print(result)
    valorAna=result[0]["Ana"]
    # print(valorAna)
    personas.append({"Alicia":valorAna})
    print(personas)

# ---------------------------Cambia ana por alicia
for per in personas1:
    if per.get("nombre")=="Ana":
        per["nombre"]="Alicia"
        break
print(personas1)





