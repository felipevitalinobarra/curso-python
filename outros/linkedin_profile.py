class UserProfile:
    def __init__(self, name, last_name, marital_status, age,
                  occupation, education, phone, email, github):
        self.name = name
        self.last_name = last_name
        self.marital_status = marital_status
        self.age = age
        self.occupation = occupation
        self.education = education
        self.phone = phone
        self.email = email
        self.github = github

    def display_profile(self):
        print(f"{'='*40}")
        print(f"Name: {self.name} {self.last_name}")
        print(f"Marital Status: {self.marital_status.capitalize()}")
        print(f"Age: {self.age} years old")
        print(f"Occupation: {self.occupation}")
        print(f"Education: {self.education}")
        print(f"Phone: {self.phone}")
        print(f"E-mail: {self.email}")
        print(f"GitHub: {self.github}")
        print(f"{'='*40}")


profile = UserProfile(
    name='Felipe',
    last_name='Barra',
    marital_status='married',
    age=28,
    occupation='QA Analyst',
    education='Systems Analysis and Development',
    phone='+55 (11) 95469-2789',
    email='felipevitalino96@gmail.com',
    github='github.com/felipevitalinobarra'
)

profile.display_profile()
