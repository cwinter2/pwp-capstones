
############# USER CLASS ########################

class User :

	def __init__(self, name, email) :
		self.name = name
		self.email = email
		self.books = {}

	def get_email(self) :
		return self.email

	def change_email(self, address) :
		self.email = address
		return 'User email updated to {}'.format(address)

	def __repr__(self) :
		return 'User {}, email: {}, books read : {}'.format(self.name, 
			self.email, len(self.books))

	def __eq__(self, other_user) :
		if self.name == other_user.name and self.email == other_user.email :
			return True
		else :
			return False

	def read_book(self, book, rating = None) :
		self.books[book] = rating

	def get_average_rating(self) :
		total = 0
		count = 0
		for book in self.books :
			if self.books[book] is not None :
				total += self.books[book]
				count += 1
			else :
				continue
		return total / count


############# BOOK CLASS ########################

class Book :

	def __init__(self, title, isbn) :
		self.title = title
		self.isbn = isbn
		self.ratings = []

	def get_title(self) :
		return self.title

	def get_isbn(self) :
		return self.isbn

	def set_isbn(self, new_isbn) :
		self.isbn = new_isbn

	def add_rating(self, rating) :
		try :
			if 0 <= rating <= 4 :
				self.ratings.append(rating)
		except :
			print('Invalid Rating')

	def get_average_rating(self) :
		return float(sum(self.ratings) / len(self.ratings))


	def __eq__(self, other_book) :
		if self.title == other_book.title and self.isbn == other_book.isbn :
			return True
		else :
			return False		

	def __repr__(self) :
		return 'Title : {}, ISBN : {}'.format(self.title, self.isbn)

	def __hash__(self) :
		return hash((self.title, self.isbn))

############# FICTION CLASS #####################

class Fiction(Book) :

	def __init__(self, title, author, isbn) :
		super().__init__(title, isbn)
		self.author = author

	def get_author(self) :
		return self.author

	def __repr__(self) :
		return '{} by {}'.format(self.title, self.author)

############# NONFICTION CLASS ##################

class Non_Fiction(Book) :

	def __init__(self, title, subject, level, isbn) :
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level

	def get_subject(self) :
		return self.subject

	def get_level(self) :
		return self.level

	def __repr__(self) :
		return '{}, a {} manual on {}'.format(self.title, self.level, self.subject)

############# TOME RATER ########################

class TomeRater :

	def __init__(self) :
		self.users = {}
		self.books = {}

	def create_book(self, title, isbn) :
		new_book = Book(title, isbn)
		return new_book

	def create_novel(self, title, author, isbn) :
		new_fiction = Fiction(title, author, isbn)
		return new_fiction

	def create_non_fiction(self, title, subject, level, isbn) :
		new_non_fiction = Non_Fiction(title, subject, level, isbn)
		return new_non_fiction

	def add_book_to_user(self, book, email, rating = None) :
		try :
			self.users[email].read_book(book, rating)
			book.add_rating(rating)

			if book in self.books :
				self.books[book] += 1
			else :
				self.books[book] = 1

		except :
			print('No user with email {}'.format(email))

	def add_user(self, name, email, user_books = None) :
		new_user = User(name, email)
		print(new_user)
		self.users[email] = new_user
		if user_books is not None :
			for book in user_books :
				self.add_book_to_user(book, email)

	def print_catalog(self) :
		for book in self.books :
			print(book)

	def print_users(self) :
		for user in self.users :
			print(user)

	def most_read_book(self) :
		return max(self.books, key = self.books.get)

	def highest_rated_book(self) :
		temp_dict = {}
		for book in self.books :
			temp_dict[book] = book.get_average_rating()
		return max(temp_dict, key = temp_dict.get)

	def most_positive_user(self) :
		temp_dict = {}
		for user in self.users :
			temp_dict[user] = self.users[user].get_average_rating()
		return max(temp_dict, key = temp_dict.get)

	def get_n_most_read_books(self, n) :
		temp_dict = self.books.copy()
		for i in range (0, n) :
			temp_book = max(temp_dict, key = temp_dict.get)
			print(temp_book, ': read {} time(s)'.format
					(str(temp_dict.pop(max(temp_dict, key = temp_dict.get)))))

	def get_n_most_prolific_readers(self, n) :
		temp_dict = {}
		for user in self.users :
			temp_dict[user] = len(self.users[user].books)
		for i in range (0, n) :
			temp_user = max(temp_dict, key = temp_dict.get)
			print(temp_user, ' has read {} book(s)'.format
					(str(temp_dict.pop(max(temp_dict, key = temp_dict.get)))))


 













