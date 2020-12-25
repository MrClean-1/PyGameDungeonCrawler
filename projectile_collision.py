def collision(bullets_one, bullets_two):
    for bullet_one in bullets_one:
        for bullet_two in bullets_two:
            if bullet_one.rect.colliderect(bullet_two.rect):
                bullets_one.remove(bullet_one)
                bullets_two.remove(bullet_two)
