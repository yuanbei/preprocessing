### Run preprocessing for non c family languages
Preprocessing is a python tool which completes the preprocessing bussiness for non c famliy language.

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

After doing preprocessing on this file, the out put file's content is like this

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
preprocessor.py [-h] [-i INPUT] [-m MACROS] [-o OUTPUT] [-e EXCLUDE]
```

optional arguments:
```python
optional arguments:
  -h, --help            Show this help message and exit
  -i INPUT, --input INPUT
                        Path to a directory or a file
  -m MACROS, --macros MACROS
                        Macros define file, contents split by comma
  -o OUTPUT, --output OUTPUT
                        Path to the output files directory
  -e EXCLUDE, --exclude EXCLUDE
                        Excluded files file
```
### Support three basic macro commands
1. include
2. define
3. undef

### Please Note
1. It will traverse the input files, do preprocessing for every file if the file path
does not in excluded file list.

2. It supports three macros command inlcude #define, #incldue,#undefine.

3. If macros file contains this content "WOW_BUILD 1; WOW_I18N", it will be translated
into two macro command "#define WOW_BUILD 1", "#define WOW_I18N".

4. Exclude files file can be used to exclude some special files and directories.If
it contains this content ".python .git", every file path contain .python or .git will
be excluded. ie home/test/.git/test.java.
