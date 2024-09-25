class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hs = {}
        ans = []
        for act in transactions:
            name, time, amount, city = act.split(',')
            time = int(time)
            if time in hs:
                if name in hs[time]:
                    hs[time][name].append(city)
                else:
                    hs[time][name] = [city]
            else:
                hs[time] = {name: [city]}
        

        for act in transactions:
            name, time, amount, city = act.split(',')
            print(amount)
            time = int(time)
            if int(amount) > 1000:
                ans.append(act)
                continue
            for i in range(time-60, time+61):
                if i in hs:
                    if name in hs[i]:
                        if len(hs[i][name]) > 1 or hs[i][name][0] != city:
                            ans.append(act)
                            break
        return ans
