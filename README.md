# File Analyzer

🧰 Утилита для анализа логов.

Позволяет запускать разные виды отчётов через командную строку.

---

## 📦 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/VladimirUstinov5690/file_analyzer.git
cd file_analyzer

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Установите зависимости:
pip install -r requirements.txt

# Запуск
python main.py --file путь_к_файлу --report тип_отчета

# Примеры
python main.py --file logs.json --report average
python main.py --file logs.log --report good_worker


