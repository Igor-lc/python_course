class AvgList(list):
    def __init__(self, lst):
        super().__init__()
        self.data = sorted(lst)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median_low(self):
        if len(self.data) & 1:
            return self.data[int(len(self.data) / 2)]
        return self.data[int(len(self.data) / 2) - 1]

    def median_high(self):
        if len(self.data) & 1:
            return self.data[int(len(self.data) / 2)]
        return self.data[int(len(self.data) / 2)]

    def median(self):
        if len(self.data) & 1:
            return self.data[int(len(self.data) / 2)]
        return (self.data[int(len(self.data) / 2)] + self.data[int(len(self.data) / 2) - 1]) / 2

    def __repr__(self):
        return repr(self.data)

    def append(self, value):
        self.data.append(value)
        super().append(value)

avg_list = AvgList([1, 2, 3, 4, 5, 6, 7])
avg_list.append(11)
print(avg_list.mean())
print(avg_list)


'''320. LIST AVERAGES
Difficulty: 6 out of 10
Create an AvgList class to get the arithmetic mean and median of a list.

AvgList must be derived from the list class, which is the main class for lists in Python.

The class must contain the following methods:

mean() - returns the arithmetic mean.
median() - Returns the median or average from a list. If the number of elements in the list is even, then the median returns the average between the two central ones.
median_low() - returns the median, but if the number of elements in the list is even, then returns the smaller (left) of the two central elements.
median_high() - returns the median, but if the number of elements in the list is even, then returns the larger (right) of the two center elements.'''
