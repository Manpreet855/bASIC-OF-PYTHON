def main():
    try:
        a=int(input("hey, enter a number: "))
        print(a)
        return


        
    except Exception as e:
        print(e)
        return



    finally:# finally alway run even in you use return
        print("I am inside finally")


main()