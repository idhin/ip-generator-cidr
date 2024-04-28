import ipaddress

def generate_ips_from_cidr(cidr_file, output_file):
    try:
        with open(cidr_file, 'r') as cidr_file:
            cidr_list = cidr_file.readlines()

            with open(output_file, 'w') as output:
                for cidr in cidr_list:
                    cidr = cidr.strip()  # Menghapus karakter baris baru
                    network = ipaddress.ip_network(cidr)
                    for ip in network:
                        output.write(str(ip) + '\n')
        print("IPs berhasil di-generate dan disimpan dalam", output_file)
    except FileNotFoundError:
        print("File CIDR tidak ditemukan.")

# Ganti cidr.txt dengan nama file CIDR yang Anda miliki
# Ganti ips.txt dengan nama file untuk menyimpan hasil IP
generate_ips_from_cidr("cidr.txt", "ips.txt")
