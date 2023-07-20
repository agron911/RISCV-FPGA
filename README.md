# RISCV-FPGA

RVfpga Workshop Installation Guide

Please follow these steps to install the software on your laptop for the RVfpga Workshop. Install the following (as described in detail below):

1.	Visual Studio Code (VSCode)
2.	PlatformIO (an extension within VSCode)
3.	ChipsAlliance Platform
4.	GTKWave

The Appendix is needed only for laptops using Windows OS. The Appendix shows how to install the drivers needed for PlatformIO.



1.	Install VSCode:

a.	Download the installation file from the following link: https://code.visualstudio.com/Download

b.	Open a terminal, and install and execute VSCode:
cd ~/Downloads
sudo dpkg -i code*.deb
code

Windows / macOS: VSCode packages are also available for Windows (.exe file) and macOS (.zip file) at https://code.visualstudio.com/Download. Follow the usual steps used for installing and executing an application in these operating systems.



2.	Install PlatformIO on top of VSCode:

a.	Install python3 utilities by typing the following in a terminal:
sudo apt install -y python3-distutils python3-venv 

Windows / macOS: this step (2.a) is not required in Windows. As for macOS, you can use homebrew to install python3: brew install python3

b.	If not yet open, start VSCode by selecting the Start button and typing “VSCode” in the search menu, then select VSCode, or type code in an Ubuntu terminal.

c.	In VSCode, click on the Extensions icon   located on the left side bar of VSCode (see Figure 1).

 
Figure 1. VSCode’s Extensions icon

d.	Type PlatformIO in the search box and install the PlatformIO IDE by clicking on the install button next to it (see Figure 2).

 
Figure 2. PlatformIO IDE Extension

e.	The OUTPUT window on the bottom will inform you about the installation process. Once finished, click “Reload Now” on the bottom right side window, and PlatformIO will finish installing inside VSCode (see Figure 3).

 
Figure 3. Reload Now after PlatformIO installs

Nexys A7 cable drivers installation: you need to manually install the drivers for the Nexys A7 board.
o	Open a terminal.
o	Go into directory [RVfpgaPath]/RVfpga/driversLinux_NexysA7. (For simplicity, we provide these drivers inside the RVfpga folder. When you install Vivado in Section 5 of this guide, you can also find these drivers inside the downloaded package as described in that section.)
o	Run the installation script:
chmod 777 *
sudo ./install_drivers
o	Unplug the Nexys A7 board from your computer and restart the computer for the changes to have effect.

Windows: follow the instructions provided in Appendix at the end of the document for installing the drivers for the Nexys A7 board.

macOS: it is not necessary to install any additional drivers.



3.	Install ChipsAlliance Platform:

-	Click on the PlatformIO icon in the left ribbon menu:  . Then expand PIO Home and click on Open. Now PIO Home will open to the Welcome window (see Figure 4).

 
Figure 4. Open PIO Home


-	In the PIO Home, click on the   button and then on the   tab (Figure 5). Look for Chipsalliance (the platform that we use in RVfpga) and open it by clicking on the   button (Figure 5).

 
Figure 5. Selecting the CHIPS Alliance Platform

-	After clicking on the   button, you will see the details of the Chips Alliance platform (as in Figure 6). Install it by clicking on the   button (Figure 6).


 
Figure 6. Installing the CHIPS Alliance Platform

-	Once installation completes, a summary of the tools that have been installed is shown, as in Figure 7. Click   to close that window.

 
Figure 7. Successful installation of CHIPS Alliance Platform



4.	Install GTKWave:

a.	Linux: Open a terminal, and install GTKWave:
	sudo apt-get install -y gtkwave

b.	Windows: GTKWave can be downloaded as a precompiled package from https://sourceforge.net/projects/gtkwave/files/. Look for the most recent Windows package, and download, execute and use it in your Windows machine.

c.	MacOS: You will use Homebrew to install gtkwave. But this time we need to use cask because it is a GUI macOS application.  Type the following commands in an open Terminal:
	brew tap homebrew/cask
	(If xquartz is not installed yet)  brew cask install xquartz
	brew cask install gtkwave
After the installation, an icon for gtkwave.app should appear in the Application folder. In order to use it from the command line, you may need to install Perl’s Switch module:
	cpan install Switch


 
Appendix: Installing drivers in Windows to use PlatformIO

To download the Zadig executable, browse to the following website (see Figure 8):

   https://zadig.akeo.ie/

 
Figure 8. Install Nexys A7 board driver used by PlatformIO

Click on Zadig 2.5 and save the executable. Then run it (zadig-2.5.exe), which is located where you downloaded it. You can also type zadig into the Start menu to find it. You will probably be asked if you want to allow Zadig to make changes to your computer and if you will let it check for updates. Click Yes both times.

Connect the Nexys A7 Board to your computer and switch it on. In Zadig, click on Options → List All Devices (see Figure 9).

 
Figure 9. List all devices in Zadig

If you click on the drop-down menu, you will see Digilent USB Device (Interface 0) and Digilent USB Device (Interface 1) listed. You will install new drivers for only Digilent USB Device (Interface 0) (see Figure 10).

 
Figure 10. Install WinUSB driver for Digilent USB Device (Interface 0)

You will now replace the FTDI driver with the WinUSB driver, as shown in Figure 11. Click on Replace Driver (or Install Driver) for Digilent USB Device (Interface 0). You are installing the driver for the Nexys A7 board or, if you previously installed Vivado, you are replacing the FTDI driver used by Vivado with the WinUSB driver used by PlatformIO. 

 
Figure 11. Replace driver for Nexys A7 board

After some time, typically several minutes, Zadig will indicate the driver was installed correctly. Click Close and then close the Zadig window.

Next time you use PlatformIO you do not need to re-install the driver. However, note that this driver is not compatible with Vivado in Windows. So you can no longer use Vivado to download bitfiles to the FPGA board. If you wanted to use Vivado to download bitfiles (not recommended) you would need to revert the driver back to the original driver installed with Vivado, as described in Appendix E of the Getting Started Guide.


