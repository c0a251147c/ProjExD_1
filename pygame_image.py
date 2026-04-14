import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flipped = pg.transform.flip(bg_img, True, False)

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200  

    bg_x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key = pg.key.get_pressed()
        
        vx, vy = -1, 0

        if key[pg.K_RIGHT]:
            vx += 2
        if key[pg.K_LEFT]:
            vx -= 2
        if key[pg.K_UP]:
            vy -= 2
        if key[pg.K_DOWN]:
            vy += 2

        kk_rct.move_ip(vx, vy)
        
        bg_x -= 1
        if bg_x <= -1600:
            bg_x = 0

        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_img_flipped, [bg_x + 800, 0])
        screen.blit(bg_img, [bg_x + 1600, 0])

        screen.blit(kk_img, kk_rct)

        
        pg.display.update()
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
