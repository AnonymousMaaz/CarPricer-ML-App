from django import forms


class CarInputForm(forms.Form):
    year = forms.IntegerField(label="Year of Manufacture")
    kms_driven = forms.IntegerField(label="Kilometers Driven")
    owner = forms.ChoiceField(
        label="Owner (as in dataset)",
        choices=[
            ("First Owner", "First Owner"),
            ("Second Owner", "Second Owner"),
            ("Third Owner", "Third Owner"),
            ("Fourth & Above Owner", "Fourth & Above Owner"),
            ("Test Drive Car", "Test Drive Car"),
        ],
    )
    fuel_type = forms.ChoiceField(
        label="Fuel Type",
        choices=[
            ("Petrol", "Petrol"),
            ("Diesel", "Diesel"),
            ("CNG", "CNG"),
        ],
    )
    seller_type = forms.ChoiceField(
        label="Seller Type",
        choices=[
            ("Dealer", "Dealer"),
            ("Individual", "Individual"),
        ],
    )
    transmission = forms.ChoiceField(
        label="Transmission",
        choices=[
            ("Manual", "Manual"),
            ("Automatic", "Automatic"),
        ],
    )

