# Ad Skipping bot
## Overview of the app
There is an app in the Playstore, Bfast Bfree and Efast Efree, where one can earn bitcoin and etherum respectively. But the problem is it isn't bearable. 
 - Watch ad for 30 secs, then a cross mark appears. 
 - Press it then it will load the loading screen. 
 - Roll the dice and you get some random points. 
 - Around 1.5 minutes of active viewing just for one roll. 
 - One can earn only about 1500 points per hour. If done continuously, in 15 minute you have to wait for an hour.
 - You can withdraw fund once every 3 days. 
 - 10000 points is around NPR 10 or less than 10 cents. 
  This is shit. Not good for anyone.<br>
## Conditions
My conditions were dire. I needed pocket money anyhow. If only my laptop would do tasks for me while i am asleep.
- Created 3 coinabse accounts.
- Installed emulator on PC and downloaded multi instance manager inside the emulator. This is so that 3 coinbase accounts X 2 Apps = 6 earning source.
- Created this bot

## Working
Its very simple. No out of the box technique. No AI involved.
- Once the dice rolls, wait for 15 secs. During that time no closing button appears so its useless to keep looking.
- The looking function just searches for pixels at specific location. The ai helper is used to create script to check certain locations
- After clicking the close button, wait few seconds and see if the main menu appears. 
- If menu appears do again. But sometimes the limit dialog box appears. In such case, close the app, open another app, then continue doing.
- Circle around for all 6 apps.
- Sometimes the bot doesn't recognize the cross button of the ad. For such conditions, set timer on each dice roll. If after 120 secs of rolling dice, main menu doesn't appear again, go breserk and restart the app.

## Ai helper
Take screenshot of the screen while cross appears. Open the SS on full screen. Run it.
- Place the mouse cursor on various locations inside the close button and press [Shift] for storing the location.
- Place the mouse cursor on the location where bot has to click when above pixels are detected and press [Alt]
- Press [Space Bar] to get the script. Copy it and place it in the central logic

## Earning
I used this bot for about a month and then got fet up. I left it to work at nights. From 11pm to about 7am. When new ads were added, bot would go breserk and restart app many times without result. Sometimes the multi instance app gave ad that caused dead end. Still managed to earn few bucks.  
After a month of use the three accounts had about $1.5, $0.9, $1 worth of bitcoins and etherum. Note that it was around 2021. I don't know the exact amount of coins and can't check either because shitty coinbase wants my passport now. Which I haven't made.

## Advice
Don't do this shit. Its output is very low. And gives ur PC alot of burden to run emulator.  
Still wanna try? Go ahead. **Burn the world.**
