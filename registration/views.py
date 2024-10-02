from django.shortcuts import render,redirect
from app.models import Registration, Event,Team,TeamMember
from django.http import HttpResponse
def HOME(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        # Extract individual records from the form
        leader_name = request.POST.get('name')
        college = request.POST.get('college')
        department = request.POST.get('dept')
        paper_title = request.POST.get('paper_title')
        paper_submission_link = request.POST.get('paper_link')
        payment_link = request.POST.get('payment_link')
        transaction_number = request.POST.get('transaction_num')
        whatsapp_group_link = request.POST.get('whatsapp_link')
        team_name = request.POST.get('team_name')
        technical_events = request.POST.getlist('technical_events')
        non_technical_events = request.POST.getlist('non_technical_events')

        # Create or get the team
        team, created = Team.objects.get_or_create(name=team_name)

        # Create a new Registration instance
        registration = Registration(
            team_name=team,
            college=college,
            department=department,
            paper_title=paper_title,
            paper_submission_link=paper_submission_link,
            payment_link=payment_link,
            transaction_number=transaction_number,
            whatsapp_group_link=whatsapp_group_link,
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
        )

        # Generate paper_id
        count = Registration.objects.count() + 1
        registration.paper_id = f'CISABZ/CSE/{count:02d}'
        registration.save()  # Save the registration first

        # Create team members
        team_members = [
            {
                'name': leader_name,
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),
                'technical_events': technical_events,
                'non_technical_events': non_technical_events
            },
            {
                'name': request.POST.get('member2_name'),
                'email': request.POST.get('member2_email'),
                'phone': request.POST.get('member2_phone'),
                'technical_events': request.POST.getlist('member2_technical_events'),
                'non_technical_events': request.POST.getlist('member2_non_technical_events')
            },
            {
                'name': request.POST.get('member3_name'),
                'email': request.POST.get('member3_email'),
                'phone': request.POST.get('member3_phone'),
                'technical_events': request.POST.getlist('member3_technical_events'),
                'non_technical_events': request.POST.getlist('member3_non_technical_events')
            },
        ]

        for member_data in team_members:
            member = TeamMember(
                registration=registration,
                name=member_data['name'],
                email=member_data['email'],
                phone=member_data['phone']
            )
            member.save()

            # Add selected technical events for the member
            for event_name in member_data['technical_events']:
                event_instance, created = Event.objects.get_or_create(name=event_name, event_type='technical')
                member.technical_events.add(event_instance)

            # Add selected non-technical events for the member
            for event_name in member_data['non_technical_events']:
                event_instance, created = Event.objects.get_or_create(name=event_name, event_type='non_technical')
                member.non_technical_events.add(event_instance)

        # After saving, redirect to a success page with the paper ID
        return render(request, 'success.html', {'paper_id': registration.paper_id})

    return render(request, 'home.html')


def search_paper_id(request):
    results = []
    if request.method == 'POST':
        paper_id = request.POST.get('paper_id')
        try:
            registration = Registration.objects.get(paper_id=paper_id)
            members = registration.members.all()  # Get all members associated with the registration
            results = {
                'registration': registration,
                'members': members,
            }
        except Registration.DoesNotExist:
            results = None  # No registration found

    return render(request, 'search.html', {'results': results})
