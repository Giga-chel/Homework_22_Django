from django.shortcuts import render


# Контроллер для домашней страницы
def home(request):
    return render(request, 'catalog/home.html')


# Контроллер для страницы контактов (с логикой доп. задания)
def contacts(request):
    # Переменная для хранения сообщения
    message = None

    # Проверка метода запроса (POST - отправка формы)
    if request.method == 'POST':
        # Получение данных из формы (в реальном проекте здесь была бы валидация)
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        # Имитация успешной обработки
        print(f"Получено сообщение от {name} ({email}): {text}")

        message = "Ваше сообщение успешно отправлено!"

    context = {
        'message': message
    }

    return render(request, 'catalog/contacts.html', context)
