from typing import Any, Optional
import requests

base_url = 'https://newsapi.org/v2'


def _make_request(endpoint: str, api_key: str, params: dict = None) -> dict[str, Any]:
    url = f"{base_url}/{endpoint}"
    default_params = {"apiKey": api_key}

    if params:
        default_params.update(params)

    try:
        response = requests.get(url, params=default_params, timeout=10)

        if response.status_code == 401:
            raise Exception("Неверный API ключ")
        elif response.status_code == 429:
            raise Exception("Превышен лимит запросов")
        elif response.status_code != 200:
            raise Exception(f"Ошибка API: {response.status_code} - {response.text}")
        if not response.text.strip():
            raise Exception("Сервер вернул пустой ответ")

        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f'Ошибка при запросе к NewsApi {endpoint}: {e}')

    except ValueError as e:
        raise Exception(f"Ошибка парсинга Json ({endpoint}): {e}")


def get_top_headlines(api_key: str, q: str = None, country: str = None, category: str = None,
                      sources: str = None, page_size: int = None, page: int = None) -> dict[str, Any]:
    params = {
        'q': q,
        'country': country,
        'category': category,
        'sources': sources,
        'pageSize': page_size,
        'page': page
    }

    params_final = {key: value for key, value in params.items() if value is not None}
    return _make_request(endpoint='top-headlines', api_key=api_key, params=params_final)


def get_everything(api_key: str, q: str, language: str = "en",
                   page_size: int = None, page: int = None,
                   sort_by: str = "publishedAt", **kwargs) -> dict[str, Any]:
    params = {
        'q': q,
        'language': language,
        'pageSize': page_size,
        'page': page,
        'sortBy': sort_by,
        **kwargs
    }

    params_final = {key: value for key, value in params.items() if value is not None}
    return _make_request(endpoint='everything', api_key=api_key, params=params_final)


def sources(api_key: str = None, **kwargs) -> dict[str, Any]:
    return _make_request("sources", api_key, kwargs)