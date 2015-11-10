### Preprocessing
Preprocessing is the tools for doing the preprocessing bussiness for non c famliy language.
You can use it in java code like this:

```java
public class TestClass  extends Application
{
#if defined(WOW_BUILD)
     public String a = "abc";
#else     
     public String a = "def";
#endif
}
```

If you run python shell like this

```python
python preprocessing.py -i testb/ -m macros.txt -o testout/ -e exclude.txt
```

The out put file's content is like this

```java
public class TestClass  extends Application
{
     public String a = "abc";
}
```
### Requirements
[PLY(Python Lex-Yacc)](https://github.com/dabeaz/ply)

### Usage 
```python
preprocessing.py [-h] [-i INPUT] [-m MACROS] [-o OUTPUT] [-e EXCLUDE]
```

optional arguments:
```python
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        path to the input files dictionary
  -m MACROS, --macros MACROS
                        macros define file, contents split by comma
  -o OUTPUT, --output OUTPUT
                        path to the output files dictionary
  -e EXCLUDE, --exclude EXCLUDE
                        excluded files file
```
