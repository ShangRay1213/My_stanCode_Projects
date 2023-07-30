"""
File: 
Name:RAY
----------------------
櫻木花道
"""

from campy.graphics.gobjects import GOval, GLabel, GLine, GArc
from campy.graphics.gwindow import GWindow
window = GWindow(600, 600)


def main():
    """
    I went to watch The FIRST SLAM DUNK during Chinese New Year.
    I thought it was really great so I drew a Sakuragi Hanamichi
    """
    face_line = GLine(197, 180, 205, 300)
    face_line_2 = GLine(197, 180, 199, 160)
    face_ovel_left = GArc(150, 200, 186, 85, x=205, y=250)
    face_ovel_down = GArc(600, 600, 260, 50, x=145, y=270)
    face_ovel_right = GArc(250, 250, 280, 80, x=280, y=211)
    mouth_down = GArc(600, 3000, 250, 50, x=150, y=100)
    mouth_up = GArc(600, 3000, 60, 50, x=160, y=306)
    mouth_right = GArc(30, 40, 270, 200, x=340, y=280)
    mouth_left = GArc(20, 20, 110, 200, x=230, y=295)
    hair_down = GLine(200, 150, 210, 140)
    hair_down_2 = GLine(210, 140, 265, 143)
    hair_down_3 = GLine(265, 143, 264, 138)
    hair_down_4 = GLine(264, 138, 272, 144)
    hair_down_5 = GLine(272, 144, 280, 142)
    hair_down_6 = GLine(280, 142, 284, 143)
    hair_down_7 = GLine(284, 143, 288, 140)
    hair_down_8 = GLine(288, 140, 300, 142)
    hair_down_9 = GLine(300, 142, 325, 141)
    hair_down_10 = GLine(325, 141, 322, 137)
    hair_down_11 = GLine(322, 137, 349, 136)
    hair_down_12 = GLine(349, 136, 354, 170)
    hair_down_13 = GLine(354, 170, 369, 175)
    hair_down_14 = GLine(369, 175, 374, 200)
    hair_down_15 = GArc(400, 400, 360, 30, x=348, y=170)
    ear_1 = GLine(375, 215, 383, 221)
    ear_2 = GArc(30, 70, 340, 180, x=382, y=205)
    ear_3 = GArc(400, 400, 300, 45, x=318, y=162)
    hair_up = GLine(200, 150, 198, 130)
    hair_up_2 = GLine(198, 130, 200, 120)
    hair_big_1 = GArc(400, 400, 320, 50, x=370, y=80)
    hair_big_2 = GArc(400, 400, 5, 45, x=345, y=90)
    hair_big_3 = GArc(400, 400, 20, 50, x=287, y=70)
    hair_big_4 = GArc(500, 500, 170, -40, x=200, y=70)
    hair_big_5 = GArc(500, 500, 150, -40, x=206, y=63)
    hair_big_6 = GArc(500, 500, 140, -40, x=220, y=55)
    hair_big_7 = GArc(500, 500, 90, -70, x=180, y=55)
    r_eyebrow = GArc(1200, 1200, 210, 30, x=200, y=15)
    r_eye_up = GArc(150, 150, 220, 60, x=200, y=185)
    r_eye_down = GArc(250, 250, 220, 50, x=203, y=180)
    l_eyebrow = GArc(1200, 1200, 300, 30, x=120, y=15)
    l_eye_up = GArc(400, 400, 270, 40, x=230, y=165)
    l_eye_down = GArc(400, 400, 270, 40, x=230, y=175)
    omg_line_1 = GLine(255, 200, 255, 220)
    omg_line_2 = GLine(275, 210, 275, 220)
    omg_line_3 = GLine(280, 195, 280, 222)
    r_eye = GOval(3, 3, x=230, y=212)
    r_eye.filled = True
    l_eye = GOval(3, 3, x=310, y=212)
    l_eye.filled = True
    hair1 = GLabel(",  '  ,    ' ,        ,'     ',   ,       ,", x=220, y=130)
    hair2 = GLabel(",  '  ,  ' ", x=360, y=150)
    hair3 = GLabel(",  '  ,  ' ", x=360, y=170)
    hair4 = GLabel(",  '  ,  '   ,   ,  ,'    ',    ', ", x=220, y=110)
    face_shy = GLabel("//", x=210, y=250)
    face_shy2 = GLabel("//", x=330, y=250)
    nose = GLabel("、", x=250, y=270)
    l_hand = GArc(500, 500, 120, 50, x=175, y=275)
    l_hand2 = GLine(175, 345, 177, 440)
    t_shirt = GArc(800, 800, 0, -40, x=130, y=205)
    t_shirt2 = GArc(100, 200, 200, 150, x=240, y=285)
    t_shirt3 = GArc(600, 600, 165, 60, x=390, y=170)
    t_shirt4 = GArc(110, 210, 200, 150, x=235, y=285)
    t_shirt5 = GArc(800, 800, 0, -40, x=135, y=210)
    t_shirt6 = GArc(600, 600, 165, 60, x=385, y=170)
    r_hand = GArc(500, 500, 70, -50, x=295, y=265)
    r_hand2 = GLine(440, 315, 445, 365)
    r_hand3 = GLine(445, 365, 443, 405)
    angry1 = GArc(15, 15, 280, 170, x=295, y=150)
    angry2 = GArc(10, 10, 20, 170, x=307, y=163)
    angry3 = GArc(13, 13, 140, 170, x=311, y=145)
    water = GArc(8, 40, 180, 180, x=220, y=260)
    water2 = GArc(8, 40, 180, 180, x=250, y=140)
    water3 = GArc(8, 40, 180, 180, x=345, y=250)
    water4 = GArc(8, 40, 180, 180, x=180, y=340)
    water5 = GArc(8, 40, 180, 180, x=405, y=320)
    water6 = GArc(4, 30, 180, 180, x=425, y=370)
    water7 = GArc(4, 30, 180, 180, x=295, y=340)
    title = GLabel("SHOHOKU", x=245, y=405)
    title.font = "Courier-30"
    word = GLabel("...天才 !!!", x=230, y=500)
    word.font = "-70"
    window.add(word)
    window.add(water7)
    window.add(water6)
    window.add(water5)
    window.add(water4)
    window.add(water3)
    window.add(t_shirt6)
    window.add(t_shirt5)
    window.add(t_shirt4)
    window.add(title)
    window.add(water2)
    window.add(water)
    window.add(angry3)
    window.add(angry2)
    window.add(angry1)
    window.add(t_shirt3)
    window.add(r_hand3)
    window.add(r_hand2)
    window.add(r_hand)
    window.add(t_shirt2)
    window.add(t_shirt)
    window.add(l_hand2)
    window.add(l_hand)
    window.add(nose)
    window.add(face_shy2)
    window.add(face_shy)
    window.add(hair4)
    window.add(hair3)
    window.add(hair2)
    window.add(hair1)
    window.add(hair_big_7)
    window.add(hair_big_6)
    window.add(hair_big_5)
    window.add(hair_big_4)
    window.add(hair_big_3)
    window.add(hair_big_2)
    window.add(r_eye)
    window.add(l_eye)
    window.add(omg_line_3)
    window.add(omg_line_2)
    window.add(omg_line_1)
    window.add(l_eye_down)
    window.add(l_eye_up)
    window.add(l_eyebrow)
    window.add(r_eye_down)
    window.add(r_eye_up)
    window.add(r_eyebrow)
    window.add(hair_big_1)
    window.add(hair_up_2)
    window.add(hair_up)
    window.add(face_line_2)
    window.add(ear_3)
    window.add(ear_2)
    window.add(ear_1)
    window.add(hair_down_15)
    window.add(hair_down_14)
    window.add(hair_down_13)
    window.add(hair_down_12)
    window.add(hair_down_11)
    window.add(hair_down_10)
    window.add(hair_down_9)
    window.add(face_line)
    window.add(face_ovel_left)
    window.add(face_ovel_down)
    window.add(face_ovel_right)
    window.add(mouth_down)
    window.add(mouth_up)
    window.add(mouth_right)
    window.add(mouth_left)
    window.add(hair_down)
    window.add(hair_down_2)
    window.add(hair_down_3)
    window.add(hair_down_4)
    window.add(hair_down_5)
    window.add(hair_down_6)
    window.add(hair_down_7)
    window.add(hair_down_8)


if __name__ == '__main__':
    main()