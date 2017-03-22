#probability.py  Author: Akira Hakuta, Date: 2017/03/22

def distinct_prob(n):
    year_day=365.0
    d = year_day - 1
    p = 1.0
    for k in range(1,n):
        p *= d/year_day
        d -=1
    return p
        
    
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    cnum_max=100
    x_list=[]
    y_list=[]
    for x in range(2, cnum_max+1):
        x_list +=[x]
        y_list +=[1-distinct_prob(x)]

    #print(x_list)
    #print(y_list)
    plt.plot(x_list, y_list, 'o')
    plt.title('')
    plt.xlabel('n: number of persons')
    plt.ylabel('p: probability at least 2 the same')
    plt.grid(True)  
    plt.xlim(0,100)
    plt.ylim(0,1)
    plt.savefig('birthdayProb.pdf')
    #plt.savefig('birthdayProb.eps') 
    plt.show()
    cnum=40# number of persons in my class
    print('There are {} persons in my class. The Birthday-Problem\'s probability is {:0.3f}.'.format(cnum, 1-distinct_prob(cnum)))
    
    