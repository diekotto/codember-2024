def solve_lock(initial_number: str, movements: str) -> str:
    # Convertimos el número inicial a una lista de dígitos
    digits = [int(d) for d in str(initial_number)]
    current_position = 0
    
    for move in movements:
        if move == 'R':
            # Mover a la derecha, volver al inicio si llegamos al final
            current_position = (current_position + 1) % len(digits)
        elif move == 'L':
            # Mover a la izquierda, ir al final si estamos al inicio
            current_position = (current_position - 1) % len(digits)
        elif move == 'U':
            # Incrementar dígito, volver a 0 si es 9
            digits[current_position] = (digits[current_position] + 1) % 10
        elif move == 'D':
            # Decrementar dígito, ir a 9 si es 0
            digits[current_position] = (digits[current_position] - 1) % 10
            
    # Convertir la lista de dígitos de vuelta a string
    return ''.join(map(str, digits))

# Casos de prueba
test_cases = [
    ("000", "URURD", "119"),
    ("1111", "UUURUUU", "4411"),
    ("9999", "LULULULD", "8000")
]

# Verificar casos de prueba
for initial, moves, expected in test_cases:
    result = solve_lock(initial, moves)
    print(f"Entrada: {initial} {moves}")
    print(f"Resultado: {result}")
    print(f"Esperado: {expected}")
    print(f"¿Correcto? {'✓' if result == expected else '✗'}\n")

# Resolver el desafío principal
initial_number = "528934712834"
movements = "URDURUDRUDLLLLUUDDUDUDUDLLRRRR"
solution = solve_lock(initial_number, movements)
print(f"Solución al desafío: {solution}")
