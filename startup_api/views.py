import pickle

import pandas as pd
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .forms import CustomerForm
from .models import Customer
from .serializer import CustomerSerializers


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


def status(X):
    try:
        model_status = pickle.load(open('predicted_status.sav', 'rb'))
        model_top = pickle.load(open('predicted_top.sav', 'rb'))
        y_pred_status = model_status.predict(X)
        y_pred_top = model_top.predict(X)

        active = 'Your startup will exist for more than 6 years (average closing time)'
        active_top = 'be in the top-500 of the most successful startups during this time.'
        closed = 'Your startup won\'t exist for more than 6 years (average closing time)'
        closed_top = 'be in the top-500 of the most successful startups before it closed.'

        if y_pred_status == 0 and y_pred_top == 1:
            predict = active + ' and ' + active_top
        elif y_pred_status == 0 and y_pred_top == 0:
            predict = active + ' but not ' + active_top
        elif y_pred_status == 1 and y_pred_top == 1:
            predict = closed + ' but ' + closed_top
        else:
            predict = closed + ' and not ' + closed_top

        return predict
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def FormView(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST or None)

        if form.is_valid():

            city = form.cleaned_data['city']
            category = form.cleaned_data['category']
            avg_members = form.cleaned_data['avg_members']
            relationships = form.cleaned_data['relationships']
            milestones = form.cleaned_data['milestones']
            funding_rounds = form.cleaned_data['funding_rounds']
            round_a = form.cleaned_data['round_a']
            round_b = form.cleaned_data['round_b']

            columns = ['is_CA', 'is_NY', 'is_MA', 'is_TX', 'is_otherstate',
                       'is_software', 'is_web', 'is_mobile', 'is_enterprise', 'is_advertising', 'is_gamesvideo',
                       'is_ecommerce', 'is_biotech', 'is_consulting', 'is_othercategory']

            df = pd.DataFrame(columns=columns)

            for i in columns:
                if i == city or i == category:
                    df[i] = [1]
                else:
                    df[i] = [0]

            df['avg_participants'] = [int(avg_members)]
            df['relationships'] = [int(relationships)]
            df['milestones'] = [int(milestones)]
            df['funding_rounds'] = [int(funding_rounds)]

            df['has_roundA'] = [1 if round_a == 'on' else 0]
            df['has_roundB'] = [1 if round_b == 'on' else 0]

            result = status(df)
            return render(request, 'status.html', {'data': result})

    form = CustomerForm()
    return render(request, 'form.html', {'form': form})
