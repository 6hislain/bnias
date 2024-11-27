from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as login_me_in, logout as log_me_out
from .models import (
    Service,
    Publication,
    Province,
    Colline,
    Commune,
    LostIdCardReport,
    RegisteredIdCardApplication,
)


# Create your views here.
class ServiceList(ListView):
    paginate_by = 48
    queryset = Service.objects.order_by("-id")
    template_name = "service/index.html"


class ServiceDetail(DetailView):
    model = Service
    paginate_by = 48
    template_name = "service/show.html"


class PublicationList(ListView):
    paginate_by = 48
    queryset = Publication.objects.order_by("-id")
    template_name = "publication/index.html"


class PublicationDetail(DetailView):
    model = Publication
    paginate_by = 48
    template_name = "publication/show.html"


@login_required(login_url="/login")
@require_http_methods(["GET"])
def dashboard(request):
    return render(request, "dashboard/index.html")


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "GET":
        return render(request, "auth/register.html")

    elif request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == "" or password != confirm_password:
            messages.info(request, "Password do not match")
            return redirect("register")

        if email == "" or User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("register")

        if username == "" or User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect("register")

        new_user = User.objects.create_user(
            username=username, email=email, password=password
        )
        new_user.save()

        user_login = authenticate(username=username, password=password)
        login_me_in(request, user_login)

        return redirect("home")


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, "auth/login.html")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect("login")

        login_me_in(request, user)
        return redirect("home")


@login_required(login_url="login")
def logout(request):
    log_me_out(request)
    return redirect("home")


@require_http_methods(["GET", "POST"])
def apply(request):
    if request.method == "GET":
        communes = Commune.objects.all()
        collines = Colline.objects.all()
        provinces = Province.objects.all()
        return render(
            request,
            "apply.html",
            {"provinces": provinces, "collines": collines, "communes": communes},
        )

    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        gender = request.POST["gender"]
        birth_date = request.POST["birthdate"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        province = request.POST["province"]
        commune = request.POST["commune"]
        colline = request.POST["colline"]

        if RegisteredIdCardApplication.objects.filter(
            Q(email=email) | Q(phone=phone)
        ).exists():
            messages.info(request, "Application already sent")

        else:
            applicant = RegisteredIdCardApplication(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                birth_date=birth_date,
                phone=phone[:10],
                email=email,
                province_id=province,
                commune_id=commune,
                colline_id=colline,
            )

            if request.FILES.get("picture") is not None:
                applicant.image = request.FILES.get("applicant")

            applicant.save()
            messages.info(request, "Thank you for applying, we'll be in touch soon")

        return redirect("apply")


@login_required(login_url="/login")
@require_http_methods(["GET", "POST"])
def lost(request):
    if request.method == "GET":
        communes = Commune.objects.all()
        collines = Colline.objects.all()
        provinces = Province.objects.all()
        return render(
            request,
            "dashboard/lost.html",
            {"provinces": provinces, "collines": collines, "communes": communes},
        )

    if request.method == "POST":
        card_id = request.POST["nid"]
        date = request.POST["date"]
        report = request.POST["report"]
        province = request.POST["province"]
        commune = request.POST["commune"]
        colline = request.POST["colline"]

        if LostIdCardReport.objects.filter(Q(card_id=card_id) | Q(date=date)).exists():
            messages.info(request, "Lost report already sent")

        else:
            lost = LostIdCardReport(
                card_id=card_id,
                date=date,
                report=report,
                province_id=province,
                commune_id=commune,
                colline_id=colline,
            )

            lost.save()
            messages.info(
                request,
                "Thank you for reporting the lost ID card, we'll be in touch soon",
            )

        return redirect("lost")
