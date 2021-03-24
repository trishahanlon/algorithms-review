import unittest


def merge_ranges(meetings):
    # Merge meeting ranges
    # Sort our input list of meetings by start time
    sorted_meetings = sorted(meetings)
    print(sorted_meetings)

    # we treat the meeting with the earlier start time as first and the other as second
    merged_meetings = [sorted_meetings[0]]
    print(merged_meetings)
    print(sorted_meetings[1:])
    print(merged_meetings[-1])

    # if the end time of the first meeting is equal to or greater than the start time of the second
    # meeting we merge the two meetings into one time range. the resulting time range's start time
    # is the first meeting's start, and it's end time is the later of the two meeting's end time
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        print("current_meeting_start: ", current_meeting_start)
        print("current_meeting_end: ", current_meeting_end)
        print("last_merged_meeting_start: ", last_merged_meeting_start)
        print("last_merged_meeting_end: ", last_merged_meeting_end)

        if (current_meeting_start <= last_merged_meeting_end):
            # merge
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
            print("merged meetings in if: ", merged_meetings)
        # else we leave them seperate
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))
            print("merged meeting in else:", merged_meetings)

    print('merged meetings at the end: ', merged_meetings)
    return merged_meetings


# Tests

class Test(unittest.TestCase):

    # def test_meetings_overlap(self):
    #     actual = merge_ranges([(1, 3), (2, 4)])
    #     expected = [(1, 4)]
    #     self.assertEqual(actual, expected)

    # def test_meetings_touch(self):
    #     actual = merge_ranges([(5, 6), (6, 8)])
    #     expected = [(5, 8)]
    #     self.assertEqual(actual, expected)

    # def test_meeting_contains_other_meeting(self):
    #     actual = merge_ranges([(1, 8), (2, 5)])
    #     expected = [(1, 8)]
    #     self.assertEqual(actual, expected)

    # def test_meetings_stay_separate(self):
    #     actual = merge_ranges([(1, 3), (4, 8)])
    #     expected = [(1, 3), (4, 8)]
    #     self.assertEqual(actual, expected)

    # def test_multiple_merged_meetings(self):
    #     actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
    #     expected = [(1, 8)]
    #     self.assertEqual(actual, expected)

    # def test_meetings_not_sorted(self):
    #     actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
    #     expected = [(1, 4), (5, 8)]
    #     self.assertEqual(actual, expected)

    # def test_one_long_meeting_contains_smaller_meetings(self):
    #     actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
    #     expected = [(1, 12)]
    #     self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)