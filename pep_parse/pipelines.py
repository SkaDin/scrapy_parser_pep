import csv
import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    """
    Пайплайн для подсчёта количества элементов с
    определенным статусом.
    """
    def open_spider(self, spider):
        """
        Метод, вызываемый при открытии паука,
        создаёт словарь и переменную-счётчик.
        """
        self.data = {}

    def process_item(self, item, spider):
        """
        Метод,вызываемый при обработке элемента.
        Подсчитывает количество элементов с определенным статусом.
        """
        status = item.get('status')
        if status:
            self.data[status] = self.data.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        """
        Метод, вызываемый при закрытии паука.
        Записывает результаты подсчета в CSV-файл.
        Дополнительно выводит общее число элементов.
        """
        now = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open(f'{BASE_DIR}/results/status_summary_{now}.csv',
                  'w',
                  encoding='utf-8',
                  newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])
            data_status_count = list(self.data.items())
            writer.writerows(data_status_count)
            writer.writerow(['Total', sum(self.data.values())])
