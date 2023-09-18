# InsightInk

InsightInk is a robust and user-friendly blogging platform, meticulously crafted on the foundation of Django. It empowers users to effortlessly share their thoughts, ideas, and experiences, offering a seamless and enriching content creation experience.


## Key Features

- **Multiple User Support**: InsightInk supports multiple user registrations and logins, ensuring a personalized experience for every user.

- **Intuitive WYSIWYG HTML Editor with Django-Froala**: InsightInk leverages the power of **[Django-Froala](https://github.com/froala/django-froala-editor)**, a seamless integration package for the Froala WYSIWYG HTML rich text editor. This modern editor brings a new level of sophistication to blog creation. With its clean design, users can easily navigate through a multitude of features, including text styling, image embedding, and much more.


- **Automated Testing and Containerization with GitHub Actions**: Every push to the main branch automatically triggers a GitHub Actions workflow to automatically validate code changes upon every push to the main branch. This ensures that the code is thoroughly tested, providing a robust and stable foundation for your blogging platform. Additionally, it utilizes Docker for containerization, enabling consistent deployment across diverse environments.



- **Containerized with Docker**: InsightInk is containerized using Docker, offering portability and consistent deployment across various environments.

## Tech Stack

- **Backend**: Django
- **Frontend**: Bootstrap
- **Database**: SQLite
- **Text Editor**: Django-Froala
- **Containerization**: Docker
- **Continuous Integration**: GitHub Actions

## Getting Started

1. Clone the repository: `git clone https://github.com/sachin-404/InsightInk.git`
2. Set up your virtual environment: `python -m venv venv ` and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Contributing

Contributions are whole heartedly welcomed! Feel free to open issues, submit pull requests, or suggest new features.

