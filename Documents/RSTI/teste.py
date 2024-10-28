dic ={}

def func(a, b):
    for _ in range (50):
        print ("funcionando")
    try:
        return a / b
    except ZeroDivisionError:
        print("ZeroDivisionErro")
    except Exception as e:
        print(f"ocorreu um erro: {e}")    
        