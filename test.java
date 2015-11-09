public class TestClass  extends Application
{
// Test comment
#if !defined(WOW_BUILD)
     public String a = "abc";
#else     
     public String a = "def";
#endif
}
