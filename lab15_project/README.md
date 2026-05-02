# Зертханалық жұмыс №15
## Жобаны орналастыруға дайындау: Nginx/Gunicorn, .env файлдары және қауіпсіздік параметрлері

**Студент:** Азатбекұлы Нұртуған  
**Пән:** Веб-бағдарламалау | Компьютерлік инженерия

---

## Жоба құрылымы

```
lab15_project/
├── myproject/              # Django жобасы
│   ├── myproject/
│   │   ├── settings.py     # Өндірістік параметрлер (.env арқылы)
│   │   ├── urls.py
│   │   └── wsgi.py         # WSGI интерфейсі (Gunicorn үшін)
│   ├── static/             # Статикалық файлдар (CSS, JS, суреттер)
│   ├── staticfiles/        # collectstatic нәтижесі (gitignore-да)
│   ├── manage.py
│   └── requirements.txt    # Python тәуелділіктері
├── nginx/
│   └── myproject.conf      # Nginx конфигурациясы
├── gunicorn/
│   └── gunicorn.conf.py    # Gunicorn конфигурациясы
├── .env.example            # .env үлгісі (нақты мәндерсіз)
├── .gitignore              # Git-тен алынып тасталған файлдар
└── README.md
```

---

## Орнату нұсқауы

### 1. Репозиторийді клондау
```bash
git clone https://github.com/yourusername/lab15-project.git
cd lab15-project
```

### 2. Виртуалды орта жасау
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# немесе
venv\Scripts\activate           # Windows
```

### 3. Тәуелділіктерді орнату
```bash
pip install -r myproject/requirements.txt
```

### 4. .env файлын баптау
```bash
cp .env.example .env
# .env файлын өзіңіздің мәндеріңізбен толтырыңыз
nano .env
```

### 5. Миграцияларды іске қосу
```bash
cd myproject
python manage.py migrate
```

### 6. Статикалық файлдарды жинау
```bash
python manage.py collectstatic
```

### 7. Gunicorn арқылы іске қосу
```bash
gunicorn myproject.wsgi:application -c ../gunicorn/gunicorn.conf.py
```

---

## Теориялық бөлім

### Nginx және Gunicorn

**Gunicorn** (Green Unicorn) — Python WSGI HTTP сервері. Django қолданбасын іске қосады және HTTP сұраулары мен Django арасындағы байланысты қамтамасыз етеді.

**Nginx** — жоғары өнімді веб-сервер және кері прокси. Екі негізгі қызмет атқарады:
- Статикалық файлдарды (CSS, JS, суреттер) тікелей береді — Django-ға жібермейді
- Динамикалық сұраулар Gunicorn-ға (Django-ға) жіберіледі

**`runserver` командасынан айырмашылығы:**
| | `runserver` | Nginx + Gunicorn |
|---|---|---|
| Мақсаты | Тек әзірлеу | Өндіріс |
| Өнімділік | Төмен | Жоғары |
| Параллельділік | 1 сұрау | Бірнеше жұмысшы |
| Статика | Django береді | Nginx береді |
| Қауіпсіздік | Аз | Жоғары |

### WSGI / ASGI

**WSGI** (Web Server Gateway Interface) — веб-сервер мен Python қолданбасы арасындағы стандартты интерфейс (PEP 3333). Синхронды сұраулар үшін.

**ASGI** (Asynchronous Server Gateway Interface) — WSGI-дің асинхронды нұсқасы. WebSocket, HTTP/2 үшін қолданылады.

### .env файлдарының қауіпсіздігі

`.env` файлдарын `.gitignore`-ға қосу **міндетті**, себебі:

1. **SECRET_KEY** — Django шифрлауының негізі. Жарияланса, сеанстарды бұзуға болады
2. **Дерекқор паролі** — дерекқорға рұқсатсыз кіру мүмкіндігі пайда болады
3. **API кілттері** — үшінші тарап қызметтеріне рұқсатсыз қол жеткізу
4. **GitHub тарихы** — файлды жойсаңыз да, тарихта қалады

**Ең жақсы тәжірибе:** `.env.example` файлын жасаңыз (нақты мәндерсіз) және оны ғана GitHub-қа жүктеңіз.

---

## Пайдаланылған технологиялар

- Python 3.11+
- Django 4.2
- Gunicorn 21.2
- Nginx 1.24
- python-dotenv 1.0
- PostgreSQL
