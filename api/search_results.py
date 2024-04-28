from dataclasses import dataclass

from pytube import Search


@dataclass
class SearchResult:
    author: str
    title: str
    video_id: str


def search_results(prompt: str) -> list[SearchResult]:
    """
    :param prompt:
    Строка поискового запроса
    :return:
    Массив из результатов поиска
    """
    s = Search(prompt)

    return [SearchResult(
        author=video.author,
        title=video.title,
        video_id=video.video_id,
    ) for video in s.results]
