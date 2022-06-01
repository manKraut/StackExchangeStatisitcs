import time
import pandas as pd


def convert_json_to_csv(json_file):
    """
    :param json_file:
    :return: csv format
    """
    df = pd.DataFrame(flatten_json(json_file), index=[0])
    return df.to_csv()


def convert_json_to_html(json_file):
    """
    :param json_file: 
    :return: html format
    """
    df = pd.DataFrame(flatten_json(json_file), index=[0])
    return df.to_html()


def flatten_json(json_file):
    """
    This function gets a json file and unpack nested json to make it appropriate for DataFrame
    :param json_file:
    :return: flatten json_file
    """
    try:
        new_json = {}
        for key in json_file['top_ten_answers_comment_count']:
            new_json['top_ten_answers_comment_count/' + str(key)] = \
                json_file['top_ten_answers_comment_count'][key]

        del json_file["top_ten_answers_comment_count"]

        for key, value in new_json.items():
            json_file[key] = value
    except KeyError as exception:
        raise exception
    return json_file


def convert_string_to_epoch(date_time):
    """
    Gets datetime format like '%Y%m%d %H:%M:%S' and returns the epoch
    :param date_time:
    :return: epoch timestamp
    """
    pattern = '%Y%m%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    return epoch
