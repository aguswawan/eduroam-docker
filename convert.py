import csv

def csv_to_ldif(csv_file, ldif_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        with open(ldif_file, 'w') as ldif:
            for row in reader:
                ldif.write(f'dn: uid={row["username"]},ou=users,dc=example,dc=com\n')
                ldif.write(f'objectClass: inetOrgPerson\n')
                ldif.write(f'uid: {row["username"]}\n')
                ldif.write(f'givenName: {row["first_name"]}\n')
                ldif.write(f'sn: {row["last_name"]}\n')
                ldif.write(f'mail: {row["email"]}\n')
                ldif.write(f'userPassword: {row["password"]}\n\n')

# Usage example
csv_to_ldif('input.csv', 'output.ldif')
