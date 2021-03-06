import unittest
import requests
import json

ip = 'https://dailydiet-api.herokuapp.com/'
# ip = 'http://127.0.0.1:5000'
class TestDiet(unittest.TestCase):

    def test_sevade(self):
        r = requests.post(ip + '/food/sevade/2300')
        result = r.json()
        assert result['diet'][3] in range(2990, 2310, 1), 'Test Failed :('

    def test_zero_sevade(self):
        r = requests.post(ip + '/food/sevade/0')
        assert r.status_code == 418, 'Khak bar saret :('

    def test_dovade(self):
        r = requests.post(ip + '/food/dovade/4300')
        result = r.json()
        assert result['diet'][2] in range(2990, 2310, 1), 'Test Failed :('

    def test_zero_dovade(self):
        r = requests.post(ip + '/food/dovade/0')
        assert r.status_code == 418, 'Khak bar saret :('

    def test_yevade(self):
        r = requests.post(ip + '/food/yevade/400')
        result = r.json()
        assert result['diet'][1] in range(390, 410, 1), 'Test Failed :('

    def test_zero_yevade(self):
        r = requests.post(ip + '/food/yevade/0')
        assert r.status_code == 418, 'Khak bar saret :('

if __name__ == '__main__':
    unittest.main()
