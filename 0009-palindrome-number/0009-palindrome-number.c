bool isPalindrome(int x) 
{
long temp=x;
long rev=0;
while(x>0){
    long dig=x%10;
    rev=rev*10+dig;
    x=x/10;
}
if(temp==rev){
    return true;
}
else{
    return false;
}
}