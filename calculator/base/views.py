from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpRequest

def main(request:HttpRequest,*args,**kwargs)-> HttpResponse:
    context = {}
    return render(request,'base/calculator.html',context)

def calculate(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        number_one = request.POST.get("number_one")
        number_two = request.POST.get("number_two")
        operation = request.POST.get("operation")

        if number_one and number_two and operation:
            number_one = float(number_one)
            number_two = float(number_two)

            if operation == "add":
                result = number_one + number_two
            elif operation == "subtract":
                result = number_one - number_two
            elif operation == "multiply":
                result = number_one * number_two
            elif operation == "divide":
                result = number_one / number_two if number_two != 0 else "Error: division by zero"
            else:
                result = "Unknown operation"

            return render(request, "base/calculator.html", {"result": result})

    return render(request, "base/calculator.html", {})