#coding

### Final result
---
To get to the point, here's the final result. I think it looks pretty nice, but if you don't, of course, you can play around to make it your own. 

Oh, and you don't need a M2 chip for this, **any M series Mac will work fine.**

![[Pasted image 20231115233056.png]]
![[Pasted image 20231115233704.png]]

### Installing UTM
---
To get started, you'll need UTM. You can use other VM software, but I'll be using UTM here, and you may run into some issues if you don't. 

UTM is available for free on [their website](https://mac.getutm.app). Download the DMG, drag it to Applications, I'm sure you know the gist of it.

![[Pasted image 20231115234833.png]]


### Downloading the ISO
---
>[!info] This install will be using 'Arch Linux ARM', for the best performance. While *technically* Arch Linux, it is a sister project. So keep that in mind when asking around on forums, if you require any help.

First, we'll grab our ISO from Archboot. Go to [their website](https://archboot.com), and scroll down to the ISOs section. We'll grab the 'aarch64' version.

![[Pasted image 20231115235610.png]]

Next, go to the 'latest' folder, to grab the most recent one.
![[Pasted image 20231115235641.png]]

Finally, download this ISO. 
![[Pasted image 20231115235744.png]]


### Configuring UTM
---
When you launch UTM, you're going to want to make a virtual machine. When you get to this prompt, select 'Virtualize', then Linux for the OS.

![[Pasted image 20231116000725.png]]


Skip all the checkboxes, hit browse, and select your Archboot ISO. 

![[Pasted image 20231116000953.png]]
