class Contact:
    def __init__(self, nama, nomor) -> None:
        self.nama = nama
        self.nomor = nomor


class ContactManager:
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self, nama, nomor):
        contact = Contact(nama, nomor)
        self.contacts.append(contact)
        print(f"Kontak {nama} berhasil ditambahkan.")

    def list_contacts(self):
        if not self.contacts:
            print("Tidak ada kontak.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Nama: {contact.nama}, Nomor: {contact.nomor}")

    def edit_contact(self):
        self.list_contacts()
        if not self.contacts:
            return

        try:
            index = int(input("Masukkan nomor kontak yang ingin diedit: ")) - 1
            if 0 <= index < len(self.contacts):
                kontak = self.contacts[index]

                nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
                nomor_baru = input("Masukkan nomor baru (kosongkan jika tidak ingin mengubah): ")

                
                kontak.nama = nama_baru if nama_baru else kontak.nama
                kontak.nomor = nomor_baru if nomor_baru else kontak.nomor

                print("Kontak berhasil diedit.")
            else:
                print("Nomor kontak tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    def delete_contact(self):
        self.list_contacts()
        if not self.contacts:
            return

        try:
            index = int(input("Masukkan nomor kontak yang ingin dihapus: ")) - 1
            if 0 <= index < len(self.contacts):
                deleted_contact = self.contacts.pop(index)
                print(f"Kontak {deleted_contact.nama} berhasil dihapus.")
            else:
                print("Nomor kontak tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")


class Main:
    def run(self):
        manager = ContactManager()
        while True:
            print("\nMenu:")
            print("1. Tambah Kontak")
            print("2. Lihat Kontak")
            print("3. Edit Kontak")
            print("4. Hapus Kontak")
            print("5. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                nama = input("Masukkan nama: ")
                nomor = input("Masukkan nomor: ")
                manager.add_contact(nama, nomor)
            elif pilihan == "2":
                manager.list_contacts()
            elif pilihan == "3":
                manager.edit_contact()
            elif pilihan == "4":
                manager.delete_contact()
            elif pilihan == "5":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid.")


if __name__ == "__main__":
    Main().run()