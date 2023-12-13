from rest_framework.views import APIView, status, Request, Response
from .models import Team
from django.forms import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError


class TeamView(APIView):
    def post(self, req: Request) -> Response:
        team = Team(**req.data)

        try:
            data_processing(req.data)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"error": err.message}, status.HTTP_400_BAD_REQUEST)

        team.save()

        converted_team = model_to_dict(team)
        return Response(converted_team, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        teams = Team.objects.all()
        converted_teams = []

        for team in teams:
            converted_team = model_to_dict(team)
            converted_teams.append(converted_team)

        return Response(converted_teams, status.HTTP_200_OK)


class TeamDetailView(APIView):
    def get(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        converted_team = model_to_dict(found_team)
        return Response(converted_team)

    def delete(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        found_team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, team_id: int) -> Response:
        try:
            found_team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for k, v in req.data.items():
            setattr(found_team, k, v)

        found_team.save()
        convert_team = model_to_dict(found_team)
        return Response(convert_team)
