from portalSpawn import portal_spawn
from portal import Portal
import random
from skullclass import SkullBadGuy
from ogreclass import OgreBadGuy


def portal_collision(player, shots, portal, portals, bones, skeletons, hearts, ogres):
    if player.collision(portal):
        collide = True
        if portal.wall == "up":
            portals.remove(portal)
            player.rect.y = 350
            player.rect.x = 382.5
            portals.clear()
            shots.clear()
            portal_spawn(portals)
            portal = Portal("down")
            portal.goto(3)
            portals.append(portal)
            collided = True
        elif portal.wall == "down":
            portals.remove(portal)
            player.rect.y = 110
            player.rect.x = 382.5
            portals.clear()
            shots.clear()
            portal_spawn(portals)
            portal = Portal("up")
            portal.goto(1)
            portals.append(portal)
            collided = True
        elif portal.wall == "left":
            portals.remove(portal)
            player.rect.x = 120
            player.rect.y = 227
            portals.clear()
            shots.clear()
            portal_spawn(portals)
            portal = Portal("right")
            portal.goto(2)
            portals.append(portal)
            collided = True
        elif portal.wall == "right":
            portals.remove(portal)
            player.rect.x = 650
            player.rect.y = 227
            portal_spawn(portals)
            portal = Portal("left")
            portal.goto(4)
            portals.append(portal)
            collided = True
        else:
            collided = False
        if collided:
            shots.clear()
            bones.clear()
            hearts.clear()

            loops = random.randint(1, 3)
            for i in range(loops):
                skeleton = SkullBadGuy()
                skeletons.append(skeleton)

            loops = random.randint(1, 2)
            for i in range(loops):
                ogre = OgreBadGuy()
                ogres.append(ogre)

        if collide:
            return True
        else:
            return False
