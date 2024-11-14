def is_valid_password (word):
  if not all(c.islower() or c.isdigit() for c in word):
    return False

  last_digit = -1  
  last_letter = '`'
  seen_letter = False
  
  for char in word:
    if char.isdigit():
      if seen_letter:
        return False
      current_digit = int(char)
      if current_digit <= last_digit:
        return False
      last_digit = current_digit
    else:
      seen_letter = True
      if char <= last_letter:
        return False
      last_letter = char  
  return True

valids = 0
invalids = 0
with open('log.txt', 'r') as file:
  for line in file:
      valid = is_valid_password(line.strip())
      if valid:
        valids += 1
      else:
        # print(f"Bad: '{line.strip()}'")
        invalids += 1

print(f'Valid words: {valids}')
print(f'Invalid words: {invalids}')
print(f'submit {valids}true{invalids}false')
