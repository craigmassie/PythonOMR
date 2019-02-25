# Python Optical Mark Recognition
Ever wanted to find checkboxes in a document? Of course you have.

## Usage
`python check_finder.py <file_name> <check_type> <percentage_for_filled>`

### check_type 

* `all`: Displays all the checkboxes found as output
* `empty`: Only displays the empty checkboxes as output
* `filled`: Only displays the filled checkboxes as output

### percentage_for_filled
The percentage required of non white pixels for the check to be considered `filled`.

## Example
`python check_finder.py ./test_images/manyboxes.png filled 25%`  

[![edited.png](https://i.postimg.cc/SKBHSNd1/edited.png)](https://postimg.cc/bGRmLPK1)
