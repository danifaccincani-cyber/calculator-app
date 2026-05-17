import tkinter as tk

# Button grid configuration
def createButtons():
    
    button = [
        
        "7","8","9","/",
        "4","5","6","*",
        "1","2","3","-",
        "0",".","+","="  
    ]
    
    # CE button
    numbers = tk.Button(window, text="CE", command=lambda: removeValue("CE"))
    numbers.grid(row=2, column=3, sticky="nsew")
    
    # numbers and operator buttons
    for i, val in enumerate(button):
        numbers = tk.Button(window, text=val, command=lambda v=val: click(v))
        numbers.grid(row=(i // 4) + 3, column=i % 4,sticky="nsew")
        
def click(value):
    
    global firstNumber, operator, expression, justCalculated
    
    match value:
        
        #operator buttons
        case '+' | '-' | '*' | '/':
            
            if operator != "":
                
                secondNumber = display.get()
                expression+=secondNumber + value
                firstNumber = str(eval(firstNumber + operator + secondNumber))
                display.set(firstNumber)
            
            else:
                expression+=display.get() + value
                firstNumber = display.get()
                
            operator = value
            output_history.set(expression)
            
            
        case '=':
            
            try:
                if firstNumber == "":
                    display.set("Insert a value")
                    return
                
                secondNumber = display.get()
                expression+=secondNumber + "="
                output_history.set(expression)
                result = eval(firstNumber + operator + secondNumber)
                display.set(result)
                firstNumber = ""
                operator = ""
                expression = ""
                justCalculated = True
                
            except ZeroDivisionError:
                display.set("Error")
        
                
        # Number and decimal buttons
        case _:
            current_display = display.get()
    
            if current_display in ("Insert a value", "Error") or justCalculated:
                display.set(value)
                justCalculated = False
        
            elif operator == "":
                if current_display == "0":
                    display.set(value)
                else:
                    display.set(current_display + value)
            
            else:
                display.set(value)
                 
    
    


# Main window configuration
window = tk.Tk()

window.geometry("600x600")
window.title("calculator App")
window.resizable(False,False)


# Global variables
firstNumber = ""
operator = ""
expression = ""
justCalculated = False


# StringVar for display and history
display = tk.StringVar(value=0)
output_history = tk.StringVar(value="")


# history label - shows the expression
history_label = tk.Label(window, textvariable=output_history)
history_label.grid(row=0, column=0, columnspan=4, sticky="nsew")


# main display label - shows current number
label = tk.Label(window, textvariable=display)
label.grid(row=1, column=0, columnspan=4, sticky="nsew")


# grid configuration
for i in range(4):
    window.columnconfigure(i, weight=1)

    
window.rowconfigure(0, weight=1)
window.rowconfigure(1,weight=2)


# Row configuration for buttons
for i in range(2,7):
    window.rowconfigure(i, weight=2)


createButtons()    



if __name__ == "__main__":
    window.mainloop()       