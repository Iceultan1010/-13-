# Зертханалық жұмыс №13 — NoteSpace

**Веб-бағдарламалау | Азатбекұлы Нұртуған**

Django-ның кіріктірілген Auth жүйесін қолданып жасалған пайдаланушы аутентификациясы бар веб-қосымша.

---

## Іске қосу

### 1. Виртуалды орта жасау
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# немесе
source venv/bin/activate     # macOS / Linux
```

### 2. Тәуелділіктерді орнату
```bash
pip install -r requirements.txt
```

### 3. Дерекқорды инициализациялау
```bash
python manage.py migrate
```

### 4. (Қосымша) Администратор аккаунтын жасау
```bash
python manage.py createsuperuser
```

### 5. Серверді іске қосу
```bash
python manage.py runserver
```

Браузерде ашыңыз: **http://127.0.0.1:8000**

---

## Беттер

| URL | Сипаттама | Рұқсат |
|-----|-----------|--------|
| `/` | Басты бет | Барлығы |
| `/accounts/register/` | Тіркелу | Анонимді |
| `/accounts/login/` | Кіру | Анонимді |
| `/accounts/logout/` | Шығу (POST) | Авторизацияланған |
| `/dashboard/` | Менің жазбаларым | @login_required |
| `/notes/create/` | Жазба қосу | @login_required |
| `/notes/<id>/edit/` | Жазба өзгерту | @login_required |
| `/notes/<id>/delete/` | Жазба жою | @login_required |
| `/admin/` | Админ панелі | Superuser |

---

## Орындалған талаптар

- ✅ Функциялық view-лар арқылы тіркелу, кіру, шығу
- ✅ `authenticate()`, `login()`, `logout()` функциялары
- ✅ `UserCreationForm` арқылы тіркелу
- ✅ Тіркелгеннен кейін автоматты кіру
- ✅ `@login_required` декораторы
- ✅ Шаблондарда `{% if user.is_authenticated %}` арқылы UI өзгерту
- ✅ Авторизациясыз қолданушыларда «Қосу/Өзгерту/Жою» жасырулы
- ✅ Кірген қолданушыда «Шығу» батырмасы және аты көрсетіледі
- ✅ Class-based view (LoginView, LogoutView) қолданылмаған
