from dataclasses import fields
import graphene
from graphene_django import DjangoObjectType
from .models import Trip, Location


class TripType(DjangoObjectType):
    class Meta:
        model = Trip
        fields = '__all__'
        
        
class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        fields = '__all__'       


class Query(graphene.ObjectType):
    trips = graphene.List(TripType)
    locations = graphene.List(LocationType)
    
    def resolve_trips(root, info, **kwargs):
        return Trip.objects.all()
    
    def resolve_locations(root, info, **kwargs):
        return Location.objects.all()
    
    
class TripInput(graphene.InputObjectType):
    name= graphene.String()
    trip_from= graphene.Int()
    trip_to= graphene.Int()
    receiver= graphene.String()
    created_by= graphene.String()
    date_created= graphene.String()
    updated_at= graphene.String()
    
    
class LocationInput(graphene.InputObjectType):
    name= graphene.String()
    county = graphene.String()
    description = graphene.String()
    created_by= graphene.String()
    
    
class CreateTrips(graphene.Mutation):
    class Arguments:
        input = TripInput(required=True)

    
    trip = graphene.Field(TripType)
    
    @classmethod
    def mutate(cls, root, info, input):
        
        _from = Location.objects.get(pk=input.trip_from)
        _to = Location.objects.get(pk=input.trip_to)
        
        trip = Trip()
        trip.name = input.name 
        trip.trip_from = _from
        trip.trip_to = _to
        trip.receiver_id = input.receiver
        trip.created_by = input.created_by
        trip.date_created = input.date_created
        trip.updated_at = input.updated_at
        trip.save()
        
        return CreateTrips(trip=trip)
    
class CreateLocation(graphene.Mutation):
    class Arguments:
        input = LocationInput(required=True)
    
    location = graphene.Field(LocationType)
    
    @classmethod
    def mutate(cls, root, info, input):
        location = Location()
        location.name = input.name
        location.county = input.county
        location.description = input.description
        location.created_by = input.created_by
        location.save()
        
        return CreateLocation(location=location)
        
class Mutation(graphene.ObjectType):
    create_trip = CreateTrips.Field()
    create_location = CreateLocation.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)