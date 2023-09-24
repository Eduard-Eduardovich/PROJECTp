def validate_data(name, email, age):
    if not (name and email and age):
        raise IndexError("НЕ присутствуют все три поля")
    if not name.isalpha():
        raise NameError("Поле имени содержит НЕ только буквы")
    if '@' not in email or '.' not in email:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
    if not (10 <= int(age) <= 99):
        raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")

def process_registration_file(input_file, good_file, bad_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                name, email, age = line.strip().split()
                validate_data(name, email, age)
                with open(good_file, 'a', encoding='utf-8') as good:
                    good.write(f"{name} {email} {age}\n")
            except (ValueError, SyntaxError, NameError, IndexError) as e:
                with open(bad_file, 'a', encoding='utf-8') as bad:
                    bad.write(f"{line.strip()} {str(e)}\n")

input_file = 'registrations.txt'
good_file = 'registrations_good.log.txt'
bad_file = 'registrations_bad.log.txt'

process_registration_file(input_file, good_file, bad_file)


        
        
        



