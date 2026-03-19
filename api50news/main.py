import pprint
from client.api_methods import get_everything

if __name__ == "__main__":
    result = get_everything(
        "425d709772f542dbb501fd8b65fcf5f2",
        q="Usa",
        page_size=100,
        page_number=3,
        language="en",
        sort_by="relevancy"
    )

    print(f"Всего найдено: {result.get('totalResults', 0)}")
    print(f"Получено статей: {len(result.get('articles', []))}")

    sm = 52
    sp = []

    if result.get('articles'):
        for i, article in enumerate(result['articles'][:sm], 1):
            title = article.get('title')
            if title and title.strip() != "" and len(article.get('description')) >= 50 and article.get('url'):

                """
                print(f"\n{i}. {article.get('title')}")
                print(f"   Источник: {article.get('source', {}).get('name')}")
                print(f"   Дата: {article.get('publishedAt')}")
                print(f"   Автор: {article.get('author')}")
                print(f"   URL: {article.get('url')}")
                """

                state = {
                    "title": article.get('title'),
                    "source": article.get('source', {}).get('name'),
                    "published": article.get('publishedAt'),
                    "author": article.get('author'),
                }
                sp.append(state)
            else:
                sm += 1
    else:
        print("Новости не найдены")
    pprint.pprint(sp)
    print(len(sp))
