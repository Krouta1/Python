#zip(*iterables) - make an iterator that aggregates elements from each of the iterables.

user_names = ['user1', 'user2', 'user3']
passwords = ['password1', 'password2', 'password3']
login_date = ['1/1/2017', '1/2/2017', '1/3/2017']

user_pass = list(zip(user_names, passwords,login_date))

for i in user_pass:
    print(i)