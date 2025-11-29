from django.shortcuts import render , redirect
from .services import TogetherAIClient

def chatbot_view(request):
    response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input',"").strip()
        if user_input:
              # Step 1: create the client instance
            client = TogetherAIClient()
             # Step 2: call the method to get response
            response_text = client.get_response(user_input)
            request.session["last_response"] = response_text
        # return re-direct doesn't sumbit form 
        return redirect("chatbot")
      
      # GET we stored 
    response = request.session.pop("last_response",None)
    return render(request, 'chatbot.html', {'response': response})
