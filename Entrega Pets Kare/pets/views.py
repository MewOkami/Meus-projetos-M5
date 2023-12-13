from rest_framework.views import Request, Response, APIView, status
from .models import Pet
from .serializers import PetsSerializer
from groups.models import Group
from traits.models import Trait
from rest_framework.pagination import PageNumberPagination


class PetView(APIView, PageNumberPagination):
    def post(self, req: Request) -> Response:

        serializer = PetsSerializer(data=req.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        group_data = serializer.validated_data.pop("group")
        traits_data = serializer.validated_data.pop("traits")

        try:
            group = Group.objects.get(
                scientific_name=group_data["scientific_name"])
        except Group.DoesNotExist:
            group = Group.objects.create(**group_data)

        pet = Pet.objects.create(**serializer.validated_data, group=group)
        for trait_data in traits_data:
            trait_name = trait_data["name"].casefold()
            try:
                trait = Trait.objects.get(name__iexact=trait_name)
            except Trait.DoesNotExist:
                trait = Trait.objects.create(**trait_data)

            pet.traits.add(trait)

        serializer = PetsSerializer(pet)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        by_trait = req.query_params.get("trait", None)
        if by_trait:
            pets = Pet.objects.filter(traits__name__icontains=by_trait)
        else:
            pets = Pet.objects.all()
        result = self.paginate_queryset(pets, req)
        serializer = PetsSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)


class PetDetailView(APIView, PageNumberPagination):
    def get(self, req: Request, pet_id: int) -> Response:
        # ipdb.set_trace()
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response(
                {"detail": "Not found."},
                status.HTTP_404_NOT_FOUND,
            )

        serializer = PetsSerializer(found_pet)
        return Response(serializer.data)

    def delete(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response(
                {"detail": "Not found."},
                status.HTTP_404_NOT_FOUND,
            )
        found_pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, req: Request, pet_id: int) -> Response:
        try:
            found_pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response(
                {"detail": "Not found."},
                status.HTTP_404_NOT_FOUND,
            )

        serializer = PetsSerializer(data=req.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        group_data = serializer.validated_data.pop("group", None)
        trait_data = serializer.validated_data.pop("traits", None)

        for key, value in serializer.validated_data.items():
            setattr(found_pet, key, value)

        if group_data:
            try:
                group = Group.objects.get(
                    scientific_name=group_data["scientific_name"])

                found_pet.group = group
            except Group.DoesNotExist:
                group = Group.objects.create(**group_data)
                found_pet.group = group

        if trait_data:
            found_pet.traits.clear()
            trait_list = []
            for trait in trait_data:
                trait_name = trait["name"].casefold()
                try:
                    traits = Trait.objects.get(
                        name__iexact=trait_name)
                except Trait.DoesNotExist:
                    traits = Trait.objects.create(**trait)
                trait_list.append(traits)
            found_pet.traits.set(trait_list)

        found_pet.save()
        serializer = PetsSerializer(found_pet)

        return Response(serializer.data, status.HTTP_200_OK)
