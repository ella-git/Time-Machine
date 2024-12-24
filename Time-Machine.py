def programming_language_era(year):
    # 根据年份返回编程语言的类别
    if year < 1950:
        return "1950年之前，早期的程序设计语言是由”0“和”1“所代表的二进制代码指令组成，这样的语言可以直接被计算机接收和执行，被称为”机器语言“。优点:在这些指令的控制下，计算机可以实现最基本的算术运算和逻辑运算，缺点:这种机器语言难以被理解，程序设计任务也繁重"
    elif 1950 <= year <= 1957:
        return "1950年代，汇编语言开始出现，优点：比较容易理解读懂程序，维护程序更加便捷。缺点：汇编语言的移植性不好"
    else:
        return "1958年，FORTRAN语言诞生，标志着高级编程语言的开始。高级语言如C、C++、Java、Python等层出不穷。优点：移植性好，语言容易被理解"


def main():
    while True:  # 创建一个无限循环，直到用户选择退出
        print("\n欢迎来到时光机——历史编程语言大冒险！")
        year = input("请输入一个年份，了解那个时代的编程语言类别（输入'exit'退出）：")
        if year.lower() == 'exit':  # 检查用户是否输入'exit'来退出程序
            print("感谢使用时光机程序，再见！")
            break  # 退出循环，结束程序
        try:
            year = int(year)  # 尝试将输入转换为整数
            era_info = programming_language_era(year)
            print(era_info)
        except ValueError:  # 处理非整数输入的情况
            print("请输入一个有效的年份或'exit'来退出。")


if __name__ == "__main__":
    main()
