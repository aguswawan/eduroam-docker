import pandas as pd

def csv_to_ldif(input_csv, output_ldif):
    # Baca data dari file CSV menggunakan pandas
    data = pd.read_csv(input_csv, delimiter=';')
    
    # Buat file LDIF untuk menulis data
    with open(output_ldif, 'w') as ldif_file:
        uidnumber = 1100
        # Iterasi melalui baris-baris dalam data CSV
        for index, row in data.iterrows():
            # Mendapatkan kolom-kolom dari CSV
            username = row['username']
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            password = row['password']

            
            # Tulis data ke file LDIF
            ldif_file.write(f"dn: uid={username},ou=pegawai,dc=example,dc=org\n")
            ldif_file.write(f"cn: {first_name} {last_name}\n")
            ldif_file.write(f"gidnumber: 500\n")
            ldif_file.write(f"givenname: {first_name}\n")
            ldif_file.write(f"homedirectory: /home/users/{username}\n")
            ldif_file.write(f"mail: {email}\n")
            ldif_file.write(f"objectclass: inetOrgPerson\n")
            ldif_file.write(f"objectclass: posixAccount\n")
            ldif_file.write(f"objectclass: top\n")
            ldif_file.write(f"sn: {last_name}\n")
            ldif_file.write(f"uid: {username}\n")
            ldif_file.write(f"uidnumber: {uidnumber + 1}\n")
            ldif_file.write(f"userpassword: {password}\n")
            ldif_file.write("\n")
            uidnumber += 1

    print(f"Konversi dari {input_csv} ke {output_ldif} selesai.")

# Gunakan fungsi dengan menyediakan nama file input CSV dan output LDIF
csv_to_ldif('input.csv', 'output.ldif')
