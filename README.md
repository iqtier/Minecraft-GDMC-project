# Minecraft-GDMC-project
Minecraft Generative Design Project==> GDMC Competition 

## Project Setup / Installation:

There are instructions below for how to get this up and running. Before running the script ensure that the chunks that are in your build area are loaded. Otherwise, the parser won't recognize the NBT and you'll have to try again.

open terminal inside the same folder where all of our codes are, run the command 

```python -m pip install -r requirements.txt``` 

that will install all the library we used in our code. 

Before run the script You need to have Minecraft java edition: version -->> 1.16.5  , along with that you need to install forge mod: version -->> 36.2.29 and GDMC HTTP interface mod: version -->> 0.3.1.jar. 

While your Minecraft running, and already created a minecraft new world, you can set your build area either from the code or or from the game itself. command from inside the game is ```/setbuildarea fromX Y fromZ toX Y toZ```  , you can choose any posetive number for fromX , Y and FromZ, and add whatever your build area length and width with them and that will be your toX and toZ, you can use any Y value, 
for example ```/setbuildarea 100 20 100 350 20 350```  means my build area starting from x =100  and z =100 coordinate and my build area size is 250 by 250.
 
Once the build area is set and your location in the game is around the build area, form your terminal run the command 

```python Build_Settlement.py```  

then you can see the settelement is getting build inside the build area.

* Project Demo: https://www.youtube.com/watch?v=04U_dVQ5OBc&t=157s&ab_channel=IqtierUddinAhammad
* Project Trailer: https://www.youtube.com/watch?v=Zp_mu0TJNpQ
