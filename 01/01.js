function solveLock(initialNumber, movements) {
  // Convertir el número inicial a un array de dígitos
  const digits = String(initialNumber).split('').map(Number);
  let currentPosition = 0;
  
  // Procesar cada movimiento
  for (const move of movements) {
    switch(move) {
      case 'R':
        // Mover a la derecha, volver al inicio si llegamos al final
        currentPosition = (currentPosition + 1) % digits.length;
        break;
      case 'L':
        // Mover a la izquierda, ir al final si estamos al inicio
        currentPosition = (currentPosition - 1 + digits.length) % digits.length;
        break;
      case 'U':
        // Incrementar dígito, volver a 0 si es 9
        digits[currentPosition] = (digits[currentPosition] + 1) % 10;
        break;
      case 'D':
        // Decrementar dígito, ir a 9 si es 0
        digits[currentPosition] = (digits[currentPosition] - 1 + 10) % 10;
        break;
    }
  }
  
  // Unir los dígitos y retornar como string
  return digits.join('');
}

// Casos de prueba
const testCases = [
  { initial: '000', moves: 'URURD', expected: '119' },
  { initial: '1111', moves: 'UUURUUU', expected: '4411' },
  { initial: '9999', moves: 'LULULULD', expected: '8000' }
];

// Verificar casos de prueba
console.log('=== Verificando casos de prueba ===');
testCases.forEach(({ initial, moves, expected }) => {
  const result = solveLock(initial, moves);
  console.log(`Entrada: ${initial} ${moves}`);
  console.log(`Resultado: ${result}`);
  console.log(`Esperado: ${expected}`);
  console.log(`¿Correcto? ${result === expected ? '✓' : '✗'}\n`);
});

// Resolver el desafío principal
const initialNumber = '528934712834';
const movements = 'URDURUDRUDLLLLUUDDUDUDUDLLRRRR';
const solution = solveLock(initialNumber, movements);
console.log('=== Solución al desafío ===');
console.log(`La combinación final es: ${solution}`);
