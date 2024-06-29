import spacy
import re

# Загрузка русскоязычной модели spaCy
nlp = spacy.load("ru_core_news_sm")

# Функция для извлечения информации из текста
def extract_info(text):
    doc = nlp(text)
    
    book_info = {
        "title": "",
        "author": "",
        "publisher": "",
        "year": "",
        "pages": "",
        "binding": "",
        "format": "",
        "seller": "",
        "location": "",
        "price": "",
        "condition": "",
        "note": ""
    }

    # Применение регулярных выражений для поиска информации
    title_author_match = re.search(r"^(.*?)(?:\.\s*|(?:\.|\s)([А-ЯЁ][а-яё\s]+))", text)
    if title_author_match:
        book_info["title"] = title_author_match.group(1).strip()
        if title_author_match.lastindex > 1:
            book_info["author"] = title_author_match.group(2).strip()

    publisher_year_match = re.search(r"М\.\s*(.*?)(\d{4}г)\.?", text)
    if publisher_year_match:
        book_info["publisher"] = publisher_year_match.group(1).strip()
        book_info["year"] = publisher_year_match.group(2).strip()

    pages_match = re.search(r"(\d+с\.?[\+\dс\.]*)", text)
    if pages_match:
        book_info["pages"] = pages_match.group(1).strip()

    binding_match = re.search(r"(картонный переплет|мягкий переплет|твердый, издательский коленкоровый переплет)", text)
    if binding_match:
        book_info["binding"] = binding_match.group(1).strip()

    format_match = re.search(r"(увеличенный формат|обычный формат|очень большой формат)", text)
    if format_match:
        book_info["format"] = format_match.group(1).strip()

    seller_match = re.search(r"BS\s*-\s*([\w-]+),\s*([\w\s\-]+)", text)
    if seller_match:
        book_info["seller"] = seller_match.group(1).strip()
        book_info["location"] = seller_match.group(2).strip()

    price_match = re.search(r"Цена:\s*(\d+\s*руб\.?)", text)
    if price_match:
        book_info["price"] = price_match.group(1).strip()

    condition_match = re.search(r"Состояние:\s*([\w\s]+)", text)
    if condition_match:
        book_info["condition"] = condition_match.group(1).strip()

    return book_info

# Чтение содержимого файла text.txt

# Разделение текста на отдельные записи (похоже на ваши примеры)


with open("text.txt","r", encoding='utf-8') as f:
    for text in f:
        # text = re.split(r"\n\s*\n", texts)
        book_data = extract_info(text)
        with open("test.txt",'a', encoding='utf-8') as tf:
            tf.write(str(book_data)+"\n")

