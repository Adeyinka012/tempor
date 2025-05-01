def shutdown():
    confirmation=input("are you sure you want to shut down (yes/no)").strip().lower()
    if confirmation == 'yes':
        print("shuting down.....")
    elif confirmation == 'no':
        print("shutdown cancelled")
    else:
        print("please select the right input (yes/no)")
shutdown()
        
        