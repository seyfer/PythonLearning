import pandas


def init():
    data = pandas.read_csv('titanic.csv', index_col='PassengerId')
    return data


def test():
    # print(data[:10])
    print(data.head(10))
    # print(data['Pclass'])
    # print(data['Pclass'].value_counts())


# male 577 female 314
def task1():
    print(data['Sex'].value_counts())


# survived 342 not survived 549
def task2():
    print(data['Survived'].value_counts())

    # 549 100
    # 342 x
    # 62.2950819672
    survived = data['Survived'].value_counts()[1];
    notSurvived = data['Survived'].value_counts()[0];
    print(survived * 100 / notSurvived)


def task3():
    classesData = data['Pclass'].value_counts()
    classesData.sort_index()

    # 3    491
    # 1    216
    # 2    184
    print(classesData)

    # 3    0.551066
    # 1    0.242424
    # 2    0.206510
    pcts = classesData / classesData.sum()
    print(pcts)

    # class1 = data['Pclass'].value_counts()[1]
    # class2 = data['Pclass'].value_counts()[2]
    # class3 = data['Pclass'].value_counts()[3]

    # 491    0.333333
    # 184    0.333333
    # 216    0.333333
    # print(100. * classesData.value_counts() / len(classesData))
    # print(classesData.value_counts(normalize=True))


def task4():
    passAges = data['Age']
    print(passAges)

    # 29.6991176471
    print(passAges.mean())

    # 28.0
    print(passAges.median())
    return


def task5():
    sibSpAndParch = data[['SibSp', 'Parch']];
    print(sibSpAndParch)

    # SibSp  1.000000  0.414838
    # Parch  0.414838  1.000000
    print(sibSpAndParch.corr())


# -----------------

data = init()
test()

# task1()

# task2()

# task3()

# task4()

# task5()
