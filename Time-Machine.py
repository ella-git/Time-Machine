def programming_language_era(year):
   
    if year < 1950:
        return "1950年之前，计算机程序主要以机器语言编写，非常依赖于特定的硬件。"
    elif 1950 <= year <= 1957:
        return "1950年代，汇编语言开始出现，它是一种低级语言，比机器语言更易于理解和编写。"
    elif 1958 <= year <= 1969:
        return "1958年，FORTRAN语言诞生，标志着高级编程语言的开始。这个时期，高级语言逐渐成为主流。"
    else:
        return "1970年以后，高级语言如C、C++、Java、Python等层出不穷，极大地丰富了编程语言的选择。"

def main():
    print("欢迎来到时光机——历史编程语言大冒险！")
    year = int(input("请输入一个年份，了解那个时代的编程语言类别："))
    era_info = programming_language_era(year)
    print(era_info)

if __name__ == "__main__":
    main()