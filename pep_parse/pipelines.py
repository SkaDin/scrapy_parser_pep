import csv
import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    """
    Пайплайн для подсчёта количества элементов с
    определенным статусом.
    """

    def __init__(self):
        self.writer = None
        self.file = None
        self.now = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.total_count = 0
        self.status_count = {
            'Active': 0,
            'Accepted': 0,
            'Deferred': 0,
            'Final': 0,
            'Provisional': 0,
            'Rejected': 0,
            'Superseded': 0,
            'Withdrawn': 0,
            'Draft': 0
        }

    def open_spider(self, spider):
        """
        Метод, вызываемый при открытии паука,
        (создаёт директорию)открывает файл
        для записи результатов'.
        """
        create_dir = BASE_DIR / 'results'
        create_dir.mkdir(exist_ok=True)
        self.file = open(f'{BASE_DIR}/results/status_summary_{self.now}.csv',
                         'w',
                         encoding='utf-8',
                         newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['Статус', 'Количество'])

    def process_item(self, item, spider):
        """
        Метод,вызываемый при обработке элемента.
        Подсчитывает количество элементов с определенным статусом.
        """
        if 'status' in item:
            status = item['status']
            if status in self.status_count:
                self.status_count[status] += 1
                self.total_count += 1
        return item

    def close_spider(self, spider):
        """
        Метод, вызываемый при закрытии паука.
        Записывает результаты подсчета в CSV-файл.
        Дополнительно выводит общее число элементов.
        """
        for status, count in self.status_count.items():
            self.writer.writerow([status, count])
        self.writer.writerow(['Total', self.total_count])
        self.file.close()
