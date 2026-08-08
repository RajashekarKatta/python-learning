# Number Gussing Game Usiing Binary search

class Solution:
    def guess_number(self, startrange, endrange):
        if startrange > endrange:
            return True
          
        mid = (startrange + endrange)//2
        print(f"Is the number {mid}? (Y/N): ", end="")
        user = input().strip()

        if user in ("y", "Y"):
            print("Congratulation User! Successfully Guessed Number.")
            return False

        elif user in ("N", "n"):
            print(f"Is the actual number greater than {mid}? (Y/N): ", end="")
            user = input().strip()

            if user in ("Y", "y"):
                return self.guess_number(mid + 1, endrange)
            elif user in ("N", "n"):
                return self.guess_number(startrange, mid - 1)
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
                return self.guess_number(startrange, endrange)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            return self.guess_number(startrange, endrange)

if __name__ == "__main__":
    print("Guessing the number")
    startrange = int(input("Enter the Startrange:"))
    endrange = int(input("Enter the endrange:"))

    print(f"Think of a number between {startrange} and {endrange}. I will try to guess it!")
    s = Solution()
    s.guess_number(startrange, endrange)