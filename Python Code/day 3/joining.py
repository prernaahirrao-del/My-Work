print("job eligibility")
first_round = float(input("Enter the marks"))
if first_round >=70:
    print("written exam pass")
    second_round = float(input("Enter the marks"))
    if second_round >= 80:
        print("code round pass")
        last_round = float(input("Enter the marks"))
        if last_round >= 90:
            print("HR round completed")
        else:
            print("failed first round")
    else:
        print("not eligible for second round")
else:       
    print("rejected")
