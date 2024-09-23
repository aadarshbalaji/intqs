class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        timetorest = {}
        ans = []
        for t in transactions:
            actions = t.split(',')
            name, time, amount, city = actions
            time = int(time)
            if time in timetorest:
                if name in timetorest[time]:
                    timetorest[time][name].append(city)
                else:
                    timetorest[time][name] = [city]
            else:
                timetorest[time] = {name: [city]}
        
        for t in transactions:
            actions = t.split(',')
            name, time, amount, city = actions
            time = int(time)
            amount = int(amount)
            #print(name, time, amount, city)
            
            if amount > 1000:
                ans.append(t)
                continue
            
            for i in range(time-60, time+61):
                if i in timetorest:
                    if name in timetorest[i]:
                        if len(timetorest[i][name]) > 1 or timetorest[i][name][0] != city:
                            ans.append(t)
                            break
                            
        return ans