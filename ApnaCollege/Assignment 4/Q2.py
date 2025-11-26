class Book:

    def __init__(self, title, author, reviews_list=None):
        self.title = title
        self.author = author
        if reviews_list is not None:
            self.reviews_list = reviews_list
        else:
            self.reviews_list = []
        # self.reviews_list = reviews_list if reviews_list is not None else []

    def add_review(self):
        review = input("Enter your review: ").strip()
        if review:  # only add if not empty
            self.reviews_list.append(review)
            print(f"{review}, Your review added.")
        else:
            print("Empty review not added.")

    def count_reviews(self):
        count = len(self.reviews_list)
        print(f"{count} is the reviews count.")

    def display_reviews(self):
        if not self.reviews_list:
            print("No reviews yet.")
        else:
            print("Reviews:")
            for i, review in enumerate(self.reviews_list, start=1):
                print(f"{i}. {review}")


b1 = Book("Witcher", "Ansh")

b1.add_review()
b1.count_reviews()
b1.display_reviews()
