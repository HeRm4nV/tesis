from django.db import models

# SyllabicSegmentationActivity = 'SS'
# InitialSyllableIdentificationActivity = 'ISI'
# FinalSyllableIdentificationActivity = 'FSI'
# InitialSyllableOmissionActivity = 'ISO'
# FinalSyllableOmissionActivity = 'FSO'
# SyllabicInversionActivity = 'SI'
# InitialPhonemeIdentificationActivity = 'IPI'
# FinalPhonemeIdentificationActivity = 'FPI'
# InitialPhonemeOmissionActivity = 'IPO'
# PhonemicSynthesisActivity = 'PS'

# Create your models here.
class Activity(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    SyllabicSegmentationActivity = 'SS'
    InitialSyllableIdentificationActivity = 'ISI'
    FinalSyllableIdentificationActivity = 'FSI'
    InitialSyllableOmissionActivity = 'ISO'
    FinalSyllableOmissionActivity = 'FSO'
    SyllabicInversionActivity = 'SI'
    InitialPhonemeIdentificationActivity = 'IPI'
    FinalPhonemeIdentificationActivity = 'FPI'
    InitialPhonemeOmissionActivity = 'IPO'
    PhonemicSynthesisActivity = 'PS'

    types = [
        (SyllabicSegmentationActivity, 'Segmentación Silábica'),
        (InitialSyllableIdentificationActivity, 'Identificación de la sílaba inicial'),
        (FinalSyllableIdentificationActivity, 'Identificación de la sílaba final'),
        (InitialSyllableOmissionActivity, 'Omisión de sílaba inicial'),
        (FinalSyllableOmissionActivity, 'Omisión de sílaba final'),
        (SyllabicInversionActivity, 'Inversión silábica'),
        (InitialPhonemeIdentificationActivity, 'Identificación del fonema inicial'),
        (FinalPhonemeIdentificationActivity, 'Identificación del fonema final'),
        (InitialPhonemeOmissionActivity, 'Omisión de fonema inicial'),
        (PhonemicSynthesisActivity, 'Síntesis fonémica'),
    ]

    type = models.CharField(max_length=3, choices= types, default=SyllabicSegmentationActivity)

    #image = models.ImageField(upload_to ='static/images/', null=True, blank=True)
    typeImage = models.ImageField(upload_to='activities/media/images/', null=True, blank=True)

    class Meta:
        unique_together = ('type', 'name')

    def realName(self):
        return str(self.type) + '_' + str(self.name)

    def answer(self):
        self.save()

    def __str__(self):
        return self.realName()
