class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        :type maxNumbers: int
        """
        self.isSlotAvailable = [True for i in range(maxNumbers)]
        self.freeslots = deque(range(maxNumbers))

    def get(self):
        """
        :rtype: int
        """
        if self.freeslots:
            rv = self.freeslots.popleft()
            self.isSlotAvailable[rv] = False
            return rv
        return -1


    def check(self, number):
        """
        :type number: int
        :rtype: bool
        """
        return self.isSlotAvailable[number]
        

    def release(self, number):
        """
        :type number: int
        :rtype: None
        """
        if not self.isSlotAvailable[number]:
            self.freeslots.append(number)
            self.isSlotAvailable[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)