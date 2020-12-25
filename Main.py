def main():
    import pygame
    from data import mageclass
    from data.transition import Transition
    from data.skullclass import SkullBadGuy
    from data.ogreclass import OgreBadGuy
    from data.projectiles import Projectile
    from data.portalSpawn import portal_spawn
    from data.portalCollision import portal_collision
    from data.projectile_collision import collision
    from data.heart import Heart
    from data.score import Score

    pygame.init()
    screen = pygame.display.set_mode((836, 525))
    background = pygame.image.load('data/background.png')
    background_size = screen.get_rect()

    done = False
    shots = []
    portals = []
    skeletons = []
    bones = []
    hearts = []
    ogres = []
    shot_cooldown = 0
    player = mageclass.Player()
    clock = pygame.time.Clock()

    for i in range(1):
        skeleton = SkullBadGuy()
        skeletons.append(skeleton)
        bones = skeleton.bone_throw()

    for i in range(0):
        ogre = OgreBadGuy()
        ogres.append(ogre)

    score = Score(screen)

    portal_spawn(portals)

    while not done:
        x = 0
        y = 0

        events = pygame.event.get()
        pos = (player.rect.x, player.rect.y)
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    if shot_cooldown == 0:
                        shot = Projectile('data/shot.png', "right")
                        shot.goto((pos[0] + 23), (pos[1] + 25))
                        shots.append(shot)
                        shot_cooldown = 15
                        player.animation("right", False)

                if event.key == pygame.K_LEFT:
                    if shot_cooldown == 0:
                        shot = Projectile('data/shot.png', "left")
                        shot.goto((pos[0] + 23), (pos[1] + 25))
                        shots.append(shot)
                        shot_cooldown = 15
                        player.animation("left", False)

                if event.key == pygame.K_UP:
                    if shot_cooldown == 0:
                        shot = Projectile('data/shot.png', "down")
                        shot.goto((pos[0] + 23), (pos[1] + 25))
                        shots.append(shot)
                        shot_cooldown = 15
                        player.animation("up", False)

                if event.key == pygame.K_DOWN:
                    if shot_cooldown == 0:
                        shot = Projectile('data/shot.png', "up")
                        shot.goto((pos[0] + 23), (pos[1] + 25))
                        shots.append(shot)
                        shot_cooldown = 15
                        player.animation("down", False)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.animation("up", False)
                if event.key == pygame.K_a:
                    player.animation("left", False)
                if event.key == pygame.K_s:
                    player.animation("down", False)
                if event.key == pygame.K_d:
                    player.animation("right", False)

        key_presses = pygame.key.get_pressed()

        if key_presses[pygame.K_w]:
            if pos[1] > 55:
                y -= 4
                player.animation("up", True)
        if key_presses[pygame.K_a]:
            if pos[0] > 70:
                x -= 4
                player.animation("left", True)
        if key_presses[pygame.K_s]:
            if pos[1] < 384:
                y += 4
                player.animation("down", True)
        if key_presses[pygame.K_d]:
            if pos[0] < 710:
                x += 4
                player.animation("right", True)

        screen.blit(background, background_size)

        if not skeletons and not ogres:
            for portal in portals:
                screen.blit(portal.image, portal.rect)
                transition = portal_collision(player, shots, portal, portals, bones, skeletons, hearts, ogres)
                if transition:
                    screen_transition = Transition()
                    score.points("room clear")
                    for i in range(10):
                        screen_transition.update(i)
                        screen.blit(screen_transition.image, screen_transition.rect)
                        pygame.display.flip()
                        clock.tick(30)

        running = player.update(x, y)

        for heart in hearts:
            screen.blit(heart.image, heart.rect)
            if heart.collision(player.rect):
                player.health += 1
                hearts.remove(heart)

        screen.blit(player.image, player.rect)
        collision(bones, shots)

        for skeleton in skeletons:
            alive = skeleton.collision(shots)
            if alive[0]:
                skeleton.update(player.rect.x, player.rect.y, bones)
                screen.blit(skeleton.image, skeleton.rect)
                bones = skeleton.bone_throw()
            else:
                if alive[1]:
                    heart = Heart()
                    heart.goto(skeleton.rect.x, skeleton.rect.y)
                    hearts.append(heart)
                skeletons.remove(skeleton)
                score.points("skeleton death")

        for ogre in ogres:
            alive = ogre.collision(shots)
            if alive[0]:
                ogre.update(player.rect.x, player.rect.y)
                screen.blit(ogre.image, ogre.rect)
                ogre.dash()
                player.enemy_collision(ogre.rect)
            else:
                if alive[1]:
                    heart = Heart()
                    heart.goto(ogre.rect.x, ogre.rect.y)
                    hearts.append(heart)
                ogres.remove(ogre)
                score.points("ogre death")

        for shot in shots:
            shot_alive = shot.update(12)
            if shot_alive:
                screen.blit(shot.image, shot.rect)
            else:
                shots.remove(shot)

        for bone in bones:
            bone_alive = bone.update(6)
            if bone_alive:
                bone.animation(4)
                screen.blit(bone.image, bone.rect)
                player.bone_collision(bone.rect, bones)
            else:
                bones.remove(bone)

        for lives in range(player.health):
            heart = player.lives(lives)
            screen.blit(heart[0], heart[1])

        if shot_cooldown != 0:
            shot_cooldown -= 1

        # Draws the score at the top of the screen by calling on a function in score class
        score.blit()

        # Flips display and sets frame-rate
        pygame.display.flip()
        clock.tick(30)

        # This is the game end screen
        while not running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = True
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main()
                    if event.key == pygame.K_ESCAPE:
                        running = True
                        done = True

            # Draws the score and highscore
            score.end_blit()
            pygame.display.flip()
            clock.tick(30)


main()
