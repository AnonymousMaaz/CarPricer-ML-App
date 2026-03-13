from django.shortcuts import render

from .forms import CarInputForm
from .services import predict_selling_price


def predict_price(request):
    predicted_price = None
    form = CarInputForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        predicted_price = predict_selling_price(form.cleaned_data)

    return render(
        request,
        "predictor/predict_form.html",
        {
            "form": form,
            "predicted_price": predicted_price,
        },
    )
