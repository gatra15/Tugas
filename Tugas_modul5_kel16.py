from userService import userService

print('System Login Kelompok16!\n')
email = input('Email : ')
password = input('Password : ')
ambil_class = userService(email, password)
ambil_class.login()