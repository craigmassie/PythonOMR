# Python Optical Mark Recognition
Ever wanted to find checkboxes in a document? Of course you have. You're in luck!

## Usage
`python check_finder.py <file_name> <check_type> <percentage_for_filled>`

### check_type 

* `all`: Displays all the checkboxes found as output
* `empty`: Only displays the empty checkboxes as output
* `filled`: Only displays the filled checkboxes as output

### percentage_for_filled
The percentage required of non white pixels for the check to be considered `filled`.

## Example
`python check_finder.py manyboxes.png filled 25%`  

[![Screenshot-2019-02-25-at-11-01-56.png](https://i.postimg.cc/wjsv4dck/Screenshot-2019-02-25-at-11-01-56.png)](https://postimg.cc/fVDDkpP3)
