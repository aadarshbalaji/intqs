class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        ans = []
        hs = {}
        for i in range(len(transactions)):
            action = transactions[i]
            name, time, amount, city = action.split(',')
            time = int(time)
            amount = int(amount)
            if time not in hs:
                hs[time] = {name:[city]}
            else:
                if name not in hs[time]:
                    hs[time][name] = [city]
                else:
                    hs[time][name].append(city)
        #print(hs)
        for act in transactions:
            name, time, amount, city = act.split(',')
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                ans.append(act)
                continue
            for i in range(time-60, time+61):
                if i in hs:
                    if name in hs[i] and ((len(hs[i][name]) > 1 )or (hs[i][name][0] != city)):
                        ans.append(act)
                        break
        return ans