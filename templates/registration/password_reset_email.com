Qualcuno ha richiesto un password reset per l'account associato alla mail{{ email }}. Segui il link per procedere:
{{ protocol}}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}