# 41-нұсқа — Build және Test кезеңдері бөлек CI/CD конвейерінде

Жоба Python тіліндегі шағын арифметикалық модульден және `pytest` арқылы тексерілетін unit-тесттерден тұрады. GitHub Actions-та `Build` пен `Test` жеке job ретінде анықталған. `Test` job-ы `needs: build` арқылы Build сәтті аяқталғаннан кейін ғана іске қосылады.

## Жоба құрылымы

```text
.
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
└── .github/workflows/main.yml
```

## Талаптар

- Python 3.12 немесе үйлесімді нұсқа
- Git
- Тесттерді орындау үшін `pytest` (`requirements.txt` ішінде бекітілген)

## Жергілікті орнату және іске қосу

```bash
python -m pip install -r requirements.txt
python app.py
```

## Build және Test кезеңдерін жергілікті тексеру

Build кезеңін модельдеу:

```bash
python -m compileall -q app.py
```

Test кезеңін орындау:

```bash
python -m pytest -v
```

## CI/CD

`.github/workflows/main.yml` workflow `main` немесе `master` тармақтарына push жасалғанда немесе pull request ашылғанда, сондай-ақ GitHub Actions интерфейсінен қолмен іске қосылады. `Build` job-ы қолданба кодын Python bytecode-ына компиляциялап, синтаксисті тексереді. Тек осы job сәтті болса, `Test` job-ы тәуелділікті орнатып, барлық unit-тестті орындайды. Қате шықса, workflow сәтсіз деп белгіленеді және тәуелді Test job-ы орындалмайды.

Репозиторийді GitHub-қа жібергеннен кейін `Actions` бетінен нақты workflow орындалуын және екі job нәтижесін тексеріңіз.

