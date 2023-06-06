# Проект парсинг
## Описание проекта:
### Проект парсинга страниц документации PEP собирающий информацию о:
#### - Версиях документа;
#### - Названих;
#### - Статусах.

### Так же включена возможность отображения:
#### * Количества документов PEP в определенном статусе.
#### * Общего количества документов;

## Используемые технологии:
### - Python v3.7
### - Scrapy(_Асинхронный фреймворк_)

## Инструкция по развёртыванию проекта:

### 1. Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:SkaDin/scrapy_parser_pep.git

cd scrapy_parser_pep
```
### 2. Создать и активировать виртуальное окружение:
```commandline
pytnon -m venv venv
source venv/Scripts/activate
```
### 3. Установить зависимости из файла requirements.txt:
```commandline
pip install -r requirements.txt
```
#### - При необходимости обновить pip:
```commandline
python3 -m pip install --upgrade pip
```

### По команде:
```commandline
scrapy crawl pep
```
### Парсер начнёт работу и соберёт актуальную информацию в 2 файла с расширенимем .csv, которые будут находится в папке _results_.

# Автор проекта: SkaDin(Сушков Денис)