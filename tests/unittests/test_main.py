from stackstats import main


def test_get_stats_fail():
    stats = main.GetStatistics('since_test', 'until_test')
    inpt = {'items': [{'owner': {'account_id': 52616,
   'reputation': 958272,
   'user_id': 157247,
   'user_type': 'registered',
   'accept_rate': 91,
   'profile_image': 'https://i.stack.imgur.com/k5zK1.jpg?s=256&g=1',
   'display_name': 'T.J. Crowder',
   'link': 'https://stackoverflow.com/users/157247/t-j-crowder'},
  'is_accepted': True,
  'score': 7,
  'last_activity_date': 1652969047,
  'last_edit_date': 1652969047,
  'creation_date': 1591085621,
  'answer_id': 62147629,
  'question_id': 62147521,
  'content_license': 'CC BY-SA 4.0'},]}
    expected = {}

    assert stats.get_stats_answers(inpt) != expected
