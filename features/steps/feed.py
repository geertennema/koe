from behave import given, when, then 
from koe import Cow, Feed

@given(u'the cow weighs {weight:d} kg')
def test_weight(context, weight ):
    context.weight = weight

@given(u'the cow is {age:d} years old')
def test_age(context, age ):
    context.cow = Cow(context.weight, age)
    assert context.cow.age == age

@when(u'we calculate the feeding requirements')
def feed(context):
    context.feed = Feed(context.cow)

@then(u'the energy should be {energy:d} MJ')
def test_energy(context, energy):
    assert context.feed.energy == energy


@then(u'the protein should be {protein:d} kg')
def test_protein(context, protein):
    assert context.feed.protein == protein


