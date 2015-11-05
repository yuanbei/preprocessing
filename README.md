### Preprocessing
Preprocessing is the tools for doing the preprocessing bussiness for non c famliy language.
You can use it in java code like this:

`
public class TestClass  extends Application
{
#if defined(WOW_BUILD)
     public String a = "abc";
#else     
     public String a = "def";
#endif
}
`

If you run python shell like this

`
python preprocessing.py -f testclass.java -c config.json
`

The out put file's content is like this

`
public class TestClass  extends Application
{
     public String a = "abc";
}
`
