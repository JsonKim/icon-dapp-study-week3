from ..sample_one import SampleOne
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestSampleOne(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.score = self.get_score_instance(SampleOne, self.test_account1)
