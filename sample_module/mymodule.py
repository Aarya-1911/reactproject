def check(num):
    if(num<100):
        raise ValueError("num should b greater than 100")
    else:
        print("valid")
