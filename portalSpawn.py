import random
from portal import Portal


def portal_spawn(portals):
    if random.randint(0, 1) == 1:
        portal = Portal("up")
        portal.goto(1)
        portals.append(portal)

    if random.randint(0, 1) == 1:
        portal = Portal("right")
        portal.goto(2)
        portals.append(portal)

    if random.randint(0, 1) == 1:
        portal = Portal("down")
        portal.goto(3)
        portals.append(portal)

    if random.randint(0, 1) == 1:
        portal = Portal("left")
        portal.goto(4)
        portals.append(portal)

    if len(portals) == 0:
        wall = random.randint(1,4)
        if wall == 1:
            portal = Portal("up")
            portal.goto(1)
            portals.append(portal)
        if wall == 2:
            portal = Portal("right")
            portal.goto(2)
            portals.append(portal)
        if wall == 3:
            portal = Portal("down")
            portal.goto(3)
            portals.append(portal)
        if wall == 4:
            portal = Portal("left")
            portal.goto(4)
            portals.append(portal)
