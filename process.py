import csv

average_position: int = 1
volume_position: int = 2
decrease_weight: int = 1
zero: int = 0
alternatives: float = 10


class Ranking:

    def __init__(self):
        """
        When creating a Ranking instance, after defining the attributes.
        Calls will be made to function that will process the file and prepare it to obtain the ranking.
        """
        # attributes
        self.path: str = "datos.csv"
        self.ranking: dict = {}
        # call to previous functions
        self.__save_questions()
        self.__accumulated_sum()
        self.__calculate_ranking()

    def __save_questions(self):
        """
        Reads only the first row to store the question in the ranking dictionary with a default value of zero.
        """
        with open(self.path, newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file, delimiter=';')
            first_row = next(csvreader)
            for idx, answer in enumerate(first_row):
                self.ranking[idx] = [answer, zero, zero]

    def __accumulated_sum(self):
        """
        Calculates the accumulated sum of the answers with the respective calculation (answer x weight).
        It also adds up the accumulated volume of answers.
        """
        with open(self.path, newline='', encoding='utf-8') as file:
            csvreader = csv.reader(file, delimiter=';')
            next(csvreader)
            weight = alternatives
            for row in csvreader:
                for idx, answer in enumerate(row):
                    position_result = float(answer) * float(weight)
                    self.ranking[idx][average_position] += position_result
                    self.ranking[idx][volume_position] += float(answer)
                if weight == 1:
                    weight = alternatives + 1
                weight -= decrease_weight

    def __calculate_ranking(self):
        """
        Calculates the calculation of the accumulated sum against the volume of answers.
        """
        for key, rank in self.ranking.items():
            division = round(float(rank[average_position]) / float(rank[volume_position]), 2)
            rank[average_position] = division

    def get_ranking(self, desc: bool) -> list:
        """
        Sorts the ranking and returns only the sorted list.
        :param desc: If you want the ranking in ascending or descending order
        :return list: Returns ranking
        """
        ranking_sorted = sorted(self.ranking.items(), key=lambda rank: rank[1][1], reverse=desc)
        ranking_formatted = list(map(lambda val: val[1], ranking_sorted))
        return ranking_formatted


if __name__ == '__main__':
    ranking = Ranking()
    ranking_result = ranking.get_ranking(desc=True)
    print('Ranking: ')
    for index, item in enumerate(ranking_result):
        ask, value, accum = item
        print('{index}. {ask} ({value})'.format(index=(index + 1), ask=ask, value=value))
