data = {'user': 1, 'name': 'ee', 'thre': 5}
is_admin = data.get('name', False)
#print(is_admin)
teams = ["fghgf", "fjhj", "fdfgu", "dfgshd", "gkjhdgkd", "gjdhgj", "vbjnkn"]
#print(",".join(teams))
print(teams[1:5])
#奇数项
print(teams[::2])
#偶数项
print(teams[1::2])
