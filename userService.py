class userService(object):
	"""docstring for userService"""
	
	def __init__ (self, email, password) :
		self.email = email;
		self.password = password;
		self.data = {
			"gatrakelompok16@gmail.com" : {
				"email" 	: "gatrakelompok16@gmail.com",
				"password"	: "12345",
				"role"		: "superadmin"
			},
			"gagahkelompok16@gmail.com" : {
				"email"		: "gagahkelompok16@gmail.com",
				"password"	: "12345",
				"role"		: "user"
			}
		}
		self.history = {
			"gatrakelompok16@gmail.com" : {
				"peminjaman_buku"	: {"Fisika Dasar", "Dasar Komputer dan Pemrograman"},
				"tanggal_pinjam"	: "25-04-2020"
			},
			"gagahkelompok16@gmail.com" : {
				"peminjaman_buku"	: {"Kalkulus", "Dasar Komputer dan Pemrograman", "Konsep Jaringan Komputer"},
				"tanggal_pinjam"	: "25-04-2020"
			}
		} 	

	def login(self):
		ambil_data, ambil_history = self.cekCredential()
		if ambil_data :
			print("\nWelcome",ambil_data['role'])
			print("Logged it as user email : ",ambil_data['email'],"\n")
			print(ambil_data['email'], " Telah meminjam buku, yaitu : \n")
			for buku in ambil_history['peminjaman_buku'] :
			 print(buku, "\n")
			print("pada tanggal : ",ambil_history['tanggal_pinjam'])
		else :
			print("\nInvalid Input!\n")

	def cekCredential(self) :
		for nilai in self.data :
			if nilai == self.email :
				ambil_data_user = self.data[nilai]
				ambil_history = self.history[nilai]
				if self.password == ambil_data_user['password'] :
					return ambil_data_user, ambil_history
				else :
					return False