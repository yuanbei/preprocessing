public class TestClass  extends Application           
    {

// Test comment
#if !defined(WOW_BUILD)
     public String a = "abc";               
#else
     public String a = "def";               
#endif
#if 0
     public int a = 0;
#endif
#if 1
    public int b =2;
#else 
#endif
   }      
