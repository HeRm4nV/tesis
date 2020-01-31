from django.shortcuts import render
from .models import Activity

# Create your views here.
def activities_types_list(request):

    activitiesTypes =[
    {'name':'Segmentación Silábica', 'type': 'SyllabicSegmentationActivity'},
    {'name':'Identificación de la sílaba inicial', 'type': 'InitialSyllableIdentificationActivity'},
    {'name':'Identificación de la sílaba final', 'type': 'FinalSyllableIdentificationActivity'},
    {'name':'Omisión de sílaba inicial', 'type': 'InitialSyllableOmissionActivity'},
    {'name':'Omisión de sílaba final', 'type': 'FinalSyllableOmissionActivity'},
    {'name':'Inversión silábica', 'type': 'SyllabicInversionActivity'},
    {'name':'Identificación del fonema inicial', 'type': 'InitialPhonemeIdentificationActivity'},
    {'name':'Identificación del fonema final', 'type': 'FinalPhonemeIdentificationActivity'},
    {'name':'Omisión de fonema inicial', 'type': 'InitialPhonemeOmissionActivity'},
    {'name':'Síntesis fonémica', 'type': 'PhonemicSynthesisActivity'},
    ]

    return render(request, 'activities/activities_types_list.html', {'activitiesTypes': activitiesTypes})

def sources(request, activityName):

    return render(request, 'activities/sources/'+activityName+'.html', {'activityName': activityName})

def js(request, activityName):

    return render(request, 'activities/js/'+activityName+'.js', {'activityName': activityName})

def activities_list(request, type):

    types = {
	'SyllabicSegmentationActivity': 'SS',
    'InitialSyllableIdentificationActivity': 'ISI',
    'FinalSyllableIdentificationActivity': 'FSI',
    'InitialSyllableOmissionActivity': 'ISO',
    'FinalSyllableOmissionActivity': 'FSO',
    'SyllabicInversionActivity': 'SI',
    'InitialPhonemeIdentificationActivity': 'IPI',
    'FinalPhonemeIdentificationActivity': 'FPI',
    'InitialPhonemeOmissionActivity': 'IPO',
    'PhonemicSynthesisActivity': 'PS'
    }

    activitiesTypes = {
    'SyllabicSegmentationActivity': 'Segmentación Silábica',
    'InitialSyllableIdentificationActivity': 'Identificación de la sílaba inicial',
    'FinalSyllableIdentificationActivity': 'Identificación de la sílaba final',
    'InitialSyllableOmissionActivity': 'Omisión de sílaba inicial',
    'FinalSyllableOmissionActivity': 'Omisión de sílaba final',
    'SyllabicInversionActivity': 'Inversión silábica',
    'InitialPhonemeIdentificationActivity': 'Identificación del fonema inicial',
    'FinalPhonemeIdentificationActivity': 'Identificación del fonema final',
    'InitialPhonemeOmissionActivity': 'Omisión de fonema inicial',
    'PhonemicSynthesisActivity': 'Síntesis fonémica',
    }

    activities = Activity.objects.filter(type=types[type])

    return render(request, 'activities/activities_list.html', {'activities': activities, 'type': activitiesTypes[type]})
