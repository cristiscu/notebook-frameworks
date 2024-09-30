This is a single **line**, not displayed properly!
Followed by another usual line, just to prove it.

This is a proper line, ending with two spaces.  
Followed by another proper line, ending as an alternative with a HTML tag.<br>
Followed by another usual line.

What follows are two **horizontal lines**, using either --- or *** markdown notations, on separate lines:

---
***

This is a **paragraph**, separated from the next one by an empty line (with or without spaces).

This is the next paragraph.

<p>And these are paragraphs using HTML tags (no empty lines between).</p>
<p>This is the next paragraph.</p>

**Code blocks** can use triple-backticks as separators:
```
var x = 123
print(x)
```

You can also specify the programming language on top, for proper code syntax highlighting:
```python
var x = 123
print(x)
```

A monospaced font (like Courier) can be used with text within backticks to show **inline code** or special characters/tags, as in `<p>...</p>`. (Try it without them, as it will not work!)

> **Blockquote**, as simple-indented text, for lines with >.
>
> Some other line (separated by an empty line with >).
>> **Double-indented text**, for lines starting with >> instead.

**Bulleted lists** (prefix items by * or -, TAB for nesting):

* item1
* item2
    - item21
    - item22
        - item221
- item3

**Numbered lists** (prefix items by 1., or 2. etc, TAB for nesting):

1. item1
2. item2
    1. item21
    1. item22
        1. item221
3. item3

**Tables**:

Column 1  | Column 2
----------|----------
cell11    | cell12
cell21    | cell22

Column 1|Column 2
-|-
cell11|cell12
cell21|cell22

Table with left/center/right-aligned text (use : under the header):

Header 1|Header 2|Header 3
---|:---:|---: 
left|center|right
left|center|right
left|center|right

**LaTeX** equation (`$$..$$`): $$y=x^2$$

inline LaTeX equation (`$..$`): $y=x^2$

