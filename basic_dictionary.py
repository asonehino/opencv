nation = {'Korea':"+82", 'US':"+1", 'Japan': "+81"}
print(nation['Korea'])

var = input()

if (var in nation):
    print('country code = ', nation['US'])
else:
    print('something wrong')