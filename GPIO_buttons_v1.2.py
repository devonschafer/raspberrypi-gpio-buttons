from guizero import App, Text, PushButton, Waffle
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
app = App(title="GPIO Buttons! v1.2", width=1300, height=150, layout="grid")

GPIO.setup(8, GPIO.HIGH)
GPIO.setup(8, GPIO.LOW)
GPIO.setup(10, GPIO.HIGH)
GPIO.setup(10, GPIO.LOW)
GPIO.setup(12, GPIO.HIGH)
GPIO.setup(12, GPIO.LOW)
GPIO.setup(16, GPIO.HIGH)
GPIO.setup(16, GPIO.LOW)
GPIO.setup(18, GPIO.HIGH)
GPIO.setup(18, GPIO.LOW)
GPIO.setup(22, GPIO.HIGH)
GPIO.setup(22, GPIO.LOW)
GPIO.setup(24, GPIO.HIGH)
GPIO.setup(24, GPIO.LOW)
GPIO.setup(26, GPIO.HIGH)
GPIO.setup(26, GPIO.LOW)
GPIO.setup(32, GPIO.HIGH)
GPIO.setup(32, GPIO.LOW)
GPIO.setup(36, GPIO.HIGH)
GPIO.setup(36, GPIO.LOW)
GPIO.setup(38, GPIO.HIGH)
GPIO.setup(38, GPIO.LOW)
GPIO.setup(40, GPIO.HIGH)
GPIO.setup(40, GPIO.LOW)
GPIO.setup(3, GPIO.HIGH)
GPIO.setup(3, GPIO.LOW)
GPIO.setup(5, GPIO.HIGH)
GPIO.setup(5, GPIO.LOW)
GPIO.setup(7, GPIO.HIGH)
GPIO.setup(7, GPIO.LOW)
GPIO.setup(11, GPIO.HIGH)
GPIO.setup(11, GPIO.LOW)
GPIO.setup(13, GPIO.HIGH)
GPIO.setup(13, GPIO.LOW)
GPIO.setup(15, GPIO.HIGH)
GPIO.setup(15, GPIO.LOW)
GPIO.setup(19, GPIO.HIGH)
GPIO.setup(19, GPIO.LOW)
GPIO.setup(21, GPIO.HIGH)
GPIO.setup(21, GPIO.LOW)
GPIO.setup(23, GPIO.HIGH)
GPIO.setup(23, GPIO.LOW)
GPIO.setup(29, GPIO.HIGH)
GPIO.setup(29, GPIO.LOW)
GPIO.setup(31, GPIO.HIGH)
GPIO.setup(31, GPIO.LOW)
GPIO.setup(33, GPIO.HIGH)
GPIO.setup(33, GPIO.LOW)
GPIO.setup(35, GPIO.HIGH)
GPIO.setup(35, GPIO.LOW)
GPIO.setup(37, GPIO.HIGH)
GPIO.setup(37, GPIO.LOW)

def gpio_8():
    if GPIO.input(8):
        GPIO.output(8, GPIO.LOW)
        button1.text = "8 ON"
        visual_1.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(8, GPIO.HIGH)
        button1.text = "8 OFF"
        visual_1.set_pixel(0, 0, 'green')

button1 = PushButton(app, text='8 ON', command=gpio_8, grid=[0, 0], align='left')
visual_1 = Waffle(app, height=1, width=1, color='grey', grid=[1,0], align='left', pad=1, dim=20)

def gpio_10():
    if GPIO.input(10):
        GPIO.output(10, GPIO.LOW)
        button2.text = "10 ON"
        visual_2.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(10, GPIO.HIGH)
        button2.text = "10 OFF"
        visual_2.set_pixel(0, 0, 'green')


button2 = PushButton(app, text='10 ON', command=gpio_10, grid=[2, 0], align='left')
visual_2 = Waffle(app, height=1, width=1, color='grey', grid=[3,0], align='left', pad=1, dim=20)

def gpio_12():
    if GPIO.input(12):
        GPIO.output(12, GPIO.LOW)
        button3.text = "12 ON"
        visual_3.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(12, GPIO.HIGH)
        button3.text = "12 OFF"
        visual_3.set_pixel(0, 0, 'green')
        
button3 = PushButton(app, text='12 ON', command=gpio_12, grid=[4, 0], align='left')
visual_3 = Waffle(app, height=1, width=1, color='grey', grid=[5,0], align='left', pad=1, dim=20)

def gpio_16():
    if GPIO.input(16):
        GPIO.output(16, GPIO.LOW)
        button4.text = "16 ON"
        visual_4.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(16, GPIO.HIGH)
        button4.text = "16 OFF"
        visual_4.set_pixel(0, 0, 'green')

button4 = PushButton(app, text='16 ON', command=gpio_16, grid=[6, 0], align='left')
visual_4 = Waffle(app, height=1, width=1, color='grey', grid=[7,0], align='left', pad=1, dim=20)

def gpio_18():
    if GPIO.input(18):
        GPIO.output(18, GPIO.LOW)
        button5.text = "18 ON"
        visual_5.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(18, GPIO.HIGH)
        button5.text = "18 OFF"
        visual_5.set_pixel(0, 0, 'green')

button5 = PushButton(app, text='18 ON', command=gpio_18, grid=[8, 0], align='left')
visual_5 = Waffle(app, height=1, width=1, color='grey', grid=[9,0], align='left', pad=1, dim=20)

def gpio_22():
    if GPIO.input(22):
        GPIO.output(22, GPIO.LOW)
        button6.text = "22 ON"
        visual_6.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(22, GPIO.HIGH)
        button6.text = "22 OFF"
        visual_6.set_pixel(0, 0, 'green')

button6 = PushButton(app, text='22 ON', command=gpio_22, grid=[10, 0], align='left')
visual_6 = Waffle(app, height=1, width=1, color='grey', grid=[11,0], align='left', pad=1, dim=20)

def gpio_24():
    if GPIO.input(24):
        GPIO.output(24, GPIO.LOW)
        button7.text = "24 ON"
        visual_7.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(24, GPIO.HIGH)
        button7.text = "24 OFF"
        visual_7.set_pixel(0, 0, 'green')

button7 = PushButton(app, text='24 ON', command=gpio_24, grid=[12, 0], align='left')
visual_7 = Waffle(app, height=1, width=1, color='grey', grid=[13,0], align='left', pad=1, dim=20)

def gpio_26():
    if GPIO.input(26):
        GPIO.output(26, GPIO.LOW)
        button8.text = "26 ON"
        visual_8.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(26, GPIO.HIGH)
        button8.text = "26 OFF"
        visual_8.set_pixel(0, 0, 'green')

button8 = PushButton(app, text='26 ON', command=gpio_26, grid=[14, 0], align='left')
visual_8 = Waffle(app, height=1, width=1, color='grey', grid=[15,0], align='left', pad=1, dim=20)

def gpio_32():
    if GPIO.input(32):
        GPIO.output(32, GPIO.LOW)
        button9.text = "32 ON"
        visual_9.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(32, GPIO.HIGH)
        button9.text = "32 OFF"
        visual_9.set_pixel(0, 0, 'green')

button9 = PushButton(app, text='32 ON', command=gpio_32, grid=[16, 0], align='left')
visual_9 = Waffle(app, height=1, width=1, color='grey', grid=[17,0], align='left', pad=1, dim=20)

def gpio_36():
    if GPIO.input(36):
        GPIO.output(36, GPIO.LOW)
        button10.text = "36 ON"
        visual_10.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(36, GPIO.HIGH)
        button10.text = "36 OFF"
        visual_10.set_pixel(0, 0, 'green')

button10 = PushButton(app, text='36 ON', command=gpio_36, grid=[18, 0], align='left')
visual_10 = Waffle(app, height=1, width=1, color='grey', grid=[19,0], align='left', pad=1, dim=20)

def gpio_38():
    if GPIO.input(38):
        GPIO.output(38, GPIO.LOW)
        button11.text = "38 ON"
        visual_11.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(38, GPIO.HIGH)
        button11.text = "38 OFF"
        visual_11.set_pixel(0, 0, 'green')

button11 = PushButton(app, text='38 ON', command=gpio_38, grid=[20, 0], align='left')
visual_11 = Waffle(app, height=1, width=1, color='grey', grid=[21,0], align='left', pad=1, dim=20)


def gpio_40():
    if GPIO.input(40):
        GPIO.output(40, GPIO.LOW)
        button12.text = "40 ON"
        visual_12.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(40, GPIO.HIGH)
        button12.text = "40 OFF"
        visual_12.set_pixel(0, 0, 'green')

button12 = PushButton(app, text='40 ON', command=gpio_40, grid=[22, 0], align='left')
visual_12 = Waffle(app, height=1, width=1, color='grey', grid=[23,0], align='left', pad=1, dim=20)

def gpio_3():
    if GPIO.input(3):
        GPIO.output(3, GPIO.LOW)
        button13.text = "3 ON"
        visual_13.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(3, GPIO.HIGH)
        button13.text = "3 OFF"
        visual_13.set_pixel(0, 0, 'green')

button13 = PushButton(app, text='3 ON', command=gpio_3, grid=[0, 1], align='left')
visual_13 = Waffle(app, height=1, width=1, color='grey', grid=[1,1], align='left', pad=1, dim=20)

def gpio_5():
    if GPIO.input(5):
        GPIO.output(5, GPIO.LOW)
        button14.text = "5 ON"
        visual_14.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(5, GPIO.HIGH)
        button14.text = "5 OFF"
        visual_14.set_pixel(0, 0, 'green')

button14 = PushButton(app, text='5 ON', command=gpio_5, grid=[2, 1], align='left')
visual_14 = Waffle(app, height=1, width=1, color='grey', grid=[3,1], align='left', pad=1, dim=20)

def gpio_7():
    if GPIO.input(7):
        GPIO.output(7, GPIO.LOW)
        button15.text = "7 ON"
        visual_15.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(7, GPIO.HIGH)
        button15.text = "7 OFF"
        visual_15.set_pixel(0, 0, 'green')

button15 = PushButton(app, text='7 ON', command=gpio_7, grid=[4, 1], align='left')
visual_15 = Waffle(app, height=1, width=1, color='grey', grid=[5,1], align='left', pad=1, dim=20)

def gpio_11():
    if GPIO.input(11):
        GPIO.output(11, GPIO.LOW)
        button16.text = "11 ON"
        visual_16.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(11, GPIO.HIGH)
        button16.text = "11 OFF"
        visual_16.set_pixel(0, 0, 'green')

button16 = PushButton(app, text='11 ON', command=gpio_11, grid=[6, 1], align='left')
visual_16 = Waffle(app, height=1, width=1, color='grey', grid=[7,1], align='left', pad=1, dim=20)

def gpio_13():
    if GPIO.input(13):
        GPIO.output(13, GPIO.LOW)
        button17.text = "13 ON"
        visual_17.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(13, GPIO.HIGH)
        button17.text = "13 OFF"
        visual_17.set_pixel(0, 0, 'green')

button17 = PushButton(app, text='13 ON', command=gpio_13, grid=[8, 1], align='left')
visual_17 = Waffle(app, height=1, width=1, color='grey', grid=[9,1], align='left', pad=1, dim=20)

def gpio_15():
    if GPIO.input(15):
        GPIO.output(15, GPIO.LOW)
        button18.text = "15 ON"
        visual_18.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(15, GPIO.HIGH)
        button18.text = "15 OFF"
        visual_18.set_pixel(0, 0, 'green')

button18 = PushButton(app, text='15 ON', command=gpio_15, grid=[10, 1], align='left')
visual_18 = Waffle(app, height=1, width=1, color='grey', grid=[11,1], align='left', pad=1, dim=20)

def gpio_19():
    if GPIO.input(19):
        GPIO.output(19, GPIO.LOW)
        button19.text = "19 ON"
        visual_19.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(19, GPIO.HIGH)
        button19.text = "19 OFF"
        visual_19.set_pixel(0, 0, 'green')

button19 = PushButton(app, text='19 ON', command=gpio_19, grid=[12, 1], align='left')
visual_19 = Waffle(app, height=1, width=1, color='grey', grid=[13,1], align='left', pad=1, dim=20)

def gpio_21():
    if GPIO.input(21):
        GPIO.output(21, GPIO.LOW)
        button20.text = "21 ON"
        visual_20.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(21, GPIO.HIGH)
        button20.text = "21 OFF"
        visual_20.set_pixel(0, 0, 'green')

button20 = PushButton(app, text='21 ON', command=gpio_21, grid=[14, 1], align='left')
visual_20 = Waffle(app, height=1, width=1, color='grey', grid=[15,1], align='left', pad=1, dim=20)

def gpio_23():
    if GPIO.input(23):
        GPIO.output(23, GPIO.LOW)
        button21.text = "23 ON"
        visual_21.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(23, GPIO.HIGH)
        button21.text = "23 OFF"
        visual_21.set_pixel(0, 0, 'green')

button21 = PushButton(app, text='23 ON', command=gpio_23, grid=[16, 1], align='left')
visual_21 = Waffle(app, height=1, width=1, color='grey', grid=[17,1], align='left', pad=1, dim=20)

def gpio_29():
    if GPIO.input(29):
        GPIO.output(29, GPIO.LOW)
        button22.text = "29 ON"
        visual_22.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(29, GPIO.HIGH)
        button22.text = "29 OFF"
        visual_22.set_pixel(0, 0, 'green')

button22 = PushButton(app, text='29 ON', command=gpio_29, grid=[18, 1], align='left')
visual_22 = Waffle(app, height=1, width=1, color='grey', grid=[19,1], align='left', pad=1, dim=20)

def gpio_31():
    if GPIO.input(31):
        GPIO.output(31, GPIO.LOW)
        button23.text = "31 ON"
        visual_23.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(31, GPIO.HIGH)
        button23.text = "31 OFF"
        visual_23.set_pixel(0, 0, 'green')

button23 = PushButton(app, text='31 ON', command=gpio_31, grid=[20, 1], align='left')
visual_23 = Waffle(app, height=1, width=1, color='grey', grid=[21,1], align='left', pad=1, dim=20)

def gpio_33():
    if GPIO.input(33):
        GPIO.output(33, GPIO.LOW)
        button24.text = "33 ON"
        visual_24.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(33, GPIO.HIGH)
        button24.text = "33 OFF"
        visual_24.set_pixel(0, 0, 'green')

button24 = PushButton(app, text='33 ON', command=gpio_33, grid=[22, 1], align='left')
visual_24 = Waffle(app, height=1, width=1, color='grey', grid=[23,1], align='left', pad=1, dim=20)

def gpio_35():
    if GPIO.input(35):
        GPIO.output(35, GPIO.LOW)
        button25.text = "35 ON"
        visual_25.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(35, GPIO.HIGH)
        button25.text = "35 OFF"
        visual_25.set_pixel(0, 0, 'green')

button25 = PushButton(app, text='35 ON', command=gpio_35, grid=[24, 1], align='left')
visual_25 = Waffle(app, height=1, width=1, color='grey', grid=[25,1], align='left', pad=1, dim=20)

def gpio_37():
    if GPIO.input(37):
        GPIO.output(37, GPIO.LOW)
        button26.text = "37 ON"
        visual_26.set_pixel(0, 0, 'grey')
    else:
        GPIO.output(37, GPIO.HIGH)
        button26.text = "37 OFF"
        visual_26.set_pixel(0, 0, 'green')

button26 = PushButton(app, text='37 ON', command=gpio_37, grid=[26, 1], align='left')
visual_26 = Waffle(app, height=1, width=1, color='grey', grid=[27,1], align='left', pad=1, dim=20)

app.display()
