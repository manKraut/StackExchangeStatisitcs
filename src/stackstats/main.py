import argparse
import logging
import requests
from . import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("assignment_encode")


class GetStatistics:
    def __init__(self, since, until):
        self.since = since
        self.until = until
        self.api = "https://api.stackexchange.com/2.3/answers"

    def get_answers(self):
        """
        Calls stackExchange API to get answers
        :return: answers
        """
        endpoint = f"{self.api}?fromdate={self.since}&todate={self.until}&site=stackoverflow"
        resp = requests.get(endpoint)
        return resp.json()

    def get_comments_for_specific_answer(self, answer_id):
        endpoint = f"{self.api}/{int(answer_id)}/comments?&site=stackoverflow"
        resp = requests.get(endpoint)
        return resp.json()

    @staticmethod
    def get_stats_answers(answers):
        """
        get an array with answers and extract statistics
        :param answers:
        :return:
        average_answers_per_question
        accepted_answers_average_score
        total_accepted_answers
        """
        total_accepted_answers = 0
        score_sum = 0
        unique_questions = set()
        for answer in answers['items']:
            unique_questions.add(answer['question_id'])
            if answer['is_accepted']:
                total_accepted_answers += 1
                score_sum += answer['score']

        accepted_answers_average_score = score_sum / total_accepted_answers
        average_answers_per_question = len(unique_questions) / len(answers['items'])
        return average_answers_per_question, accepted_answers_average_score, total_accepted_answers

    def get_comments_for_answers(self, answers):
        comments_for_answers = {}
        for answer in answers:
            answer_id = answer['answer_id']
            comments_in_json = self.get_comments_for_specific_answer(answer_id)
            comments_for_answers[answer_id] = len(comments_in_json['items'])
        return comments_for_answers

    def run(self):
        """
        run the pipeline
        :return: output
        """
        logger.info("Getting answers...")
        answers_json = self.get_answers()
        logger.info("Answers collected")

        logger.info("Running analysis on answers...")
        average_answers_per_question, accepted_answers_average_score, total_accepted_answers = \
            self.get_stats_answers(answers_json)
        logger.info("Analysis Done")

        top_answers = sorted(answers_json['items'], key=lambda k: k['score'], reverse=True)[:10]

        logger.info("Getting comments for top 10 answers...")
        comments_for_answers = self.get_comments_for_answers(top_answers)
        logger.info("Comments collected")

        data = {
            "total_accepted_answers": total_accepted_answers,
            "accepted_answers_average_score": accepted_answers_average_score,
            "average_answers_per_question": round(average_answers_per_question, 1),
            "top_ten_answers_comment_count": comments_for_answers
        }

        return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("since", nargs='+')
    parser.add_argument("until", nargs='+')
    parser.add_argument("--output-format", choices=["csv", "html", "json"], default="json",
                        type=lambda x: x.lower())

    args = parser.parse_args()

    logger.info("Getting statistics from StackExchange API since %s until %s",
                args.since[0], args.until[0])

    logger.info("You will receive you results in %s format", args.output_format)

    since_epoch = utils.convert_string_to_epoch(args.since[0])
    until_epoch = utils.convert_string_to_epoch(args.until[0])

    get_statistics = GetStatistics(since_epoch, until_epoch)
    stats_json = get_statistics.run()

    logger.info("Statistics analysis Done!")
    logger.info("Statistics:")

    if args.output_format == "json":
        print(stats_json)
    elif args.output_format == "csv":
        print(utils.convert_json_to_csv(stats_json))
    elif args.output_format == "html":
        print(utils.convert_json_to_html(stats_json))


if __name__ == "__main__":
    main()
