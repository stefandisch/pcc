name = "ada Lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # Use f-string (format string, since 3.6)
print(f"Full name: {full_name.title()}")

print("\nStrip strings")
language=' python '
print(language)
print(language.rstrip())
print(language.lstrip())
print(language.strip)