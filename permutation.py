import unittest
from copy import deepcopy
from itertools import permutations

class MyTestCase(unittest.TestCase):

    def permutation_generator(self, input):
        def l(acc, _l):
            if not _l:
                yield acc
                return

            for idx, ele in enumerate(acc):
                yield from l(acc + [ele], _l[:idx] + _l[idx + 1:])

        return l([], input)

    def permutation_with_built_in(self, _list):
        _permu = []
        for i in range(1, len(_list) + 1):
            _permu.extend(permutations(_list, i))
        return [list(item) for item in _permu]

    def permutation(self, input):
        answer = []

        def l(acc, _l):
            if len(_l) == 0:
                return

            for idx, ele in enumerate(_l):
                _acc = acc[0:len(acc)]
                _list = _l[0:len(_l)]
                _acc.append(ele)
                answer.append(_acc)

                l(_acc, _l[0:idx] + _l[idx + 1:])

        l([], input)

        return sorted(answer, key=lambda x: len(x))

    def permutation2(self, input):
        answer = []

        def l(acc, _l):
            if len(_l) == 0:
                return

            for ele in _l:
                _acc = deepcopy(acc)
                _list = deepcopy(_l)
                _acc.append(ele)
                answer.append(_acc)
                _list.remove(ele)

                l(_acc, _list)

        l([], input)

        return sorted(answer, key=lambda x: len(x))


    def test_1(self):
        case = [1,2,3,4]
        result = self.permutation(case)
        expected = self.permutation_with_built_in(case)
        self.assertEqual(result, expected)  # add assertion here

    def test_2(self):
        case = [1,2,3,4,5,6]
        result = yield self.permutation_generator(case)
        expected = self.permutation_with_built_in(case)
        self.assertEqual(result, expected)

    def test_3(self):
        case = [1,2,3,4,5,6,7,8,9,10,11]
        result = yield self.permutation_generator(case)
        expected = self.permutation_with_built_in(case)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
