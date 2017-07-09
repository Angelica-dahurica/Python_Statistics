import csv

class Solution():

	def solve(self):
		csv_reader = csv_reader = csv.reader(open('exhaust_emission_2014.csv'))
		list_old = []
		for row in csv_reader:
			list_old.append(row[1])

		list_old = list_old[6:37]
		print list_old


if __name__ == '__main__':
	S = Solution()
	S.solve()
