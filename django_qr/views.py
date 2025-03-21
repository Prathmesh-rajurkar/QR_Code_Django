from django.shortcuts import render
from . import forms
import qrcode
import os 
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = forms.QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            qr = qrcode.make(url)
            print(qr)
            res_name_file = res_name.replace(' ','_').lower()
            filename = f'qr_code_{res_name_file}.png'
            filepath = f'media/qr_code_{res_name_file}.png'
            qr.save(filepath)

            qr_url = os.path.join(settings.MEDIA_URL,filename)

            context = {
                'res_name':res_name,
                'qr_url':qr_url,
                'filename':filename,
            }
            return render(request,'qr_result.html',context)
    else:
        form = forms.QRCodeForm()
        context = {'form': form}
        return render(request,'generate_qr_code.html',context)