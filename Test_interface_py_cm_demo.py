#!/usr/bin/env python
#coding: utf-8
# @Date    : 2018-03-08 17:53:19
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import unittest,requests,json,MySQLdb
from parameterized import parameterized

class Test_interface_py_cm(unittest.TestCase):

	def setUp(self):
		print("<<<<<< start test >>>>>>")
		self.base_url = "http://192.168.11.67:8063/api/"
		self.s = requests.Session()
		self.headers = {'content-type': 'application/json;charset=UTF-8'}

	def tearDown(self):
		print("<<<<<< end test >>>>>>\n")

	@parameterized.expand([
			(1,1,0),
			(1,100,0)
			])
	def test1(self,arg_page,arg_pagesize,message):
		data = {"minTimes": 9}
		r = self.s.post(self.base_url + "intellif/mining/analysis/community/stranger/list/page/" + str(arg_page) + "/pagesize/" + str(arg_pagesize),data=json.dumps(data),headers=self.headers)
		result = r.json()
		print(result)
		self.assertEqual(r.status_code,200)
		self.assertEqual(result["errCode"],message)
		# self.assertEqual(result['data'][0]['id'], '31598')
		r.connection.close()

	# @unittest.skip(1)
	def test2(self):
		db = MySQLdb.connect("192.168.11.67","root","introcks1234","intellif_mining")
		cursor = db.cursor()
		cursor.execute("SELECT id,created,updated,face_url,indexed,source_face_id,version,label FROM t_community_stranger_detail")
		data = cursor.fetchone()
		print(data)

# def create_test(name, arg_page, arg_pagesize):
# 		def test1(self):
# 			data = {"minTimes": 9}
# 			r = self.s.post(
# 				self.base_url + "intellif/mining/analysis/community/stranger/list/page/" + str(arg_page) + "/pagesize/" + str(arg_pagesize),
# 				data=json.dumps(data), headers=self.headers)
# 			result = r.json()
# 			self.assertEqual(r.status_code, 200)
# 			self.assertEqual(result["errCode"], 0)
# 			# self.assertEqual(result['data']['name'], '31598')
# 			r.connection.close()
# 		setattr(Test_interface_py_cm, name, test1)

# create_test(name='test1_1', arg_page=1, arg_pagesize=10)
# create_test(name='test1_2', arg_page='', arg_pagesize='')
# create_test(name='test1_3', arg_page=1, arg_pagesize='')
# create_test(name='test1_4', arg_page='', arg_pagesize=20)


# def runner():
# 	suite = unittest.TestSuite()
# 	suite.addTest(Test_interface_py_cm('test1'))
# 	unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
	unittest.main()