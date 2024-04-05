def check_vowels():
    # Código a implementar utilizando input.
    nombre = input("escriba su nombre: ")
    vocal_a = "a"
    vocal_e = "e"
    vocal_i = "i"
    vocal_o = "o"
    vocal_u = "u"

    print("Contiene a: ",vocal_a in nombre)
    print("Contiene e: ",vocal_e in nombre)
    print("Contiene i: ",vocal_i in nombre)
    print("Contiene o: ",vocal_o in nombre)
    print("Contiene u: ",vocal_u in nombre)

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
